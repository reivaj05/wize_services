from django.core.urlresolvers import reverse
from django.views.generic import CreateView, FormView, ListView
from .forms import UrlConvertForm
from common.mixins import FormMessagesMixin
from .models import UrlShort
# Create your views here.


class UrlConvertView(FormMessagesMixin, FormView):
    template_name = 'url_shortener/convert_url.html'
    form_class = UrlConvertForm
    success_message = 'Short Url successfully created'
    error_message = 'There was an error trying to create the url'
    # success_url = '/thanks/'

    def get_success_url(self):
        return reverse('url_shortener:url_list')


class UrlListView(ListView):
    """
        View to display a list of the urls converted
    """
    template_name = 'url_shortener/url_list.html'
    context_object_name = 'url_list'
    model = UrlShort

    def get_queryset(self):
        return UrlShort.objects.all()
