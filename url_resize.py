import sys
from PIL import Image
import requests

# command line argument is manifest.csv
filename = sys.argv[1]

with open(filename) as f:
    lines = f.readlines()

for url in lines:
    url = url.strip()
    im = Image.open(requests.get(url, stream=True).raw)
    filename = url.split("/")[-1]
    im.save('resized/' + filename, "JPEG", dpi=(256,256))
