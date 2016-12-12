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
from django.db import transaction

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

@transaction.non_atomic_requests
def mine_gold(request):
	rocks=[]
	mining=[]
	for line in open('test.json', 'r'):
		rocks.append(json.loads(line))

	for i in range(0, len(rocks)):
		code = rocks[i].get('code')
		sales = rocks[i].get('sales')
		if sales is None:
			sales = 0;
		businessprofits = rocks[i].get('businessprofits')
		if businessprofits is None:
			businessprofits = 0
		continuing = rocks[i].get('continuing')
		if continuing is None:
			continuing = 0
		netincome = rocks[i].get('netincome')
		if netincome is None:
			netincoem = 0
		netincomeruling = rocks[i].get('netincomeruling')
		if netincomeruling is None:
			netincomeruling = 0
		netincomenon = rocks[i].get('netincomenon')
		if netincomenon is None:
			netincomenon = 0
		asset = rocks[i].get('asset')
		if asset is None:
			asset = 0
		liabilities = rocks[i].get('liabilities')
		if liabilities is None:
			liabilities = 0
		totalequities = rocks[i].get('totalequities')
		if totalequities is None:
			totalequities = 0
		totalequitiesruling = rocks[i].get('totalequitiesruling')
		if totalequitiesruling is None:
			totalequitiesruling = 0
		totalequitiesnon = rocks[i].get('totalequitiesnon')
		if totalequitiesnon is None:
			totalequitiesnon = 0
		eqities = rocks[i].get('eqities')
		if eqities is None:
			eqities = 0
		cashbusiness = rocks[i].get('cashbusiness')
		if cashbusiness is None:
			cashbusiness = 0
		cashinvestment = rocks[i].get('cashinvestment')
		if cashinvestment is None:
			cashinvestment = 0
		cashfinance = rocks[i].get('cashfinance')
		if cashfinance is None:
			cashfinance = 0
		capex = rocks[i].get('capex')
		if capex is None:
			capex = 0
		fcf	= rocks[i].get('fcf')
		if fcf is None:
			fcf = 0
		ibl = rocks[i].get('ibl')
		if ibl is None:
			ibl = 0
		roop = rocks[i].get('roop')
		if roop is None:
			roop = 0
		netprofitmargin = rocks[i].get('netprofitmargin')
		if netprofitmargin is None:
			netprofitmargin = 0
		roe = rocks[i].get('roe')
		if roe is None:
			roe = 0
		roa = rocks[i].get('roa')
		if roa is None:
			roa = 0
		debtratio = rocks[i].get('debtratio')
		if debtratio is None:
			debtratio = 0
		err = rocks[i].get('err')
		if err is None:
			err = 0
		eps = rocks[i].get('eps')
		if eps is None:
			eps = 0
		per = rocks[i].get('per')
		if per is None:
			per = 0
		bps = rocks[i].get('bps')
		if bps is None:
			bps = 0
		pbr = rocks[i].get('pbr')
		if pbr is None:
			pbr = 0
		dps = rocks[i].get('dps')
		if dps is None:
			dps = 0
		rcdp = rocks[i].get('rcdp')
		if rcdp is None:
			rcdp = 0
		cdr = rocks[i].get('cdr')
		if cdr is None:
			cdr = 0
		stock = rocks[i].get('stock')
		if stock is None:
			stock = 0
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
			return JsonResponse({})
		else:
			q = QueryDict(samdasu)
			myDict = dict(q)
			
			condition = myDict.get('condition');
			operator = myDict.get('operator');
			value = myDict.get('value');
			
			ore = {}
			for i in range(len(condition)):
				ore.update({'{0}__{1}'.format(condition[i],operator[i]):value[i]})
			
			#ore.update({'{0}__{1}'.format('pbr','gt'):1});
			jeju = Bronze.objects.filter(**ore).order_by('per')[:5]
			
			gamgyul = serializers.serialize('json', jeju)
			print(gamgyul)
			return JsonResponse(gamgyul, safe=False)
	except Exception as err:
		print(err);
