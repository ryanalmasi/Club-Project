import requests
import pickle
import json

receiptEndpoint = 'https://ocr.asprise.com/api/v1/receipt'
receipt = 'receipt.jpeg'

r = requests.post(receiptEndpoint,
                  data = {'api_key': 'Test', 'recognizer': 'auto', 'ref_no': 'oct_python_123'},
                  files = {'file': open(receipt, 'rb')})

try:
    with open(r.text, "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print('End')


print(data['receipts'])
print()
print(data['items'])