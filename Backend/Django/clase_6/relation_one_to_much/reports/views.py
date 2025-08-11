from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article   

# Create your views here.

def create(request):
    # Logic to create a new article
    rep = Reporter(name="John Doe", email="john@example.com")
    rep.save()

    art = Article(title="Sample Article", content="This is a sample article.", reporter=rep)
    art.save()
    art2 = Article(title="Sample Article 2", content="This is a sample article 2.", reporter=rep)
    art2.save()
    art3 = Article(title="Sample Article 3", content="This is a sample article 3.", reporter=rep)
    art3.save()

    result = art.reporter.email
    result2 = rep.article_set.all()
    return HttpResponse(f"Create a new article. Reporter email: {result}. Articles: {list(result2)}")
