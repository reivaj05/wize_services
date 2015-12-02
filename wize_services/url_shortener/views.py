from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, RedirectView
from .forms import UrlConvertForm
from common.mixins import FormMessagesMixin
from .models import UrlShort
from config.settings.keys import KEYS
import bitly_api
# Create your views here.


class UrlConvertView(FormMessagesMixin, CreateView):
    template_name = 'url_shortener/convert_url.html'
    form_class = UrlConvertForm
    context_object_name = 'long_url'
    success_message = 'Short Url successfully created'
    error_message = 'There was an error trying to create the url'
    # success_url = '/thanks/'

    def get_success_url(self):
        return reverse('url_shortener:url_list')

    def post(self, request, *args, **kwargs):
        super(UrlConvertView, self).post(request, *args, **kwargs)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(form=form)
        long_url = str(context['long_url'])
        b = bitly_api.Connection(KEYS['BITLY_USER'], KEYS['BITLY_SHORTENER_KEY'])
        response = b.shorten('http://www.pythonforbeginners.com/bitly/bitly-shortener-with-python')
        short_url = response['url']
        list(UrlShort.objects.all())[-1].delete()
        UrlShort.objects.create(long_url=long_url, short_url=short_url)
        return redirect(self.get_success_url())


class UrlListView(ListView):
    """
        View to display a list of the urls converted
    """
    template_name = 'url_shortener/url_list.html'
    context_object_name = 'url_list'
    model = UrlShort

    def get_queryset(self):
        return UrlShort.objects.all()

class UrlRedirectShortUrl(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        pass
