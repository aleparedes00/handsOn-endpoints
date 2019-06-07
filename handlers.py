import connexion
from flask import abort
from google.cloud import firestore

# Database settings
db = firestore.Client()
products_ref = db.collection('products')


def get_product(product_id):
    product = products_ref.where('id', '==', product_id).get()

    try:
        return next(product).to_dict()
    except StopIteration:
        abort(404)


def get_all_products():
    # Get products from database
    all_products = list(map(lambda d: d.to_dict(), products_ref.get()))

    return all_products


def add_products():
    # Extract products from body
    json_payload = connexion.request.get_json()

    # Add a new products to database
    for product in json_payload:
        doc_ref = products_ref.document('product-{}'.format(product.get('id')))
        doc_ref.set({
            'id': product.get('id'),
            'title': product.get('title'),
            'price': product.get('price')
        })

    return {"message": "{} products saved".format(len(json_payload))}
