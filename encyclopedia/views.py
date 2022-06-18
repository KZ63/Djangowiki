from webbrowser import get
from django.shortcuts import render, redirect
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request, title):
    return render(request, "encyclopedia/content.html", {
        "title": title,
        "entry": markdown2.markdown(util.get_entry(title))
    })


def newPage(request):
    if request.method == 'GET':
        return render(request, "encyclopedia/newPage.html")


def search(request):
    search_word = request.GET['q']
    word = util.get_entry(search_word)
    print(type(word))
    if not word:
        entries_list = util.list_entries()
        target_entries = []
        for i in range(0, len(entries_list)):
            if search_word in entries_list[i]:
                target_entries.append(entries_list[i])
        return render(request, "encyclopedia/searchresult.html", {
            "entries": target_entries
        })
    else:
        return render(request, "encyclopedia/content.html", {
            "entry": word
        })


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    word = util.get_entry(title)
    if not word:
        try:
            util.save_entry(title, content);
            return render(request, "encyclopedia/content.html", {
                "entry": util.get_entry(title)
            })
        except:
            return render(request, "encyclopedia/error.html", {
                "errorMessage": "undefiend error"
            })
    else:
        return render(request, "encyclopedia/error.html", {
            "errorMessage": "This title is already exists."
        })


def edit(request, title):
    content = util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": content
    })