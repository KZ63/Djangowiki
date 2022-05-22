from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request, title):
    return render(request, "encyclopedia/content.html", {
        "entry": util.get_entry(title)
    })


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

    
    

