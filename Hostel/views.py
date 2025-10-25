from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages  # Import messages framework
from django.contrib.auth import authenticate,login as auth_login
from .models import HostelUser,Profile 
from django.contrib.auth.decorators import login_required

def register_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpass = request.POST.get('cpass')

        # Check if passwords match
        if password != cpass:
            messages.error(request,"Password do not match")
            return redirect('register_page')

        # Check if username already exists
        if User.objects.filter(username=name).exists():
            return HttpResponse("Username already taken. Please choose another one.")

        # Check if email already exists (optional but recommended)
        if User.objects.filter(email=email).exists():
            return HttpResponse("Email is already in use. Try another one.")
        
        # Save the data in database
        HostelUser.objects.create(
            name=name,
            email=email,
            password=password
        )
        messages.success(request,"Account created successfully!")
        return redirect('login')  # Redirect to login page after successful registration

    return render(request, 'signup.html')



def user_login(request):  # Renamed from 'login' to 'user_login'
    if request.method == 'POST':
        username = request.POST.get('username') # from form input
        password = request.POST.get('password') # from form input
        
        try:
            # check user in HostelUser table
            hostel_user = HostelUser.objects.get(name=username, password=password)
            # if found, store session
            request.session['hostel_user_id'] = hostel_user.id
            request.session['hostel_user_name'] = hostel_user.name
            messages.success(request, f"Welcome {hostel_user.name}!")
            return redirect('index')  # after login go to home/index
        except HostelUser.DoesNotExist:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')

def user_logout(request):
    request.session.flush()
    return redirect('login')

# Create your views here.
def index(request):
    floors = range(1, 9)  # Floors 1 to 7
    return render(request, "index.html", {"floors": floors})
    # return render(request,'index.html')




def booking(request):
    # Get floor number (default = 1)
    floor = int(request.GET.get("floor", 1))

    rooms = []
    for i in range(1, 15):  # 101–114, 201–214, etc.
        room_number = f"{floor}{str(i).zfill(2)}"

        if 1 <= i <= 4:   # Single Sharing
            sharing = "Single Sharing"
            btn = "book"   # Book Now
        elif 5 <= i <= 8:  # Two Sharing
            sharing = "Two Sharing"
            btn = "select"
        elif 9 <= i <= 12: # Three Sharing
            sharing = "Three Sharing"
            btn = "select"
        else:              # 113–114 → Four Sharing
            sharing = "Four Sharing"
            btn = "select"

        rooms.append((room_number, sharing, btn))

    return render(request, "booking.html", {"floor": floor, "rooms": rooms})



# def booking(request):
#     # Get floor number (default = 1)
#     floor = int(request.GET.get("floor", 1))

#     rooms = []
#     for i in range(1, 15):  # 101–114, 201–214, etc.
#         room_number = f"{floor}{str(i).zfill(2)}"

#         if 1 <= i <= 4:   # Single Sharing
#             sharing = "Single Sharing"
#             beds = 1
#             btn = "book"
#         elif 5 <= i <= 8:  # Two Sharing
#             sharing = "Two Sharing"
#             beds = 2
#             btn = "select"
#         elif 9 <= i <= 12: # Three Sharing
#             sharing = "Three Sharing"
#             beds = 3
#             btn = "select"
#         else:              # 13–14 → Four Sharing
#             sharing = "Four Sharing"
#             beds = 4
#             btn = "select"

#         rooms.append({
#             "room_number": room_number,
#             "sharing": sharing,
#             "beds": beds,
#             "btn": btn,
#         })

#     return render(request, "booking.html", {"floor": floor, "rooms": rooms})


















# def selectroom(request):
#     room_type = request.GET.get("room_type")
#     room_number = request.GET.get("room_number")

#     # Decide bed count from room type
#     if room_type == "Two Sharing":
#         bed_count = 2
#     elif room_type == "Three Sharing":
#         bed_count = 3
#     elif room_type == "Four Sharing":
#         bed_count = 4
#     else:
#         bed_count = 1  # default

#     # Create a list of bed numbers
#     beds = list(range(1, bed_count + 1))

#     return render(request, "selectroom.html", {
#         "room_type": room_type,
#         "room_number": room_number,
#         "beds": beds
#     })



# def confirmbooking(request):
#     room_type = request.GET.get("room_type", "")
#     room_number = request.GET.get("room_number", "")
#     bed_number = request.GET.get("bed_number", "")
#     return render(request, "confirmbooking.html", {
#         "room_type": room_type,
#         "room_number": room_number,
#         "bed_number": bed_number
#     })
#     # check if hostel_user_id exists in session
#     if not request.session.get("hostel_user_id"):
#         return redirect("login")   # redirect to login if not logged in
    
#     return render(request, "confirmbooking.html")




from django.shortcuts import render, redirect
from .models import Booking

def confirmbooking(request):
    # Check login session
    if not request.session.get("hostel_user_id"):
        return redirect("login")   # redirect to login if not logged in

    if request.method == "POST":
        # Save booking details from form
        booking = Booking.objects.create(
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            gender=request.POST.get("gender"),
            dob=request.POST.get("dob") or None,

            phone=request.POST.get("phone"),
            email=request.POST.get("email"),

            check_in=request.POST.get("check_in"),
            check_out=request.POST.get("check_out"),
            room_type=request.POST.get("room_type"),
            room_number=request.POST.get("room_number"),
            bed_number=request.POST.get("bed_number"),

            id_type=request.POST.get("id_type"),
            id_number=request.POST.get("id_number"),
            payment_method=request.POST.get("payment_method"),
            payment_reference=request.POST.get("payment_reference"),

            special_requests=request.POST.get("special_requests"),
            emergency_contact_name=request.POST.get("emergency_contact_name"),
            emergency_contact_phone=request.POST.get("emergency_contact_phone"),
            address=request.POST.get("address"),

            terms_accepted=bool(request.POST.get("terms")),
        )
        booking.save()

        # After saving, redirect to a success/confirmation page
        return redirect("index")  # create this template/view

    # GET request → render form with pre-filled values
    room_type = request.GET.get("room_type", "")
    room_number = request.GET.get("room_number", "")
    bed_number = request.GET.get("bed_number", "")

    return render(request, "confirmbooking.html", {
        "room_type": room_type,
        "room_number": room_number,
        "bed_number": bed_number,
    })






def profile(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        dob = request.POST.get("dob")
        address = request.POST.get("address")
        course = request.POST.get("course")
        college = request.POST.get("college")
        phone = request.POST.get("phone")
        profile_image = request.FILES.get("profile_image")

        # Save data to database
        profile = Profile(
            full_name=full_name,
            dob=dob,
            address=address,
            course=course,
            college=college,
            phone=phone,
            profile_image=profile_image
        )
        if profile_image:
            profile.profile_image = profile_image
        profile.save()

        return render(request, "profile.html", {"request": request, "profile": profile})
    return render(request, "profile.html")






def about(request):
    return render(request,'about.html')

def facilities(request):
    return render(request,'facilities.html')

def facilities1(request, room1):
    return render(request, "facilities1.html", {"facility": room1})

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        # Save to DB
        contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect("contact")  # redirect to the same page    
    return render(request,'contact.html')
