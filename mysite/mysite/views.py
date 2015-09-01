from django.shortcuts import render_to_response

def editor(request):
	return render_to_response('editor.html', 
		{'title': 'dai',
		 'action': '/api/blogs'
		})