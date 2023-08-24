from django.shortcuts import render
from django.http import request,HttpResponse


# Create your views here.
def home(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        url = f'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=2ca69a6d25d980dc573ffce7c467b9fe'
        response = requests.get(url)
        data = dict(response.json())
        return render(request,'weather.html',{
            'city':data['name'],
            'main':data['weather'][0]['main'],
            'temp': data['main']['temp'],
            'max':data['main']['temp_max'],
            'min':data['main']['temp_min'],
            'feels':data['main']['feels_like'],
            })
    return render(request,'index.html',{})