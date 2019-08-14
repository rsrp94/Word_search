from django.shortcuts import render

from django.http import JsonResponse
from app.models import Data

def search(request):
    input_word = request.GET.get('word')
    results = Data.objects.filter(word__contains=input_word).order_by("-count").values("word", "count")
    exact_match = []
    starts_with = []
    remaining_words = []
    for r in results:
        _word = r.get('word')
        if _word == input_word:
            exact_match.append(r)
        elif _word.startswith(input_word):
            starts_with.append(r)
        else:
            remaining_words.append(r)
    
    total_results = exact_match + starts_with + remaining_words

    return JsonResponse({"result": total_results[:25]})
