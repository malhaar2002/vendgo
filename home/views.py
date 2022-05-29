from django.shortcuts import render, redirect
from home import authenticate, data

def signup_page(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        buisness = request.POST['business_name']     
        gstin = request.POST['gstin']
        number = request.POST['contactno']  
        name = request.POST['name']   
        location = request.POST['location']
        industry = request.POST['industry']
        iam = request.POST['iam']
        context = {'email':email}
        authenticate.create_user(email, password)
        request.session['email'] = email
        data.add_new_user_details(name,email,number,buisness,gstin,industry,location,iam)
        if str(iam).lower() == "retailer":
            return render(request, 'retailer_dashboard.html', context)
        elif str(iam).lower() == "vendor":
            return render(request, 'vendor_dashboard.html', context)
    return render(request, 'register.html')

def login_page(request):
    if request.method == "POST":
            email = request.POST["your_email"]
            password = request.POST["your_pass"]

            data_auth = authenticate.login_check(str(email), str(password))
            context = {'email':email}
            
            if data_auth == True:
                request.session["email"] = email
                if data.retailer_vendor(email) == True:
                    return redirect('/retail')
                else:
                    return render(request, 'vendor_dashboard.html', context)  
                     
            if data == True:
                request.session['email'] = email
                return render(request, 'vendor_dashboard.html', context)
    
    return render(request, "login.html")