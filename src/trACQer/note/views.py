# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.views.generic import list_detail
from django.shortcuts import render_to_response
from trACQer.note.forms import SearchFormSet
from trACQer.note.models import Nota

def index( request ):
    import datetime
    anno = datetime.datetime.now().year
    url = '/note/list/%d/' % ( anno )
    return HttpResponseRedirect( url )

def edit( request ):
    return search( request, optional_h3="Ricerca Nota per modifica." )

def delete( request ):
    return search( request, optional_h3="Ricerca Nota per cancellazione." )

def search( request, optional_h3=None ):
    if request.method == "POST":
        formset = SearchFormSet( request.POST )
        if formset.is_valid():
            filter_dict = {}
            for cdata in formset.cleaned_data:
                if cdata['valore']:
                    campo = cdata['campo']
                    criterio = cdata['criterio']
                    valore = cdata['valore']
                    filter_dict.setdefault( campo + '__' + criterio, valore )
            return list_detail.object_list( request,
                queryset=Nota.objects.filter( **filter_dict ),
                paginate_by=100,
                template_name='note/list.html',
                template_object_name='note' )
        else:
            return HttpResponse( formset.errors )
    else:
        if not optional_h3:
            optional_h3 = "Ricerca Nota"
        form = SearchFormSet( initial=[{'campo':'anno'}, {'campo':'direzione_richiedente'},
                                      {'campo':'numero'},
                                       {'campo':'protocollo_origine_numero'}] )
        return render_to_response( 'note/search.html',
                    {'form': form, 'optional_h3': optional_h3},
                    context_instance=RequestContext( request ) )

def aggiungi( request, object_id ):
    tipo = request.GET['tipo']
    if 'tipo' in request.GET and tipo:
        if tipo == 'oda':
            request.session['nota_id'] = object_id
            return HttpResponseRedirect( '/oda/create/' )
        if tipo == 'rda':
            request.session['nota_id'] = object_id
            return HttpResponseRedirect( '/rda/create/' )
        if tipo == 'gara':
            request.session['nota_id'] = object_id
            return HttpResponseRedirect( '/gara/create/' )
        return Http404
    else:
        return Http404

def collega( request, type=None ):
    pass

def test( request ):
    #===========================================================================
    # if request.session['nota_id']:
    #    nota_id = request.session.get( 'nota_id' )
    #    del request.session['nota_id']
    #===========================================================================
    return render_to_response( 'note/test.html',
                context_instance=RequestContext( request ) )
