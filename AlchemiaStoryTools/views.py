from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    if request.method == 'POST':
        parameters = {
            'atkmatk': request.POST.get('atkmatk'),
            'skill': request.POST.get('skill'),
            'ele_atk': request.POST.get('ele_atk'),
            'enemy_def': request.POST.get('enemy_def'),
            'cdmg': request.POST.get('cdmg'),
            'df': request.POST.get('df'),
            'atkUp': request.POST.get('atkUp'),
            'hits': request.POST.get('hits')
        }
        
        for parameter, value in parameters.items():
            if value == '' and parameter == 'skill':
                parameters[parameter] = 100.0
            elif value == '' and parameter == 'hits':
                parameters[parameter] = 1.0 
            elif value == '':
                parameters[parameter] = 0.0
  
            else:
                parameters[parameter] = float(value)
        
        default_cdmg = 1.2
        default_ele = 1.2
        

        if request.POST.get('crit') == 'false':
            default_cdmg = 1
            parameters['cdmg'] = 0.0
            
        if request.POST.get('eleWeak') == 'false':
            default_ele = 1
            parameters['ele_atk'] = 0.0
              
        result = (
            ((parameters['atkmatk'] * (1 + parameters['atkUp']/100)) * (parameters['skill']/100)) 
            * (default_ele + (parameters['ele_atk']*0.005)) - parameters['enemy_def']
            ) * (default_cdmg + (parameters['cdmg']/100)) * (1 + (parameters['df']/100))

        result = result * parameters['hits']
        # import pandas as pd
        # print(parameters)
        parameters['damage'] = result
        
        # parameters = pd.DataFrame(parameters, index=[1])
        # parameters.to_csv('data/damage.csv', index=False)
        return JsonResponse({
            'success': True,
            'message': result, 
        })
    return render(request, 'home/index.html')