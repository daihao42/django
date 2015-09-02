from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import Blog

def editor(request):
	if request.method == 'POST' :
		if 'content' in request.POST:
			blog=Blog(title=request.POST['title'],content=request.POST['content'])
			blog.save()
			print("OK!")
		else:
			print('none')
	return render_to_response('editor.html', 
		{'title': '编辑日志'
		},context_instance=RequestContext(request))

def blog(request):
	return render_to_response('blog.html', 
		{'blogs': Blog.objects.all()
		})

def signin(request):
	return render_to_response('signin.html')

