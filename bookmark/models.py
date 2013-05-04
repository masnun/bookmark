from django.db import models


class Bookmark(models.Model):
    slug = models.CharField('Slug', max_length=255, unique=True, blank=False)
    long_url = models.TextField('URL', blank=False)
    title = models.CharField(max_length=255, blank=False)
    note = models.TextField('Note', blank=True)

    def __unicode__(self):
        return self.title


