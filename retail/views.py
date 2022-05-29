from django.shortcuts import render, redirect
from django.http import HttpResponse
from home import data

materials = ['Brass', 'Iron', 'Steel']

def index(request):
    d = {'material': materials}
    if request.method == 'POST':
        material = request.POST['material']
        vendor = request.POST['vendor']
        band = request.POST['band']
        quantity = request.POST['units_required']
        expiry = request.POST['expiry']
        final = {'material':material, 'vendor':vendor, 'band':band, 'quantity':quantity, 'expiry':expiry}
        data.post_request(material,vendor,band,quantity,request.session.get('email')) #store this data in the database
        return redirect("/retail")
    return render(request,'add_request.html',d)

def load_vendors(request):
    material_name = request.GET.get('material')
    vendors = data.get_vendor(str(material_name).lower())
    return render(request, 'vendors_dropdown_list_options.html', {'vendors': vendors})

def load_bands(request):
    material_name = request.GET.get('material')
    vendor_name = request.GET.get('vendor')
    return render(request, 'bands_dropdown_list_options.html', {'bands':['40-60 for $400/unit', '60-80 for $300/unit', '80-100 for $200/unit']})

def show_dash(request):
    my_bids = data.my_bids(request.session.get('email'))
    in_bids = []
    return render(request, 'retailer_dashboard.html', {"my_bids":my_bids, "in_bids":in_bids})

def all_av_bids(request):
    av_bids = data.available_bids()
    if request.method == "POST":
        bid = int(request.POST['bid_no'])
        global bid_id
        bid_id = av_bids[bid][4]
        return render(request, 'view_available_bid.html', {"material":av_bids[bid][0], "vendor":av_bids[bid][1], "ppu":av_bids[bid][2], "quota":av_bids[bid][3]})
    for i in range(len(av_bids)):
        av_bids[i] = av_bids[i][0:4]
    return render(request, 'available_bids.html', {"av_bids":av_bids})

def view_bid(request):
    if request.method == "POST":
        quantity = request.POST['quantity']
        data.submit_aval_bid("6s9l4osub4U3qBV582qM", "10")
        return redirect("/retail")
    return redirect('retail/find_bid')
    


