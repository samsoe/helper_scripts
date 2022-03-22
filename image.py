import os
import tempfile

from google.cloud import storage, vision
from wand.image import Image

storage_client = storage.Client()
vision_client = vision.ImageAnnotatorClient()

bucket = storage_client.get_bucket("mpgn_buckeye_images")

# create a list of all objects in bucket
blob_iterator = bucket.list_blobs(prefix="2022-01-20_mpgn_buckeye_images", client=storage_client)

# Resizes the given file using ImageMagick.
def resize_img(current_blob):
    file_name = current_blob.name
    _, temp_local_filename = tempfile.mkstemp()

    # Download file from bucket.
    current_blob.download_to_filename(temp_local_filename)
    print(f"Image {file_name} was downloaded to {temp_local_filename}.")

    # Resize the image using ImageMagick.
    with Image(filename=temp_local_filename) as image:
        image.resize(256, 256)
        image.save(filename=temp_local_filename)

    print(f"Image {file_name} was resized.")

    # Upload result to a second bucket
    resize_bucket_name = "mpgn_buckeye_images_resized"
    resize_bucket = storage_client.bucket(resize_bucket_name)
    new_blob = resize_bucket.blob(file_name)
    new_blob.upload_from_filename(temp_local_filename)
    print(f"Resized image uploaded to: gs://{resize_bucket_name}/{file_name}")

    os.remove(temp_local_filename)


# Iterate through objects in bucket
for blobi in blob_iterator:
    if blobi.name[-4:] == ".jpg":
        resize_img(blobi)
