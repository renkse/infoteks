# coding=utf-8
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.contrib import messages
import math


# основная вьюшка
def index(request):
    return render(request, 'index.html')


# вьюшка принимающая число через аякс
def prime_factors(request):
    if request.method == 'POST':
        number = request.POST['number']
        if number.isdigit():
            factors = get_prime_factors(int(number))
            result = ' = ' + str(factors).strip('[]').replace(',',' *')
            return HttpResponse(result)
        else:
            return HttpResponse('Input positive number, please')
    else:
        messages.add_message(request, messages.INFO, "Not POST method")
        return redirect(index)


# функция раскладывающая число на простые множители
def get_prime_factors(number):
    if number == 1:
        return [1]
    else:
        result = []
        # берем все простые числа < sqrt(number)
        primes = get_primes(int(math.sqrt(number)))
        for p in primes:
            while (number % p) == 0:
                result.append(p)
                number //= p
        if number > 1:
            result.append(number)
        return result


# функция возвращающая список всех простых чисел до указанного числа (решето Эратосфена)
def get_primes(n):
    primes = [i for i in range(1, n+1)]
    primes[0] = 0
    for i in xrange(0, n):
        if primes[i] != 0:
            for j in xrange(i+primes[i], n, primes[i]):
                primes[j] = 0
    return [x for x in primes if x != 0]
