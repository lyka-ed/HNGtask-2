from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@csrf_exempt
def point_list(request):
  header = {"Access-Control-Allow-Origin":"*"}
  data = {
    "slackUsername":"lykaokpos",
    "backend":True,
    "age":24,
    "bio":"I love food.",
    
  }
  return JsonResponse(data, safe=False, headers=header)

@api_view(['POST'])
def arth_operation(request):
    header = {"Access-Control-Allow-Origin":"*"}
    result = 0
    add_array = ['add', 'addition', 'added', 'sum', 'sumation', 'adding']
    subtract_array = ['minus', 'subtraction','difference','subtracting', 'subtract']
    multi_array = ['multi', 'multiplication', 'multiply', 'multiplying', 'product',]
    
    x = int(request.data["x"])
    y = int(request.data["y"])
    operation = str(request.data["operation_type"])
    split_str = operation.split(" ")
    
    
    for items in split_str:
      if items.lower() in add_array:
        result = x+y
        operation = "addition"
        break
      elif items.lower() in subtract_array:
        result = x-y
        operation = "subtraction"
        break
      elif items.lower() in multi_array:
        result = x*y
        operation = "Multiplication"
        break
      else:
        operation = "invalid operator"
       
    new_data = {
        "slackUsername":"lykaokpos",
        "x":x,
        "y":y,
        "operation_type": operation,
        "result":result,
    }
    return Response(new_data, status=status.HTTP_200_OK, headers=header)





