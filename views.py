from django.shortcuts import render, HttpResponse
import requests
import json

def index(request):
    return HttpResponse('Hello world')

def poo(request):
    return HttpResponse('Poo')

def profile(request):
    parsedData = []
    if request.method == 'POST':
        username = request.POST.get('user')
        r = requests.get('https://api.github.com/users/' + username)
        jsonList = []
        # r = requests.get('https://api.github.com/users/rigondeaux')
        jsonList.append(json.loads(r.content))
        userData = {}
        for data in jsonList:
            userData['login'] = data['login']
            userData['blog'] = data['blog']
            userData['email'] = data['email']
            userData['public_gists'] = data['public_gists']
            userData['public_repos'] = data['public_repos']
            userData['avatar_url'] = data['avatar_url']
            userData['followers'] = data['followers']
            userData['following'] = data['following']
        parsedData.append(userData)
    # combines a template with a context dictionary and
    # returns a HttpResponse object with that rendered text
    return render(request, 'gitget/profile.html', {'data': parsedData})
    '''
    parsedData is a list with the userData dictionary inside
    eg,
    [{'login' : 'rigondeaux'...}]}
    thus, { 'data' : parsedData } is a dictionary with
    one key value pair, where the value is the parsedData list
    containing the userData dictionary
    eg,
    {'data': [{'login' : 'rigondeaux'...}]}
    '''
