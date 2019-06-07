# Products API
API to create new products and get products (mocked)

## Test locally with Python

## Build & push docker image
### Build
    
    docker build -t gcr.io/sandbox-tlengyel/products-api .

### Test the image locally

    docker run -p 8080:8080 gcr.io/sandbox-tlengyel/products-api

### Push the image to the registry
    
    docker push gcr.io/sandbox-tlengyel/products-api

## Deploy the backend app
Test it by accessing the Cloud Run service. Then remove allUsers from Invoker role. Test it has been removed. 
    
## Deploy Cloud Endpoints service

## Deploy ESP

## Test everything
And test the portal