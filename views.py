from django.shortcuts import render,HttpResponse
# Create your views here.
def loginpage(request):
    #return HttpResponse('Login Success')
    return render(request,'login.html',{})
def verifypage(request):
    #return HttpResponse('Verifying')
    if request.method=='POST':
        u=request.POST.get('uname')
        p=request.POST.get('pw')
        from .models import AccountModel as AM
        try:
            AM.objects.get(user=u)
            return HttpResponse('LOGIN SUCCESS')
        except:
            a=AM()
            a.user=u
            a.pwd=p
            a.save()
            return HttpResponse('Account created')

