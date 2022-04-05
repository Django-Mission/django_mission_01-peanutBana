from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def calculator(request):
    #return HttpResponse("계산기 기능 구현")
    #print(f'request = {request}')
    #print(f'request type = {type(request)}')
    #print(f'request.__dict__ = {request.__dict__}')

    #1. 데이터 확인
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operator = request.GET.get('operator')
    
    #2. 계산
    if operator == '+':
        result = int(num1) + int(num2)
    elif operator == '-':
        result = int(num1) + int(num2)
    elif operator == '*':
        result = int(num1) * int(num2)
    elif operator == '/':
        result = int(num1) / int(num2)
    else:
        result = 0

    #3. 응답
    return render(request, 'calculator.html', {'result' : result})

def lotto(request):
    # 1~45의 정수가 담긴 리스트 생성
    num = list(range(1,46))

    #num리스트 중에 6개의 숫자 랜덤으로 뽑기
    lotto_num = random.sample(num,6)

    #응답
    return render(request, 'lotto.html',{'lotto_num' : lotto_num})


def lotto_cnt(request):
    num = list(range(1,46))
    res = []
    game_cnt = request.GET.get('game_cnt')
    for i in len(game_cnt):
        lotto_num = random.sample(num,6)
        res.apppend(lotto_num)
    return render(request, 'lotto_output.html',{'res': res})

