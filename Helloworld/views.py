from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # response=HttpResponse("UPPAL STORE WELCOMES YOU ! !")
    #Dynamic variables
    developed_by="dev uppal"
    mentors=[
        "monu bhaiya",
        "sashi bushan uncle",
        "anju uppal",
        "Ayush kumar",
    ]
    context={
        "developer":developed_by,
        "mentors":mentors
    }
    response = render(request,'Helloworld/index.html',context)
    return response
