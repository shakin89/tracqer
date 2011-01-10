
#from django.conf.urls.defaults import *
from django.conf.urls.defaults import patterns
from django.http import Http404, HttpResponse
from django.views.generic import list_detail, create_update
from trACQer.rda.models import RichiestaDiAcquisto
from datetime import datetime

def rda_per_year(request, anno):
    if request.method == "POST":
        anno = request.POST.get('scelta_anno', datetime.now().year)        
    rda = RichiestaDiAcquisto.objects.filter(anno__exact=anno)[:1]
    if not rda:
        raise Http404
    anniRda = RichiestaDiAcquisto.objects.distinct().values('anno')
    anni_rda = []
    for a in anniRda:
        anni_rda.append(a.values()[0])
    anno_corrente = datetime.now().year
    return list_detail.object_list(request, 
            queryset = RichiestaDiAcquisto.objects.filter(anno__exact=anno), 
            paginate_by = 100, 
            template_name = 'rda/list.html',
            template_object_name = 'rda',
            extra_context = {'anno': anno, 
                             'anni_rda': anni_rda,
                             'anno_corrente': anno_corrente}
            )

rda_create = {'model':RichiestaDiAcquisto,
              'template_name':'rda/create.html',
              'post_save_redirect':'/rda/'
              }

rda_update = {'model':RichiestaDiAcquisto,
              'template_name':'rda/edit.html',
              'post_save_redirect':'/rda/'}
 
rda_detail = {'queryset': RichiestaDiAcquisto.objects.all(), 
              'template_name': 'rda/detail.html',
              'template_object_name' : 'rda'}

rda_delete ={'model': RichiestaDiAcquisto,
             'post_delete_redirect': '/rda/',
             'template_name': 'rda/delete.html',
             'template_object_name': 'rda'}

urlpatterns = patterns('',
        (r'^$','trACQer.rda.views.index'),
        (r'^list/(?P<anno>\d{4})/$', rda_per_year),
        (r'^create/$', create_update.create_object, rda_create),
        (r'^edit/$', 'trACQer.rda.views.edit'),
        (r'^search/$', 'trACQer.rda.views.search'),
        (r'^delete/$', 'trACQer.rda.views.delete'),
        (r'^(?P<object_id>\d+)/$', list_detail.object_detail, rda_detail),
        (r'^(?P<object_id>\d+)/edit/$', create_update.update_object, rda_update),
        (r'^(?P<object_id>\d+)/delete/$', create_update.delete_object, rda_delete),
        )
