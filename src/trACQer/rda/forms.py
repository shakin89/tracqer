
from django import forms
from trACQer.rda.models import RichiestaDiAcquisto

def creaListaCampi():
    counter = 0
    lista = []
    for f in RichiestaDiAcquisto._meta.fields:
        counter +=1
        if f.name != "id" and f.name != "created" and f.name != "last_modified":
            lista.append((f.name, f.name))
    return lista

listaCampi = creaListaCampi()
criteriRicerca = (('iexact', 'Uguale a'),
                  ('gt', 'Maggiore di'),
                  ('gte', 'Maggiore uguale a'),
                  ('lt', 'Minore di'),
                  ('lte', 'Minore uguale a'),
                  ('icontains', 'Contiene'),
                  ('istartswith', 'Inizia per')
                  )

class SearchForm(forms.Form):
    campo = forms.ChoiceField(choices=listaCampi, label="")
    criterio = forms.ChoiceField(choices=criteriRicerca, label="")
    valore = forms.CharField(max_length=100, label="", required=False)

SearchFormSet = forms.formsets.formset_factory(SearchForm, max_num=4)