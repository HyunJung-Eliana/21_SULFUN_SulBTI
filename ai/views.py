import pandas as pd


from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from analysis.MyAnalysis import MyAnalysis

from config.settings import DATA_DIRS

def home(request):
	return render(request, 'index.html')

def dashboard(request):
	return render(request, 'dashboard.html')

def mix(request):
	my1 = request.POST['my_bti1'];
	my2 = request.POST['my_bti2'];
	you11 = request.POST['you1_bti1'];
	you12 = request.POST['you1_bti2'];
	you21 = request.POST['you2_bti1'];
	you22 = request.POST['you2_bti2'];
	you31 = request.POST['you3_bti1'];
	you32 = request.POST['you3_bti2'];

	result = MyAnalysis().mix(my1,my2,you11,you12,you21,you22,you31,you32);

	return render(request, 'oursulbti.html', result)

def type16(request):
	return render(request, 'type16.html')

def EAOL(request) :
	return render(request, 'EAOL.html')

def IAOL(request) :
	return render(request, 'IAOL.html')

def IAOH(request) :
	return render(request, 'IAOH.html')

def EAOH(request) :
	return render(request, 'EAOH.html')

def ECOL(request) :
	return render(request, 'ECOL.html')

def ICOL(request) :
	return render(request, 'ICOL.html')

def ICOH(request) :
	return render(request, 'ICOH.html')

def ECOH(request) :
	return render(request, 'ECOH.html')

def ECSL(request) :
	return render(request, 'ECSL.html')

def ICSL(request) :
	return render(request, 'ICSL.html')

def ICSH(request) :
	return render(request, 'ICSH.html')

def ECSH(request) :
	return render(request, 'ECSH.html')

def EASL(request) :
	return render(request, 'EASL.html')

def IASL(request) :
	return render(request, 'IASL.html')

def IASH(request) :
	return render(request, 'IASH.html')

def EASH(request) :
	return render(request, 'EASH.html')

def NO(request) :
	return render(request, 'NO.html')

def sns(request) :
	return render(request, 'sns.html')

def isjn(request) :
	return render(request, 'isjn.html')

