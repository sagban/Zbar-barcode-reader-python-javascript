# Zbar-barcode-reader-python-javascript
A bar code reader which detects and read barcode and Qr codes from the live streaming webcam, laptop cam and mobile phones (back and front both) camera.

Features
-------

- Reads and decodes any type of bar code and qr code from the live camera stream.
- Compatible with all the modern devices.
- Can be accessible from the mobile camera (back and front both)
- Uses javascript `getUserMedia ` API call to get live camera feed.
- Uses Python open source library (Zbar) Pyzbar for barcode decoding.
- Runs on Django server.
Note: Code can be use on different python frameworks.
Important Files: `/bar/static/js/main.js` `/bar/views.py` `/bar/barcode.py`

Usage
-------

**To run locally:**

First fork this repository and then follow these steps:
```
git clone https://github.com/your-name/Zbar-barcode-reader-python-javascript.git
cd Zbar-barcode-reader-python-javascript
pip install -r requirements.txt
python manage.py runserver
```
Now open [127.0.0.1:8000](127.0.0.1:8000 "127.0.0.1:8000") locally on your browser.


*Note: Starting with Chrome 47, `getUserMedia()` requests are only allowed from secure origins: HTTPS or localhost.*

**Solution: For development use `django-sslserver` for testing on different mobile devices and IP other than localhosts. Find this out [here](https://github.com/teddziuba/django-sslserver "here")*


Sequence Diagram
------------- 

![Sequence](./brief.svg)


End
----
