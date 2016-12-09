from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .models import Bronze
from .forms import PostForm
from .forms import SearchForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import QueryDict
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
		jeju = Bronze.objects.filter(code=samdasu)
		gamgyul = serializers.serialize('json', jeju)
		print(gamgyul)
		return JsonResponse(gamgyul, safe=False)
		
def mine_gold(request):
	rocks=[]
	mining=[]
	for line in open('test.json', 'r'):
		rocks.append(json.loads(line))

	for i in range(0, len(rocks)):
		code = rocks[i].get('code')
		sales = rocks[i].get('sales')
		businessprofits = rocks[i].get('businessprofits')
		continuing = rocks[i].get('continuing')
		netincome = rocks[i].get('netincome')
		netincomeruling = rocks[i].get('netincomeruling')
		netincomenon = rocks[i].get('netincomenon')
		asset = rocks[i].get('asset')
		liabilities = rocks[i].get('liabilities')
		totalequities = rocks[i].get('totalequities')
		totalequitiesruling = rocks[i].get('totalequitiesruling')
		totalequitiesnon = rocks[i].get('totalequitiesnon')
		eqities = rocks[i].get('eqities')
		cashbusiness = rocks[i].get('cashbusiness')
		cashinvestment = rocks[i].get('cashinvestment')
		cashfinance = rocks[i].get('cashfinance')
		capex = rocks[i].get('capex')
		fcf	= rocks[i].get('fcf')
		ibl = rocks[i].get('ibl')
		roop = rocks[i].get('roop')
		netprofitmargin = rocks[i].get('netprofitmargin')
		roe = rocks[i].get('roe')
		roa = rocks[i].get('roa')
		debtratio = rocks[i].get('debtratio')
		err = rocks[i].get('err')
		eps = rocks[i].get('eps')
		per = rocks[i].get('per')
		bps = rocks[i].get('bps')
		pbr = rocks[i].get('pbr')
		dps = rocks[i].get('dps')
		rcdp = rocks[i].get('rcdp')
		cdr = rocks[i].get('cdr')
		stock = rocks[i].get('stock')
		mining.append(Bronze(code=code,sales=sales,businessprofits = businessprofits, continuing = continuing, netincome = netincome, netincomeruling = netincomeruling, 
							netincomenon = netincomenon, asset = asset, liabilities = liabilities, totalequities = totalequities, totalequitiesruling = totalequitiesruling, 
							totalequitiesnon = totalequitiesnon, eqities = eqities, cashbusiness = cashbusiness, cashinvestment = cashinvestment,
							cashfinance = cashfinance, capex = capex, fcf = fcf, ibl = ibl, roop = roop, netprofitmargin = netprofitmargin, roe = roe, 
							roa = roa, debtratio = debtratio, err = err, eps = eps, per = per, bps = bps, pbr = pbr, dps = dps, rcdp = rcdp, cdr = cdr,stock = stock))
	#alist = [Entry(headline=val) for val in values]
	Bronze.objects.bulk_create(mining)
	return render(request, 'blog/gold.html',{'form': "success"})

def wash_gold(request):
	return render(request, 'blog/washingold.html',{})

@csrf_exempt
def alluvialmining(request):
	#samdasu = request.POST.get('samdasu')
	#value = request.POST.get('value');
	try:
		samdasu = request.body;
		print(samdasu)
		if not samdasu:
			return JsonResponse({'samdasu':'none'})
		else:
			q = QueryDict(samdasu)
			myDict = dict(q)
			
			ssamba = myDict.get('condition');
			ssamja = myDict.get('operator');
			value = myDict.get('value');
			
			ore = {}
			ore.update({'{0}__{1}'.format(ssamba[0],ssamja[0]):value[0]})
			
			#ore.update({'{0}__{1}'.format('pbr','gt'):1});
			jeju = Bronze.objects.filter(**ore).order_by('per')[:5]
			
			gamgyul = serializers.serialize('json', jeju)
			print(gamgyul)
			return JsonResponse(gamgyul, safe=False)
	except Exception as err:
		print(err);
