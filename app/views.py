from django.shortcuts import render # type: ignore
from django.http.response import HttpResponse
from django.http.request import HttpRequest

# Create your views here.
def near_hundred(request, n: int) -> bool:
    return HttpResponse(abs(n - 100) <= 10 or abs(n - 200) <= 10)

def string_splosion(request, s: str) -> str:
    result = ""
    for i in range(len(s)):
        result += s[:i+1]
    return HttpResponse(result)

def cat_dog(request ,s: str) -> bool:
    return HttpResponse(s.count('cat') == s.count('dog'))

def lone_sum(request, a: int, b: int, c:int) -> int:
    total = 0
    if a != b and a != c:
        total += a
    if b != a and b != c:
        total += b
    if c != a and c != b:
        total += c
    return HttpResponse(total)