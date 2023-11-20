from django.shortcuts import render
from django.http import HttpResponse

def calculator(request):
    return render(request, 'calculator/calculator.html')

def calculate(request):
    if request.method == 'POST':
        expression = request.POST.get('expression', '')
        try:
            result = eval(expression)
            return render(request, 'calculator/calculator.html', {'result': result, 'expression': expression})
        except Exception as e:
            error_message = f"Error: {e}"
            return render(request, 'calculator/calculator.html', {'error_message': error_message, 'expression': expression})
    else:
        return HttpResponse("Method not allowed")
