import logging
import os
import azure.functions as func
from azure.storage.blob import BlobServiceClient


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    print("Connection String:", os.getenv("NewAzureWebJobsStorage"))
    # Initialize BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(os.getenv("NewAzureWebJobsStorage"))
    
    # Specify the container name
    container_name = 'my-container'  # replace with your actual container name
    container_client = blob_service_client.get_container_client(container_name)
    
    # List blobs in the container
    blob_list = container_client.list_blobs()
    blobs = [blob.name for blob in blob_list]

    # Return blob names as a response
    return func.HttpResponse(f"PMtest1 - Peter Macfie has got this working :-)\nBlobs in '{container_name}': {', '.join(blobs)}")

