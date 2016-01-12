from django.shortcuts import render, render_to_response


# Create your views here.
from django.template.context import RequestContext
from timeline.models import Tweet


def tweets(request):
    tweets = Tweet.objects.all()
    return render_to_response('tweets.html',
                              {'tweets': tweets},
                              context_instance=RequestContext(request)
                              )
