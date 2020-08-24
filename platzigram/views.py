""" Platzigram URLS module """
#Django
from django.http import HttpResponse, JsonResponse
# utilities
from datetime import datetime
import json


def hello_world(request):
    """ Return a Hello"""
    now = datetime.now().strftime("%b %dth, %Y - %H:%M hrs")
    return HttpResponse(f"Oh, hi! Current Server Time is {now}")


def sort_num(request):
    """ Sort some numbers from Request """
    num_str = request.GET["numbers"]
    num_lst = [int(n) for n in num_str.split(",")]
    data = {
        "num": sorted(num_lst),
        "status": "ok",
        "msg": "Integer soarted Succesfully!"
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


def guten_tag(request, name, jahre_alt):
    """ Returns Good Morging in German """
    if (jahre_alt < 18):
        msg = f"Entschuldigung {name}! dass du sehr jung bist"
    else:
        msg = f"Guten Tag {name}!"

    data_res = {"status": "OK", "msg": msg}

    return HttpResponse(json.dumps(data_res), content_type="application/json")
