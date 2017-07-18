# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils import timezone
from datetime import datetime
import random
import time

def index(request):
	try:
		return render(request, 'gold/index.html')
	except:
		return redirect('/reset')

def processMoney(request):
	request.session['wallet'] = request.session['wallet'] + request.session['gold']
	return redirect('/')

def reset(request):
	request.session['wallet'] = 0
	request.session['activity'] = ['reset',]
	return redirect('/')

def farm(request):
    try:
    	request.session['gold'] = random.randrange(10,21)
    	request.session['time'] = time.strftime('%Y/%m/%d %I:%M %p')
    	request.session['activity'].insert(0,'Earned ' + str(request.session['gold']) + ' golds from the farm! ' + str(request.session['time']))
    	return redirect('/process_money')
    except:
		return redirect('/reset')		

def cave(request):
	try:
	    request.session['gold'] = random.randrange(5,11)
	    request.session['time'] = time.strftime('%Y/%m/%d %I:%M %p')
	    request.session['activity'].insert(0,'Earned ' + str(request.session['gold']) + ' golds from the cave! ' + str(request.session['time']))
	    return redirect('/process_money')
	except:
		return redirect('/reset')	

def house(request):
	try:
	    request.session['gold'] = random.randrange(2,6)
	    request.session['time'] = time.strftime('%Y/%m/%d %I:%M %p')
	    request.session['activity'].insert(0,'Earned ' + str(request.session['gold']) + ' golds from the house! ' + str(request.session['time']))
	    return redirect('/process_money')
	except:
		return redirect('/reset')	

def casino(request):
	try:
	    request.session['gold'] = random.randrange(-50,51)
	    request.session['time'] = time.strftime('%Y/%m/%d %I:%M %p')
	    if request.session['gold'] < int(0):
	        request.session['activity'].insert(0,('Lost ' + str(request.session['gold'] * -1) + ' golds from the casino... ouch! ' + str(request.session['time'])))
	    elif request.session['gold'] >= int(0):
	        request.session['activity'].insert(0,'Earned ' + str(request.session['gold']) + ' golds from the casino! ' + str(request.session['time']))
	    return redirect('/process_money')
	except:
		return redirect('/reset')	

