from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("Home page ")
    friends=[
        'Arghya',
        'Aman',
        'Aditya'
        
    ]
  
    return JsonResponse(friends,safe=False)