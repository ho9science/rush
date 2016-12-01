from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .models import Bronze
from .forms import PostForm
from .forms import SearchForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})

def post_list(request):
	#posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
	posts = Post.objects.filter()
	return render(request, 'blog/post_list.html', {'posts': posts})

def view_gold(request):
	form_class = SearchForm(request.POST)
	return render(request, 'blog/gold.html',{'form': form_class})

@csrf_exempt
def post_gold(request):
	samdasu = request.POST.get('samdasu')
	if not samdasu:
		return JsonResponse({'samdasu':'none'})		
	else:
		code = int(samdasu)
		jeju = Bronze.objects.filter(code=code)
		gamgyul = serializers.serialize('json', jeju)
		print(gamgyul)
		return JsonResponse(gamgyul, safe=False)
		
			#return HttpResponse(data, content_type="json", context_instance=RequestContext(request))
	#return render_to_response('blog/gold.html', "{'samdasu': 'nothing'}")