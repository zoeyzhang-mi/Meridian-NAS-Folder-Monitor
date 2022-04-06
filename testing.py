import requests

my_data = {
    'date': '2021-12-29 16:13:31', 
    'serialNumber': 'SN152F01036941', 
    'vendorLot': 'VendorLotnumber', 
    'operatorID': 'Operator', 
    'result': 'PASS', 
    'summary': 'SENSORs out of range:0, PIXELs out of range:0', 
    'moduleType': 2, 
    'batchComment': 
    'CJ51--2021-12-29 003A', 
    'batchName': 'B1P00008', 
    'testResult': {'PIXEL(40,30)': 8104, 'Summary': 'SENSORs out of range:0, PIXELs out of range:0'}, 
    'macID': '04C76A035015432EA76BD9302E6DD386', 
    'guiVersion': 'V3.8.7', 
    'firmwareVersion': '03.03.1', 
    'position': 'Unit1', 
    'waferNumber': 919, 
    'waferCoordX': 13, 
    'waferCoordY': 5, 
    'waferErrorCode': 'X370', 
    'testConditions': {'blackbody': 60, 'module': 60}, 
    'blackbody': 60, 
    'module': 60, 
    'rework': 0, 
    'Summary': 'B01'}

url='http://192.168.50.131:5000/testing'
r = requests.post(url, json=my_data, timeout=10)

#r = requests.get(url, json=my_data, timeout=10)
print(r.url)
print(f"Status Code: {r.status_code}, Response: {r.json()}")

