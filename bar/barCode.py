from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
from PIL import Image
import re
import io
import base64, json



def decode(url):
    # Find barcodes and QR codes

    imgstr = re.search(r'base64,(.*)', url).group(1)
    image_bytes = io.BytesIO(base64.b64decode(imgstr))
    im = Image.open(image_bytes)

    arr = np.array(im)[:, :, 0]
    decodedObjects = pyzbar.decode(arr)
    print(decodedObjects)


    # return decodedObjects.Decoded
    # Print results
    data = []

    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data, '\n')
        data.append({
            "code":obj.data.decode('utf-8') ,
            "type": obj.type
        })
        # return "Code: "+code.decode('utf-8') + "\nType: "+ types
    #data = serializers.serialize('json', data)
    print(data)
    return data
