from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
from django.template import loader
from .models import Question
import requests

def rest(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('rest/restindex.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def forecast(request):
    print()
    print("forecast entered")
    API_Key = 'cd8b51d756e628a1c5453e7710378772'
    city = "Tokyo,jp"
    if request.POST['city']:
        city = request.POST['city']
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    query = {
        'units': 'metric',
        'q': city,
        'cnt': '30',
        'appid': API_Key
    }
    r = requests.get(url, params=query)
    #print("response", r.json())
    #print("Weather forecast in Tokyo at UTC(needs +9h): ")
    result1 = []
    result2 = []
    result3 = []
    result4 = []
    for x in range(r.json()['cnt']):
        #print("x: ", x)
        days = r.json()['list'][x]['dt_txt'].split(' ')
        day = days[0].split('-')
        year = day[0]
        day2 = day[1]
        day3 = day[2]
        times = days[1].split(':')
        time = times[0]
        result1.append(str(day2) + '月' + str(day3) + '日')
        result2.append(str(time) + '時頃')
        result3.append("温度は " + str(r.json()['list'][x]['main']['temp']) + '度')
        if r.json()['list'][x]['weather'][0]['main'] == 'Clear':
            result4.append('晴れ')
        elif r.json()['list'][x]['weather'][0]['main'] == 'Clouds':
            result4.append('曇り')
        else:
            result4.append('雨')

        #print(r.json()['list'][x]['dt_txt'],
        #"temp: ", r.json()['list'][x]['main']['temp'],
        #"weather: ", r.json()['list'][x]['weather'][0]['main'], "/", r.json()['list'][x]['weather'][0]['description'])

    mapped_num = map(str, result1) #格納される数値を文字列にする
    result_string = ' '.join(mapped_num)
    #print("result_string", result_string)
    #print("city", city)
    #print(mapped_num)
    
    if city == "Hokkaido,jp":
        citys = "北海道"
    elif city == "Osaka,jp":
        citys = "大阪府"
    elif city == "Tokyo,jp":
        citys = "東京都"
    print("forecast ended")
    print()
    return render(request, 'rest/forecast.html', {'city': citys, 'year': year, 'result1': result1, 'result2': result2, 'result3': result3, 'result4': result4,})