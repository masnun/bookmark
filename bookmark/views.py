from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from bookmark.forms import BookmarkForm

from bookmark.models import Bookmark
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def home(request):
    form = BookmarkForm()
    if request.method == "POST":
        form = BookmarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    return render_to_response('home.html', {'form': form}, context_instance=RequestContext(request))