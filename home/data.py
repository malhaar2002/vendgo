from asyncio.windows_events import NULL
import os
import firebase_admin
from firebase_admin import credentials
from google.cloud import firestore
from firebase_admin import firestore
from home import views

from vendgoDjango.settings import BASE_DIR

cred = credentials.Certificate(os.path.join(BASE_DIR, 'home/serviceAccountKey.json'))
#cred = credentials.Certificate('home/serviceAccountKey.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def add_new_user_details(name, email, number, buisness, GSTIN, industry, Location, iam):
    doc = db.collection(iam).document(email)
    doc.set({'email' : email, "GSTIN" : GSTIN, "buisness_name" : buisness, "location" : Location, "contact_number" : number, "name" : name, "industry" : industry, "my_bid" : []})

def get_vendor(material_name):
    doc = db.collection('Vendor').where('material_catalog','array_contains', material_name).get()
    vendor = []
    
    i = 0
    for ele in doc:
        vendor.append((ele.to_dict())['buisness_name'])

    return vendor

def post_request(material, vendor, band, quantity, user_email):
    doc = db.collection("bids").document()
    doc.set({"material" : material, "vendor_name" : vendor, "band" : band, "quantity" : quantity, "id" : doc.id})
    bid_id = doc.id
    doc = db.collection('Retailer').document(user_email)
    data1 = doc.get()
    data = data1.to_dict()["my_bids"]
    data.append(bid_id)
    doc.update({"my_bids" : data})

def retailer_vendor(email):
    vendor = db.collection("Vendor").where("email", "==", email).get()
    retailer = db.collection("Retailer").where("email", "==", email).get()
    if_vendor = []
    if_retailer = []

    for ele in retailer:
        if_retailer.append(ele.to_dict())
    for ele in vendor:
        if_vendor.append(ele.to_dict())

    if vendor == []:
        return True
    if retailer == []:
        return False

def my_bids(email):
    data = db.collection("Retailer").document(email).get()
    
    my_bid_id = []
    my_bid = []
    
    my_bid_id = list((data.to_dict())["my_bids"])
    
    for ele in my_bid_id:
        data = db.collection("bids").document(ele).get()
        temp = []
        temp.append((data.to_dict())['material'])
        temp.append((data.to_dict())['vendor_name'])
        temp.append((data.to_dict())['band'])
        temp.append((data.to_dict())['quantity'])
        my_bid.append(temp)
        temp = []

    return(my_bid)

def available_bids():
    data = db.collection("bids").where(u"material", u"!=", u"").get()
    aval_bids = []
    
    for ele in data:
        temp = []
        temp.append((ele.to_dict())['material'])
        temp.append((ele.to_dict())['vendor_name'])
        temp.append((ele.to_dict())['band'])
        temp.append((ele.to_dict())['quantity'])
        temp.append((ele.to_dict())['id'])

        aval_bids.append(temp)

    return(aval_bids)

def submit_aval_bid(id, quantity):
    doc = db.collection("bids").document(id)
    data = doc.get()
    data1 = data.to_dict()["quantity"]
    data2 = str(int(data1) + int(quantity))
    doc.update({"quantity": data2})
