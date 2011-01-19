from django.db import models
from datetime import datetime

def _get_year():
    return datetime.now().year

class DirezioneRichiedente( models.Model ):
    created = models.DateTimeField( auto_now_add=True )
    last_modified = models.DateTimeField( auto_now=True )
    attivo = models.BooleanField( default=True )
    direzione = models.CharField( max_length=50, unique=True )
    sigla = models.CharField( max_length=2, unique=True )

    def __unicode__( self ):
        return u"(%s) %s" % ( self.sigla, self.direzione )

    class Meta:
        verbose_name_plural = "Direzioni Richiedenti"
        ordering = ['direzione', 'sigla']

class FunzioneRichiedente( models.Model ):
    created = models.DateTimeField( auto_now_add=True )
    last_modified = models.DateTimeField( auto_now=True )
    attivo = models.BooleanField( default=True )
    funzione = models.CharField( max_length=100, unique=True )
    sigla = models.CharField( max_length=20 )
    direzione = models.ForeignKey( DirezioneRichiedente, related_name="funzioni" )
    funzione_riferimento = models.ForeignKey( 'self', blank=True, null=True )

    def __unicode__( self ):
        return u"Dir.: %s / %s (%s)" % ( self.direzione.sigla, self.funzione, self.sigla )

    class Meta:
        verbose_name_plural = "Funzioni Richiedenti"

class TipoDocumento( models.Model ):
    created = models.DateTimeField( auto_now_add=True )
    last_modified = models.DateTimeField( auto_now=True )
    attivo = models.BooleanField( default=True )
    sigla = models.CharField( max_length=40 )
    tipo_documento = models.CharField( max_length=200, blank=True, null=True )

    def __unicode__( self ):
        return self.sigla

    class Meta:
        verbose_name_plural = "Tipi Documento"

class TipologiaContratto( models.Model ):
    created = models.DateTimeField( auto_now_add=True )
    last_modified = models.DateTimeField( auto_now=True )
    attivo = models.BooleanField( default=True )
    tipologia_contratto = models.CharField( max_length=150 )
    sigla = models.CharField( 'Tipologia contratto (abbr.)', max_length=2, null=True, blank=True )

    def __unicode__( self ):
        return "%s" % ( self.tipologia_contratto )

    class Meta():
        verbose_name_plural = "Tipologie Contratto"
        ordering = ["tipologia_contratto"]

class SceltaContraente( models.Model ):
    created = models.DateTimeField( auto_now_add=True )
    last_modified = models.DateTimeField( auto_now=True )
    attivo = models.BooleanField( default=True )
    scelta_contraente = models.CharField( max_length=100 )

    def __unicode__( self ):
        return "%s" % ( self.scelta_contraente )

    class Meta():
        verbose_name_plural = "Scelte Contraente"
        ordering = ["scelta_contraente"]

class SceltaContraenteDettaglio( models.Model ):
    created = models.DateTimeField( auto_now_add=True )
    last_modified = models.DateTimeField( auto_now=True )
    attivo = models.BooleanField( default=True )
    scelta_contraente_dettaglio = models.CharField( 'Dettaglio scelta contraente', max_length=150 )

    def __unicode__( self ):
        return "%s" % ( self.scelta_contraente_dettaglio )

    class Meta():
        verbose_name_plural = "Dettaglio scelte contraente"
        ordering = ["scelta_contraente_dettaglio"]

class FaseProcessoAcquisti( models.Model ):
    created = models.DateTimeField( auto_now_add=True )
    last_modified = models.DateTimeField( auto_now=True )
    attivo = models.BooleanField( default=True )
    fase = models.CharField( 'Fase del processo ACQ', max_length=150 )

    def __unicode__( self ):
        return "%s" % ( self.fase )

    class Meta():
        verbose_name_plural = "Fasi processo ACQ"
        ordering = ["fase"]

    class Meta:
        verbose_name_plural = "Importi Documento"

class TipoFirma( models.Model ):
    """
    TipoFirma elenca le varie tipologie di firme necessarie ad autorizzare
    i documenti
    Es. Firma AD, Firma RF 2L, Firma Resp ACQ (RF 1o Liv.) ecc
    """
    created = models.DateTimeField( auto_now_add=True )
    last_modified = models.DateTimeField( auto_now=True )
    attivo = models.BooleanField( default=True )
    tipo_firma = models.CharField( max_length=50 )
    sigla = models.CharField( max_length=10 )

    def __unicode__( self ):
        return self.tipo_firma

    class Meta():
        verbose_name_plural = "Tipo Firme"

class TipoData( models.Model ):
    """
    TipoData elenca le varie tipologie di date disponibili su un documento
    """
    created = models.DateTimeField( auto_now_add=True )
    last_modified = models.DateTimeField( auto_now=True )
    attivo = models.BooleanField( default=True )
    tipo_data = models.CharField( max_length=30 )

    def __unicode__( self ):
        return self.tipo_data

    class Meta():
        verbose_name_plural = "Tipo Date"

class DataDocumento( models.Model ):
    created = models.DateTimeField( auto_now_add=True )
    last_modified = models.DateTimeField( auto_now=True )
    tipo_data = models.ForeignKey( TipoData )
    data = models.DateField( default=datetime.now )
    documento = models.ForeignKey( "Documento", related_name="data", blank=True, null=True )

    def __unicode__( self ):
        return "%s: %s" % ( self.tipo_data.tipo_data, self.data.strftime( "%d/%m/%Y" ) )

    class Meta():
        verbose_name_plural = "Date documento"

class TipoAssegnazioneDocumento( models.Model ):
    """
    Model: 
    Description: 
    """
    created = models.DateTimeField( auto_now_add=True )
    last_modified = models.DateTimeField( auto_now=True )
    attivo = models.BooleanField( default=True )
    tipo_assegnazione = models.CharField( max_length=50, blank=True, null=True )

    def __unicode__( self ):
        return self.tipo_assegnazione

    class Meta():
        verbose_name_plural = "Tipi assegnazione documenti"

class Nota( models.Model ):
    created = models.DateTimeField( auto_now_add=True )
    last_modified = models.DateTimeField( auto_now=True )
    anno = models.IntegerField( default=_get_year )
    direzione_richiedente = models.ForeignKey( DirezioneRichiedente, related_name="note" )
    numero = models.IntegerField()
    funzione_richiedente = models.ForeignKey( FunzioneRichiedente, related_name="note", blank=True, null=True )
    numero_ti = models.CharField( "Nr. TI", max_length=20, blank=True, null=True )
    protocollo_origine_numero = models.CharField( "Nr. Prot. Origine", max_length=30, blank=True, null=True )
    protocollo_origine_data = models.DateField( "Data Prot. Origine", blank=True, null=True )
    protocollo_acq_numero = models.CharField( "Nr. Prot. ACQ", max_length=30, blank=True, null=True )
    protocollo_acq_data = models.DateField( "Data Prot. ACQ", blank=True, null=True )
    note = models.TextField( blank=True, null=True )

    def __unicode__( self ):
        return u"Nota %s" % ( self.sigla )

    def _get_sigla( self ):
        return "%s-%s" % ( self.direzione_richiedente.sigla, self.numero )
    sigla = property( _get_sigla )

    def get_absolute_url( self ):
        return "/note/%i/" % ( self.id )

    class Meta:
        verbose_name_plural = 'Note'
        ordering = ['anno']
        unique_together = ['anno', 'numero']

class StatoRda( models.Model ):
    created = models.DateTimeField( auto_now_add=True )
    last_modified = models.DateTimeField( auto_now=True )
    attivo = models.BooleanField( default=True )
    stato = models.CharField( max_length=100 )

    def __unicode__( self ):
        return "%s" % ( self.stato )

    class Meta():
        verbose_name_plural = "Stati R.d.A."
        ordering = ["stato"]

class Documento( models.Model ):
    #------------------------------------------------------- 
    # DATI GENERALI
    #-------------------------------------------------------     
    created = models.DateTimeField( auto_now_add=True )
    last_modified = models.DateTimeField( auto_now=True )
    nota = models.ForeignKey( Nota, related_name="documenti" )
    tipo_documento = models.ForeignKey( TipoDocumento )
    numero_documento = models.IntegerField()
    numero_riferimento = models.IntegerField( blank=True, null=True )
    numero_riferimento2 = models.IntegerField( blank=True, null=True )
    #data = models.ForeignKey( DataDocumento, blank=True, null=True )
    descrizione = models.CharField( max_length=500, null=True, blank=True )

    stato_rda = models.ForeignKey( StatoRda, null=True, blank=True )
    annullata = models.BooleanField( default=False )
    deroga = models.BooleanField( "R.d.A. con deroga?", default=False )
    deroga_rifiutata = models.BooleanField( "Deroga Rifiutata", default=False )
    data_deroga_anpa = models.DateField( null=True, blank=True )
    codice_progetto_investimento = models.CharField( max_length=20, null=True, blank=True )
    gruppo_merci = models.CharField( max_length=20, null=True, blank=True )

    #------------------------------------------------------- 
    # STATI AVANZAMENTO
    #-------------------------------------------------------     
    fase_processo_acquisti = models.ForeignKey( FaseProcessoAcquisti, blank=True, null=True )
    tipologia_contratto = models.ForeignKey( TipologiaContratto, null=True, blank=True )
    scelta_contraente = models.ForeignKey( SceltaContraente, blank=True, null=True )
    scelta_contraente_dettaglio = models.ForeignKey( SceltaContraenteDettaglio, blank=True, null=True )

    #------------------------------------------------------- 
    #DATI AMMINISTRATIVI
    #-------------------------------------------------------     
    cig = models.CharField( max_length=20, null=True, blank=True )
    cup = models.CharField( max_length=20, null=True, blank=True )
    codice_gara = models.CharField( max_length=20, null=True, blank=True )
    codice_simog = models.CharField( max_length=20, null=True, blank=True )

    #------------------------------------------------------- 
    # IMPORTI
    #-------------------------------------------------------     
    #importo_base = models.ForeignKey( ImportoDocumento, related_name="importo_base", blank=True, null=True )
    #importo_aggiudicazione = models.ForeignKey( ImportoDocumento, related_name="importo_aggiudicazione", blank=True, null=True )

    fornitore = models.CharField( max_length=100, blank=True, null=True )

    #------------------------------------------------------- 
    # ASSEGNATARI
    #-------------------------------------------------------     
    #assegnazione = models.ForeignKey( AssegnazioneDocumento, blank=True, null=True )

    #------------------------------------------------------- 
    # TRACKING FIRME
    #-------------------------------------------------------     
    #firma = models.ForeignKey( FirmaDocumento, blank=True, null=True )


    def __unicode__( self ):
        return "Doc: %s numero %d" % ( self.tipo_documento.sigla, self.numero_documento )

    def _get_importo_base_totale( self ):
        importo_totale = 0.0
        for i in self.importo_base:
            importo_totale += i.importo
        return importo_totale
    importo_base_totale = property( _get_importo_base_totale )

    def _get_importo_aggiudicazione_totale( self ):
        importo_totale = 0.0
        for i in self.importo_aggiudicazione:
            importo_totale += i.importo
        return importo_totale
    importo_aggiudicazione_totale = property( _get_importo_aggiudicazione_totale )

    def _get_delta_euro( self ):
        delta_euro = 0.0
        if self.importo_aggiudicazione and self.importo_base:
            delta_euro = self.importo_base_totale - self.importo_aggiudicazione_totale
        return delta_euro
    delta_euro = property( _get_delta_euro )

    def get_absolute_url( self ):
        return "/documenti/%d/" % ( self.id )

    class Meta():
        verbose_name_plural = "Documenti"

class ImportoDocumento( models.Model ):
    """
    ImportoDocumento serve per tenere traccia degli importi
    delle RDA, delle Oda e dei bc, nonche' degli AQ.
    L'importo puo' anche essere suddiviso per anno.
    """
    created = models.DateTimeField( auto_now_add=True )
    last_modified = models.DateTimeField( auto_now=True )
    anno = models.IntegerField( default=_get_year )
    importo = models.DecimalField( max_digits=25, decimal_places=4, null=True, blank=True )
    importo_documento = models.ForeignKey( Documento, related_name="importo_documento", null=True, blank=True )
    importo_aggiudicazione = models.ForeignKey( Documento, related_name="importo_aggiudicazione", null=True, blank=True )

    def __unicode__( self ):
        return "Anno: %d - Importo: %25.2f" % ( self.anno, self.importo )

class AssegnazioneDocumento( models.Model ):
    """
    AssegnazioneDocumento elenca i vari step di assegnazione di un documento
    """
    created = models.DateTimeField( auto_now_add=True )
    last_modified = models.DateTimeField( auto_now=True )
    tipo_assegnazione = models.ForeignKey( TipoAssegnazioneDocumento )
    data_assegnazione = models.DateField( default=datetime.now )
    #assegnatario = models.ForeignKey( "Buyer" )
    documento = models.ForeignKey( Documento, related_name="assegnazione", blank=True, null=True )

    def __unicode__( self ):
        return self.tipo_assegnazione.tipo_assegnazione

    class Meta():
        verbose_name_plural = "Assegnazioni Documenti"

class FirmaDocumento( models.Model ):
    """
    FirmaDocumento tiene traccia delle firme apposte sui documenti
    """
    created = models.DateTimeField( auto_now_add=True )
    last_modified = models.DateTimeField( auto_now=True )
    attivo = models.BooleanField( default=True )
    data = models.DateField()
    tipo_firma = models.ForeignKey( TipoFirma )
    documento = models.ForeignKey( Documento, related_name="firma", blank=True, null=True )

    def __unicode__( self ):
        return "Data: %s - Firma: %s" % ( self.data, self.tipo_firma.tipo_firma )

    class Meta():
        verbose_name_plural = "Firme Documenti"





