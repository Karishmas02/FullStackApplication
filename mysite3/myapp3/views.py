from django.shortcuts import render
import json
from .models import Register
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse

# def home(request):
#     return HttpResponse("<h1>I am venogopal from Title park</h1>")


@csrf_exempt
def reg(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        Fname=data.get("Fname")
        Lname=data.get("Lname")
        Phone=data.get("Phone")
        Email=data.get("Email")
        Password = data.get("Password")

        Register.objects.create(
        Fname=Fname,
        Lname=Lname,
        Phone=Phone,
        Email=Email,
        Password=Password)  
        return JsonResponse({"message":"Registered Succesfully"},status=201)
    return JsonResponse({"error":"POST METHOD ONLY"},status=405)



@csrf_exempt

def login(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        Email = data.get("Email")
        Password = data.get("Password")
        user  = Register.objects.filter(Email=Email,Password=Password)  
        if user:
            return JsonResponse({"message":"Login Successfully"})
        else:
            return JsonResponse({"message":"Invalid email or password"})
    return JsonResponse({"Error":"Post method is required"})

#getdata
# @csrf_exempt #decorators
# def get_data(request):
#     if request.method == "GET":
#         datas= Register.objects.all()
#         user = []
#         for  data in datas:
#             user.append({
#                 "id":data.id,
#                 "firstname":data.Fname
#             })
#         return JsonResponse({"Details":user})
#     return JsonResponse({"Error":"GET method only"})



@csrf_exempt
def get_data(request):
    if request.method=="GET":
        data=Register.objects.all()
        sample = []
        for users in data:
            sample.append({
            "Firstname":users.Fname,
            "Lastname":users.Lname,
            "Phone" : users.Phone,
            "Email" : users.Email,
            "Password":users.Password
            })
        return JsonResponse({"Details":sample})
    return JsonResponse({"Error":"Get method only"})

@csrf_exempt
def delete_data(request):
    if request.method =="DELETE":
        data = json.loads(request.body.decode("utf-8"))
        Id=data.get("id")
        remove = Register.objects.filter(id=Id)
        if remove.exists():
            remove.delete()
            return JsonResponse({"message":"Deleted Successfully"})
        else :
            return JsonResponse({"message":"Deleted unSuccessfully"})
    return JsonResponse({"Error":"Delete method only"})   
    
# @csrf_exempt
# def update_data(request):
#     if request.method == "PUT":
#         data = json.loads(request.body.decode("utf-8"))
#         Id = data.get("id")
#         Fname = data.get("Fname")
#         Lname = data.get("Lname")
#         Phone = data.get("Phone")
#         Email = data.get("Email")
#         Password = data.get("Password")
#         user = Register.objects.filter(id=Id)
#         if user.exists():
#             user = user.first()
#             if Fname:
#                 user.Fname = Fname
#             if Lname:
#                 user.Lname = Lname
#             if Phone:
#                 user.Phone = Phone
#             if Email:
#                 user.Email = Email
#             if Password:
#                 user.Password = Password
#             user.save()
#             return JsonResponse({"message": "Updated Successfully"})
#         else:
#             return JsonResponse({"message": "User not found"})
#     return JsonResponse({"Error": "PUT method only"})


@csrf_exempt
def update_data(request):
    if request.method == "PUT":
        data = json.loads(request.body.decode("utf-8"))
        Id = data.get("id")
        if not Register.objects.filter(id=Id).exists():
            return JsonResponse({"message": "User not found"}, status=404)
        Register.objects.filter(id=Id).update(
            Fname=data.get("Fname"),
            Lname=data.get("Lname"),
            Phone=data.get("Phone"),
            Email=data.get("Email"),
            Password=data.get("Password")
        )
        return JsonResponse({"message": "Updated Successfully"})
    return JsonResponse({"Error": "PUT method only"}, status=400)




# @csrf_exempt
# def update_data(request):
#     if request.method == "PUT":
#         data = json.loads(request.body.decode("utf-8"))
#         Id =data.get("id")
#         Register.objects.filter(id=Id).update(
#         Fname =data.get("Fname"),
#         Lname = data.get("Lname"),
#         Phone = data.get("Phone"),
#         Email = data.get("Email"),
#         Password = data.get("Password")
#         )
#         return JsonResponse({"meassage":"updated successfully"})
#     return JsonResponse({"Error":"put method only"})



@csrf_exempt
def update_data(request):
    if request.method == "PUT":
        data = json.loads(request.body.decode("utf-8"))
        Id = data.get("id")
        if not Register.objects.filter(id=Id).exists():
            return JsonResponse({"message":"User not found"})
        Register.objects.filter(id=Id).update(
        Fname=data.get("Fname"),
        Lname=data.get("Lname"),
        Phone=data.get("Phone"),
        Email=data.get("Email"),
        Password=data.get("Password")
        )
        return JsonResponse({"message":"Updated Scuccessfully"})
    return JsonResponse({"Error":"PUT method only"})