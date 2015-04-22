from django.shortcuts import render
from django.http import HttpResponse
from hello.models import Post

# Create your views here.
def index(request):
	#output = ""
	if(request.POST != Post(text=request.POST["text"])):
		test = Post(text=request.POST["text"])
		test.save()
	else:
		return HttpResponse("Error Text")
	postobj = Post.objects.all()
	context = {'postobj':postobj}
	return render(request,'index.html',context)

def myfunction(request):
	return HttpResponse("HelloWorld myfunction")

