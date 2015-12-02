from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class UrlShort(models.Model):

    long_url = models.URLField(
        _('Long url'),
        max_length=200,
        help_text=_('Insert Url to convert')
    )
    short_url = models.CharField(
        _('Short url'),
        max_length=200,
        help_text=_('Insert Url to convert')
    )

    def __unicode__(self):
        return '{long_url} {short_url}'.format(
            long_url=self.long_url,
            short_url=self.short_url)
