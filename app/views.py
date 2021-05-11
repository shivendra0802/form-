from django.shortcuts import render
from django.http import HttpResponse
import re

# Create your views here.
def index(request):
    return render(request, 'app/index.html')


# count = digits = special = alphabets = 0

# def removepunc(request):
#     count = digits = special =  0
#     alphabets = 0
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     spchar = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
#     for i in range(0, len(djtext)):
#         if(djtext[i] != ''):
#             count = count + 1
#         elif(djtext[i].isdigit()):
#             digits = digits + 1
#         elif(djtext[i].isalpha()):
#             alphabates = alphabates + 1    
#         else:
#             spchar = spchar + 1
#             print("String contains Special Characters.")
#     print(djtext.count)
#     print(len(djtext.split()))
#     print(djtext.isalpha())
#     print(djtext.isnumeric())
#     print(djtext.isalnum())
#     return HttpResponse("remove punc")


def check(request):
    djtext = request.GET.get('text', 'default')
    d=l=m=0
    for c in djtext:
        if c.isdigit():
            d=d+1
        elif c.isalpha():
            l=l+1    
        else:
            m=m+1
    print(djtext)        
    print(len(djtext))
    print("Letters", l)
    print("Digits", d)
    print("specialChar", m)
    return HttpResponse("check")



