from django.shortcuts import render_to_response,render,redirect
from english.models import article,choice,User,performance,question
import json
from django.db.models import Count
from django.http import HttpResponse,HttpResponseRedirect
from english.forms.register import RegistrationForm
from english.forms.authenticate import AuthenticationForm
from django.template import RequestContext
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
import ast
import math




# Create your views here.
def show_article_list(request):
	if not request.user.is_authenticated():
		return render_to_response("login.html")
	else:
		listing=list(article.objects.values('id','image','heading','level','summary'))
		listing=json.dumps(listing)
		return render_to_response("list.html",{'list':listing})

def open_article(request,articleid):
	if not request.user.is_authenticated():
		return render_to_response("login.html")
	else:
		listing=list(article.objects.values('image','heading','level','summary','content').filter(id=articleid))
		listing=json.dumps(listing)
		question_list=list(choice.objects.filter(question_id__article_id__id=articleid).values('question_id__id','question_id__question_text','choice1','choice2','choice3','choice4'))
		question_list=json.dumps(question_list)
		attempted_list=list(performance.objects.filter(question_id2__article_id__id=articleid,user_id__id=request.user.id).values('question_id2__id'))
		attempted_list=json.dumps(attempted_list)
		return render_to_response("test.html",{'list':listing,'question':question_list,'attempt':attempted_list})

def load_more(request,id):
	newarticle_list=list(article.objects.values('id','heading','level','summary').filter(id__in=[id,id-2,id-3,id-4,id-5,id-6]))
	newarticle_list=json.dumps(newarticle_list)
	return HttpResponse(newarticle_list)
@csrf_exempt
def response(request):
	current_user=request.user
	if request.method=='POST':
		newdict=json.loads(request.body)
		newdict=json.dumps(newdict)
		newdict=ast.literal_eval(newdict)
		
		question_id=str(newdict['question_id'])
		selected_choice=str(newdict['selected_choice'])
		
		
		right_choice=list(choice.objects.filter(question_id__id=question_id).values('right_choice'))
		right_choice=json.dumps(right_choice)
		right_choice=ast.literal_eval(right_choice)

		
		if right_choice[0]['right_choice']!=selected_choice:
			key=0
		else:
			key=1
	p=performance.objects.create(question_id2_id=question_id,user_id=current_user,response=selected_choice,key=key)
		
	return HttpResponse(right_choice[0]['right_choice'])

def performance_stats(request):
	if not request.user.is_authenticated():
		return render_to_response("login.html")
	else:
		
		current_user=request.user.id
		grammar_correct=performance.objects.filter(user_id__id=current_user,question_id2__genre=2,key=1).count()
		grammar_total=performance.objects.filter(user_id__id=current_user,question_id2__genre=2).count()
		grammar_percentage=0.0
		grammar_percentage=(float(grammar_correct) /float(grammar_total))*100
		grammar_list={'num_correct':grammar_correct,'num_total':grammar_total,'percentage':grammar_percentage}
		grammar_list=json.dumps(grammar_list)
		vocab_correct=performance.objects.filter(user_id__id=current_user,question_id2__genre=1,key=1).count()
		vocab_total=performance.objects.filter(user_id__id=current_user,question_id2__genre=1).count()
		vocab_percentage=0.0
		if vocab_total==0:
			vocab_total=2
		vocab_percentage=(float(vocab_correct) /float(vocab_total))*100
		vocab_list={'num_correct':vocab_correct,'num_total':vocab_total,'percentage':vocab_percentage}
		vocab_list=json.dumps(vocab_list)
		comp_correct=performance.objects.filter(user_id__id=current_user,question_id2__genre=3,key=1).count()
		comp_total=performance.objects.filter(user_id__id=current_user,question_id2__genre=3).count()
		comp_percentage=0.0
		if comp_total==0:
			comp_total=2
		comp_percentage=(float(comp_correct) /float(comp_total))*100
		comp_list={'num_correct':comp_correct,'num_total':comp_total,'percentage':comp_percentage}
		comp_list=json.dumps(comp_list)
		
		
		
		return render_to_response('profile.html',{'grammar':grammar_list,'vocab':vocab_list,'comp':comp_list})






@csrf_exempt
def register(request):
	if request.method == 'POST':
		
		#user = User.objects.create_user(password=request.GET.get('password',''),email=request.GET.get('email',''))
		selectedpackages = json.loads(request.body)
		new_json = json.dumps(selectedpackages)
		#return HttpResponse(str(new_json))
		newdict = ast.literal_eval(new_json)
		#kk = selectedpackages.account
		#return HttpResponse(str(newdict['email']))

		user = User.objects.create_user(password=str(newdict['password']),email=str(newdict['email']))
		return HttpResponse(str("ll"))
		#status=2

		#return render_to_response('register.html',{'status':status})

		

		
		#user = User.objects.create_user(password=request.GET.get('password',''),email=request.GET.get('email',''))
	else:
		next=str('http://localhost:8000/login/')
		return render_to_response('register.html',{'next':next})
		



def login(request):
	return render_to_response('login.html')

def register2(request):
	return render_to_response("register.html")

# Create your views here.
