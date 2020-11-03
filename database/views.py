from django.shortcuts import render
from django.http import JsonResponse


from database.models import user_data
# Create your views here.

def userList(request):
  if request.method == "GET":
    print("get")

  if request.method == 'POST':
    print("post")
  user = user_data.objects.all()
  obj = dict()
  obj['code'] = 200
  obj['message'] = "123456"
  arr = []
  for item in user:
    temp_obj = {}
    temp_obj['user_code'] = item.user_code
    temp_obj['phone'] = item.phone
    temp_obj['user_name'] = item.user_name
    temp_obj['email'] = item.email
    temp_obj['password'] = item.password
    temp_obj['gender'] = item.gender
    temp_obj['is_deleted'] = item.is_deleted
    arr.append(temp_obj)
  obj['data'] = arr
  return JsonResponse(obj)
