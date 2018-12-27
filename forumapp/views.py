from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
list_ = [{"name":'good','password':'python'},{'name':'learning','password':'django'}]
def test(request):
    # return HttpResponse("Hello World!!")
    return render(request,'test.html', {'form' : list_})