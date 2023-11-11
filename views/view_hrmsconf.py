from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
# from population.models import Population,DetailFamily,Family,Religion,Profession,Citizen,Aldeia,Village,User,Migration,Death,Migrationout,Temporary,ChangeFamily
# from population.utils import getnewidp,getnewidf
# from population.forms import Family_form,Family_form,FamilyPosition,Population_form,DetailFamily_form,CustumDetailFamily_form,Death_form,Migration_form,Migrationout_form,Changefamily_form
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone

# from custom.utils import getnewid, getjustnewid, hash_md5, getlastid
from django.db.models import Count
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Q
from datetime import date
from django.http import JsonResponse

from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from rekrutamentu.forms import FileUploadForm
from purchase_request.models import *
from custom.models import RequestSet, Department,Position

from settingapps.utils import  decrypt_id, encrypt_id
from django.core.paginator import Paginator

from django.utils import translation
from django.utils import timezone
from datetime import datetime

from django.contrib.auth.models import User, Group

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from purchase_request.forms import RequestOrderForm, ItemRequestForm
from employee.models import EmployeeUser
import logging
from django.core.exceptions import ObjectDoesNotExist


# from twilio.rest import Client

def hrmsconf(request):





    # account_sid = 'AC5b66b01f15d57ca88b1eddb02ca3d622'
    # auth_token = 'ed8ba42ac0d468895accd11f957ab805'
    # client = Client(account_sid, auth_token)

    # message = client.messages.create(
    # from_='whatsapp:+14155238886',
    # body='Your Twilio code is 1238432',
    # to='whatsapp:+6282339519417'
    # )


    
    # print(message.sid)

    # dadospr = RequestOrder.objects.all().order_by('-id')
    context = {

        "pajina_hrms_conf" : "active",
            }
    return render(request, 'hrms_conf/hrmsconf.html',context)



def hrmsconftab(request,tab):
    # dadospr = RequestOrder.objects.all().order_by('-id')
    context = {

        "pajina_hrms_conf" : "active",
        "tab_"+str(tab): "active",
        "tab" : tab,
            }
    return render(request, 'hrms_conf/hrmsconf.html',context)



def hrmsconfrequestset(request,tab,level):
    # dadospr = RequestOrder.objects.all().order_by('-id')
    context = {

        "pajina_hrms_conf" : "active",
        "tab" : tab,
        "level" : level,
            }
    return render(request, 'hrms_conf/hrmsconfrequestset.html',context)






def generatelevelandgroup(request):
    departement = Department.objects.all()
    position = Position.objects.all()
    for pos in position.iterator() :
        for dep in departement.iterator() :
            strap_position = pos.name.replace(" ", "_")
            strap_department = dep.name.replace(" ", "_")
            groupname = str(strap_position)+str("_")+str(strap_department)
            print(groupname)
            new_group, created = Group.objects.get_or_create(name=groupname)
            new_group.save()


    for pos in position.iterator() :
            strap_position = pos.name.replace(" ", "_")
            groupname = str("Executive")+str("_")+str(strap_position)
            print(groupname)
            new_group, created = Group.objects.get_or_create(name=groupname)
            new_group.save()

    return redirect('hrmsconf:hrmsconf')




