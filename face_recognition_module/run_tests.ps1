coverage run  --omit **/__init__.py,tests/**,test_detection.py,test_recognition.py -m unittest discover
coverage report -i