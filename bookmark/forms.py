from django.forms import ModelForm
from bookmark.models import Bookmark


class BookmarkForm(ModelForm):
    class Meta:
        model = Bookmark
