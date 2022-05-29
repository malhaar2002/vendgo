from django.shortcuts import render

# Create your views here.
def vendor_dashboard(request):
    return render(request, 'vendor_dashboard.html')

def view_order(request):
    return render(request, 'view_order.html')

def view_catalogue(request):
    data = [["wool", 100, 200, 30], ["wool", 200, 300, 50], ["quartz", 100, 300, 60]]
    context = {'data': data}
    return render(request, 'catalogue.html', context)

def add_band(request):
    if request.method == "POST":
        material = request.POST['material']
        min_quantity = request.POST['min_quantity']
        max_quantity = request.POST['max_quantity']
        ppu = request.POST['ppu']
    return render(request, 'add_band.html')