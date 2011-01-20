'''
Created on 17/dic/2010

@author: fabrizio
'''

from django.conf.urls.defaults import patterns
from django.http import HttpResponseNotFound
from django.views.generic import create_update, list_detail
from django.contrib.auth.decorators import login_required

from trACQer.note.models import Nota
from trACQer.note.forms import NoteCreateForm
from trACQer.note.views import index, edit, delete, search, aggiungi, collega, creaDocumento
import datetime

def note_per_anno( request, anno ):
    if request.method == 'POST':
        anno = int( request.POST.get( 'scelta_anno', datetime.datetime.now().year ) )
    note = Nota.objects.filter( anno__exact=anno ).values( 'anno' ).distinct()
    if not note:
        return HttpResponseNotFound( 'Oggetto non trovato' )
    anniNote = Nota.objects.distinct().values( 'anno' )
    anni_note = []
    for a in anniNote:
        anni_note.append( a.values()[0] )
    anno_corrente = datetime.datetime.now().year
    return list_detail.object_list( request,
            queryset=Nota.objects.filter( anno__exact=anno ),
            paginate_by=100,
            template_name='note/list.html',
            template_object_name='note',
            extra_context={'anno': anno,
                             'anni_note': anni_note,
                             'anno_corrente': anno_corrente}
            )

def note_dettaglio( request, object_id ):
    n = Nota.objects.get( pk=int( object_id ) )
    listaCampi = [( f.verbose_name, eval( "n." + f.name ) ) for f in Nota._meta.fields][3:]
    #listaCampi.insert(0, ("Nota", n.sigla))
    #listaCampi=[(f.verbose_name, f.value_to_string()) for f in Nota._meta.fields]
    return list_detail.object_detail( request,
               queryset=Nota.objects.all(),
               object_id=object_id,
               template_name='note/detail.html',
               template_object_name='nota',
               extra_context={'listaCampi': listaCampi} )

note_create = {#'model': Nota,
               'form_class': NoteCreateForm,
               'template_name': 'note/create.html',
               'post_save_redirect': '/note/%(id)s/'
               }

note_update = {'model': Nota,
               'template_name': 'note/edit.html',
               'post_save_redirect': '/note/%(id)s/'}

note_delete = {'model': Nota,
               'post_delete_redirect': '/note/',
               'template_name': 'note/delete.html',
               'template_object_name': 'nota'}

urlpatterns = patterns( '',
        ( r'^$', login_required( index ) ),
        ( r'^list/(?P<anno>\d{4})/$', login_required( note_per_anno ) ),
        ( r'^create/$', login_required( create_update.create_object ), note_create ),
        ( r'^edit/$', login_required( edit ) ),
        ( r'^delete/$', login_required( delete ) ),
        ( r'^search/$', login_required( search ) ),
        #( r'^(?P<object_id>\d+)/$', list_detail.object_detail, nota_detail ),
        ( r'^(?P<object_id>\d+)/$', login_required( note_dettaglio ) ),
        ( r'^(?P<object_id>\d+)/edit/$', login_required( create_update.update_object ), note_update ),
        ( r'^(?P<object_id>\d+)/delete/$', login_required( create_update.delete_object ), note_delete ),
        ( r'^(?P<object_id>\d+)/aggiungi/$', login_required( aggiungi ) ),
        ( r'^(?P<object_id>\d+)/collega/$', login_required( collega ) ),
        ( r'^(?P<note_id>\d+)/documento/create/$', login_required( creaDocumento ) ),
        ( r'^test/$', 'trACQer.note.views.test' ),
        )

