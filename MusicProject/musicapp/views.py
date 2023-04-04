from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
request_json = requests.get("https://itunes.apple.com/search?term=Alex&media=music&entity=album",verify=False)
requestfiledata = request_json.json()
def basepage(request):
    return render(request,'base.html')

def MusicTotorial(request):    
    record_filter = lambda x:x if request.GET['artistname'] in x['artistName'] else None
    list_of_data = list(filter(record_filter,requestfiledata['results']))
    print(list_of_data)
    return render(request,'home.html',{"musicRecords":list_of_data})



