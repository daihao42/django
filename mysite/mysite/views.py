#-*-coding:utf-8-*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import Blog
import uuid

def editor(request):
	if request.method == 'POST' :
		if 'content' in request.POST:
			blog=Blog(title=request.POST['title'].encode('utf8'),content=request.POST['content'].encode('utf8'))
			blog.save()
	return render_to_response('editor.html', 
		{'title': '编辑日志'
		},context_instance=RequestContext(request))

def blog(request):
	return render_to_response('blog.html', 
		{'blogs': Blog.objects.all()
		})

def signin(request):
	return render_to_response('signin.html')

def register(request):
	return render_to_response('register.html',
		{'img_uuid': uuid.uuid1()})


#####defalut image of HD########
def head_img_upload(request,offset):
	if request.method == 'POST' :
		file=request.FILES['file']
		file.file.seek(0)
		path=os.path.abspath('.')
		path=os.path.join(path,"static")
		path=os.path.join(path,"HeadImg")
		path=os.path.join(path,"%s.jpg" % offset)
		with open(path,"wb") as jpg:
			for i in file.file:
				jpg.write(i)


