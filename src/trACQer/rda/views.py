# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import list_detail
from django.shortcuts import render_to_response
from django.template import RequestContext
from trACQer.rda.forms import SearchFormSet
from trACQer.rda.models import RichiestaDiAcquisto
from datetime import datetime

def index(request):
    import datetime
    anno = datetime.datetime.now().year
    return HttpResponseRedirect('/rda/list/%d/' % (anno))

def edit(request):
    return search(request, optional_h3 = "Ricerca R.d.A. per modifica.")

def delete(request):
    return search(request, optional_h3 = "Ricerca R.d.A. per cancellazione.")

def search(request, optional_h3 = None):
    if request.method == "POST":
        formset = SearchFormSet(request.POST)
        if formset.is_valid():
            listaCampi = []
            for f in RichiestaDiAcquisto._meta.fields:
                listaCampi.append(f.name)
            filter_dict = {}
            for cdata in formset.cleaned_data:
                if cdata['valore']:
                    campo = cdata['campo']
                    criterio = cdata['criterio']
                    valore = cdata['valore']
                    filter_dict.setdefault(campo + '__' + criterio, valore)
            return list_detail.object_list(request,
                queryset = RichiestaDiAcquisto.objects.filter(**filter_dict),
                paginate_by = 100,
                template_name = 'rda/list.html',
                template_object_name = 'rda')
        else:
            return HttpResponse(formset.errors)
    else:
        if not optional_h3:
            optional_h3 = "Ricerca R.d.A."
        form = SearchFormSet(initial = [{'campo':'numero'}, {'campo':'anno'},
                                      {'campo':'protocollo_origine_numero'},
                                       {'campo':'protocollo_origine_data'}])
        return render_to_response('rda/search.html',
                    {'form': form, 'optional_h3': optional_h3},
                    context_instance = RequestContext(request))


