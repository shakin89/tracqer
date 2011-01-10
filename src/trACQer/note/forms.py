
from django import forms
from django.db.models import Max
from trACQer.note.models import Nota
from django.db import transaction

def creaListaCampi():
    counter = 0
    lista = []
    for f in Nota._meta.fields:
        counter += 1
        if f.name != "id" and f.name != "created" and f.name != "last_modified":
            lista.append( ( f.name, f.name ) )
    return lista

listaCampi = creaListaCampi()
criteriRicerca = ( ( 'iexact', 'Uguale a' ),
                  ( 'gt', 'Maggiore di' ),
                  ( 'gte', 'Maggiore uguale a' ),
                  ( 'lt', 'Minore di' ),
                  ( 'lte', 'Minore uguale a' ),
                  ( 'icontains', 'Contiene' ),
                  ( 'istartswith', 'Inizia per' )
                  )


class NoteCreateForm( forms.ModelForm ):
    class Meta:
        model = Nota
        exclude = ( 'numero', )
    
    @transaction.commit_on_success
    def save( self, commit=True ):
        model = super( NoteCreateForm, self ).save( commit=False ) 
        num = Nota.objects.filter( anno__exact=model.anno ).aggregate( Max( 'numero' ) )
        model.numero = int( num.get( 'numero__max', 0 ) ) + 1
        if commit:
            model.save()
        return model
    
class SearchForm( forms.Form ):
    campo = forms.ChoiceField( choices=listaCampi, label="" )
    criterio = forms.ChoiceField( choices=criteriRicerca, label="" )
    valore = forms.CharField( max_length=100, label="", required=False )

SearchFormSet = forms.formsets.formset_factory( SearchForm, max_num=4 )



