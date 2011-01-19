'''
Created on 24/nov/2010

@author: manci409
'''
from trACQer.note.models import Nota, DirezioneRichiedente, FunzioneRichiedente
from trACQer.note.models import AssegnazioneDocumento, DataDocumento, Documento
from trACQer.note.models import FaseProcessoAcquisti, FirmaDocumento, ImportoDocumento
from trACQer.note.models import SceltaContraente, SceltaContraenteDettaglio, StatoRda
from trACQer.note.models import TipoAssegnazioneDocumento, TipoData, TipoDocumento
from trACQer.note.models import TipoFirma, TipologiaContratto
from django.contrib import admin

class NoteAdmin( admin.ModelAdmin ):
    list_display = ( 'anno', 'sigla' )
admin.site.register( Nota, NoteAdmin )

class DirezioneRichiedenteAdmin( admin.ModelAdmin ):
    pass
admin.site.register( DirezioneRichiedente, DirezioneRichiedenteAdmin )

class FunzioneRichiedenteAdmin( admin.ModelAdmin ):
    pass
admin.site.register( FunzioneRichiedente, FunzioneRichiedenteAdmin )

class AssegnazioneDocumentoAdmin( admin.TabularInline ):
    model = AssegnazioneDocumento
    extra = 1
#admin.site.register( AssegnazioneDocumento, AssegnazioneDocumentoAdmin )

class DataDocumentoAdmin( admin.TabularInline ):
    model = DataDocumento
    extra = 1
#admin.site.register( DataDocumento, DataDocumentoAdmin )

class ImportoDocumentoAdmin( admin.TabularInline ):
    model = ImportoDocumento
    extra = 1
    fk_name = "importo_documento"
    fields = ( 'anno', 'importo', )
#admin.site.register( ImportoDocumento, ImportoDocumentoAdmin )

class ImportoAggiudicazioneAdmin( admin.TabularInline ):
    model = ImportoDocumento
    extra = 1
    fk_name = "importo_aggiudicazione"
    fields = ( 'anno', 'importo', )

class FaseProcessoAcquistiAdmin( admin.ModelAdmin ):
    pass
admin.site.register( FaseProcessoAcquisti, FaseProcessoAcquistiAdmin )

class FirmaDocumentoAdmin( admin.TabularInline ):
    model = FirmaDocumento
    extra = 1
    fields = ( "tipo_firma", "data", )
#admin.site.register( FirmaDocumento, FirmaDocumentoAdmin )

class DocumentoAdmin( admin.ModelAdmin ):
    inlines = [DataDocumentoAdmin, ImportoDocumentoAdmin, ImportoAggiudicazioneAdmin, FirmaDocumentoAdmin]
admin.site.register( Documento, DocumentoAdmin )

class SceltaContraenteAdmin( admin.ModelAdmin ):
    pass
admin.site.register( SceltaContraente, SceltaContraenteAdmin )

class SceltaContraenteDettaglioAdmin( admin.ModelAdmin ):
    pass
admin.site.register( SceltaContraenteDettaglio, SceltaContraenteDettaglioAdmin )

class StatoRdaAdmin( admin.ModelAdmin ):
    pass
admin.site.register( StatoRda, StatoRdaAdmin )

class TipoAssegnazioneDocumentoAdmin( admin.ModelAdmin ):
    pass
admin.site.register( TipoAssegnazioneDocumento, TipoAssegnazioneDocumentoAdmin )

class TipoDataAdmin( admin.ModelAdmin ):
    pass
admin.site.register( TipoData, TipoDataAdmin )

class TipoDocumentoAdmin( admin.ModelAdmin ):
    pass
admin.site.register( TipoDocumento, TipoDocumentoAdmin )

class TipoFirmaAdmin( admin.ModelAdmin ):
    pass
admin.site.register( TipoFirma, TipoFirmaAdmin )

class TipologiaContrattoAdmin( admin.ModelAdmin ):
    pass
admin.site.register( TipologiaContratto, TipologiaContrattoAdmin )

