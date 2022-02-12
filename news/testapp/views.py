from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'testapp/index.html')

def moviesinfo(request):
    head_msg='Latest Movie information'
    msg1='Sonali is recovering'
    msg2='salman getting married'
    msg3='narener modi in a bollywood movie'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'testapp/news.html',context=my_dict)

def sportsinfo(request):
    head_msg='Latest Sports information'
    msg1='kohli century'
    msg2='Msd is coming back soon'
    msg3='World cup 2022'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'testapp/news.html',context=my_dict)

def politicsinfo(request):
    head_msg='Latest Politics information'
    msg1='Acche din aagye'
    msg2='Rahul gandhi'
    msg3='narener modi in a bollywood movie'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'testapp/news.html',context=my_dict)