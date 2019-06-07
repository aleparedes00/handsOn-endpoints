import connexion
from google.cloud import firestore

db = firestore.Client()

def health_check():
    return "Hello!", 200

def get_all_procucts():
    json_payload = connexion.request.json

    # Get products from database
    users_ref = db.collection(u'users')
    docs = users_ref.get()

    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))


def add_product():
    json_payload = connexion.request.json

    # Add a new document
    doc_ref = db.collection(u'products').document(u'product-')
    doc_ref.set({
        u'id': u'12',
        u'name': u'bananes',
        u'price': 2.5
    })
