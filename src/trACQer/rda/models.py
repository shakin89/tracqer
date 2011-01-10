from django.db import models
#from trACQer.imprese.models import Impresa
from trACQer.buyers.models import Buyer
from datetime import datetime

class DirezioneRichiedente( models.Model ):
    created = models.DateTimeField( auto_now_add = True )
    last_modified = models.DateTimeField( auto_now = True )
    direzione_richiedente = models.CharField( max_length = 100 )
    sigla = models.CharField( max_length = 2 )
    attivo = models.BooleanField()

    def __unicode( self ):
        return "Direzione: (%s) %s" % ( self.sigla, self.direzione_richiedente )

    class Meta:
        ordering = ['sigla', 'direzione_richiedente']
        verbose_name_plural = "Direzioni Richiedenti"

class StatoRda( models.Model ):
    stato = models.CharField( max_length = 100 )

    def __unicode__( self ):
        return "%s" % ( self.stato )

    class Meta():
        verbose_name_plural = "Stati R.d.A."
        ordering = ["stato"]

class FaseProcessoAcquisti( models.Model ):
    fase = models.CharField( 'Fase del processo ACQ', max_length = 150 )

    def __unicode__( self ):
        return "%s" % ( self.fase )

    class Meta():
        verbose_name_plural = "Fasi processo ACQ"
        ordering = ["fase"]

class TipologiaContratto( models.Model ):
    tipologia_contratto = models.CharField( max_length = 150 )
    slug = models.CharField( 'Tipologia contratto (abbr.)', max_length = 2, null = True, blank = True )

    def __unicode__( self ):
        return "%s" % ( self.tipologia_contratto )

    class Meta():
        verbose_name_plural = "Tipologie Contratto"
        ordering = ["tipologia_contratto"]

class SceltaContraente( models.Model ):
    scelta_contraente = models.CharField( max_length = 100 )

    def __unicode__( self ):
        return "%s" % ( self.scelta_contraente )

    class Meta():
        verbose_name_plural = "Scelte Contraente"
        ordering = ["scelta_contraente"]

class SceltaContraenteDettaglio( models.Model ):
    scelta_contraente_dettaglio = models.CharField( 'Dettaglio scelta contraente', max_length = 150 )

    def __unicode__( self ):
        return "%s" % ( self.scelta_contraente_dettaglio )

    class Meta():
        verbose_name_plural = "Dettaglio scelte contraente"
        ordering = ["scelta_contraente_dettaglio"]

class ImportoOda( models.Model ):
    anno = models.IntegerField( "Anno" )
    importo_oda = models.DecimalField( "Importo O.d.A.", max_digits = 25, decimal_places = 5 )

class TempoAttraversamento( models.Model ):
    tempo_attraversamento = models.IntegerField( blank = True, null = True )

    def __unicode__( self ):
        return "%s" % str( self.tempo_attraversamento )

class TipoDataRda( models.Model ):
    tipo_data = models.CharField( max_length = 100 )

    def __unicode__( self ):
        return str( self.tipo_data )

class DataRda( models.Model ):
    tipo = models.ForeignKey( TipoDataRda )
    data = models.DateField()

    def __unicode__( self ):
        return str( self.tipo )

class ShoppingCart( models.Model ):
    created = models.DateTimeField( auto_now_add = True )
    last_modified = models.DateTimeField( auto_now = True )
    anno = models.IntegerField( default = datetime.now().year )
    numero_sc = models.CharField( 'Numero S.C.', max_length = 30, unique = True, null = True, blank = True )
    data_sc = models.DateField( 'Data S.C.', null = True, blank = True )
    descrizione = models.CharField( max_length = 500, null = True, blank = True )

    stato_rda = models.ForeignKey( StatoRda, related_name = 'rda', null = True, blank = True )
    annullata = models.BooleanField( default = False )
    deroga = models.BooleanField( "R.d.A. con deroga?", default = False )
    cdc_investimento = models.CharField( 'C.d.C. / Investimento', max_length = 20, null = True, blank = True )
    gruppo_merci = models.CharField( max_length = 20, null = True, blank = True )

    ##################################################
    # DATE
    ##################################################
    #data protocollo rda
    #data_rda_cartacea = models.DateField('Data R.d.A. cartacea', null = True, blank = True)
    #data timbro arrivo protocollo acq
    #data_arrivo_acq = models.DateField(null = True, blank = True)
    #data assegnazione sc in sap
    #data_rda_sap = models.DateField(null = True, blank = True)
    #???
    #data_firma = models.DateField(null = True, blank = True)
    # data arrivo deroga
    data_deroga_anpa = models.DateField( null = True, blank = True )

    #data_oda_meno_data_arrivo_dcia = models.IntegerField('Data OdA - Data arr. DCIA', null = True, blank = True)
    #oggi_meno_data_arrivo_dcia = models.IntegerField('Oggi - Data arr. DCIA', null = True, blank = True)
    #data_rda_sap_meno_data_rda_cartacea = models.IntegerField('Data RdA SAP - Data RdA cartacea', null = True, blank = True)
    #oggi_meno_data_rda_cartacea = models.IntegerField('Oggi - Data RdA cartacea', null = True, blank = True)
    #data_oda_meno_data_rda_sap = models.IntegerField('Data OdA meno Data RdA SAP', null = True, blank = True)
    #oggi_meno_data_rda_sap = models.IntegerField(null = True, blank = True)
    # il campo sottostante e' il minimo valore tra 
    # data_oda_meno_data_arrivo_dcia 
    # e tra 
    #data_oda_meno_data_rda_sap
    #data_oda_rda_sap_rda_cartacea = models.IntegerField(null = True, blank = True)
    #come si calcola il tempo di attraversamento
    #se il campo soprastante e' uguale a zero allora
    # il tempo di attraversamento e' il minimo tra 
    #oggi_meno_data_arrivo_dcia e tra oggi_meno_data_rda_sap
    #altrimenti 
    #  se il campo soprastante e' minore di zero allora 
    #    il tempo di attraversamento e' 
    #    data_oda_meno_data_rda_sap
    #  altrimenti 
    #    e' il campo soprastante
    #tempo_di_attraversamento = models.IntegerField(null = True, blank = True)
    #tempo_attraversamento_gg_solari = models.IntegerField(null = True, blank = True)
    #tempo_attraversamento_gg_lavorativi = models.IntegerField(null = True, blank = True)

    ##################################################
    # IMPORTI
    ##################################################
    #importo_rda_totale = models.DecimalField(max_digits = 25, decimal_places = 4, null = True, blank = True)
    #importo_rda_anno_1 = models.DecimalField(max_digits = 25, decimal_places = 4, null = True, blank = True)
    #importo_rda_anno_2 = models.DecimalField(max_digits = 25, decimal_places = 4, null = True, blank = True)
    #importo_rda_anno_3 = models.DecimalField(max_digits = 25, decimal_places = 4, null = True, blank = True)

    #oda_contratto = models.CharField('O.d.A. / Contratto', max_length = 30, null = True, blank = True)
    #data_oda_contraatto = models.DateField(null = True, blank = True)
    #importo_oda_totale = models.DecimalField(max_digits = 25, decimal_places = 4, null = True, blank = True)
    #importo_oda_anno_1 = models.DecimalField(max_digits = 25, decimal_places = 4, null = True, blank = True)
    #importo_oda_anno_2 = models.DecimalField(max_digits = 25, decimal_places = 4, null = True, blank = True)
    #importo_oda_anno_3 = models.DecimalField(max_digits = 25, decimal_places = 4, null = True, blank = True)

    #delta_euro = models.DecimalField(max_digits = 25, decimal_places = 4, null = True, blank = True)
    #delta_euro_su_quota_anno_1 = models.DecimalField(max_digits = 25, decimal_places = 4, null = True, blank = True)
    #delta_percentuale = models.DecimalField(max_digits = 10, decimal_places = 4, null = True, blank = True)

    fase_processo_acquisti = models.ForeignKey( FaseProcessoAcquisti, blank = True, null = True )
    #societa_richiesta_id = models.ForeignKey()
    #societa_aggiudicataria_id = models.ForeignKey()
    fornitore = models.CharField( max_length = 100, null = True, blank = True )
    tipologia_contratto = models.ForeignKey( TipologiaContratto, null = True, blank = True )
    scelta_contraente = models.ForeignKey( SceltaContraente, blank = True, null = True )
    scelta_contraente_dettaglio = models.ForeignKey( SceltaContraenteDettaglio, blank = True, null = True )
    note = models.TextField( null = True, blank = True )

    #buyer_id = models.ForeignKey()
    #buyer = relation('Buyer', foreign_keys=buyer_id, primaryjoin='rda.buyer_id == buyer.id')
    #buyer = models.CharField(max_length=100, null=True, blank=True)

    ##################################################
    # DATI AMMINISTRATII
    ##################################################
    cig = models.CharField( max_length = 20, null = True, blank = True )
    cup = models.CharField( max_length = 20, null = True, blank = True )
    codice_gara = models.CharField( max_length = 20, null = True, blank = True )
    codice_simog = models.CharField( max_length = 20, null = True, blank = True )

    ##################################################
    # TRACKING FIRME
    ##################################################
    #firma_rf_3l = models.CharField(max_length = 100, null = True, blank = True)
    #data_firma_rf_3l = models.DateField(null = True, blank = True)
    #firma_rf_2l = models.CharField(max_length = 100, null = True, blank = True)
    #data_firma_rf_2l = models.DateField(null = True, blank = True)
    #firma_rf_1l = models.CharField(max_length = 100, null = True, blank = True)
    #data_firma_rf_1l = models.DateField(null = True, blank = True)
    #firma_ad = models.CharField(max_length = 100, null = True, blank = True)
    #data_firma_ad = models.DateField(null = True, blank = True)

    #allegato1 = Column(Unicode(1))
    #allegato2 = Column(Unicode(1))
    rf_3l_assegnatario = models.CharField( max_length = 100, null = True, blank = True )
    rf_3l_data_assegnazione = models.DateField( null = True, blank = True )
    #buyer_id = Column(Integer, ForeignKey('buyer.id'), nullable=True)
    #buyer_assegnatario = relation('Buyer', foreign_keys=buyer_id) #, primaryjoin='rda.buyer_id == buyer.id')
    buyer_assegnatario = models.ForeignKey( Buyer, blank = True, null = True )
    data_assegnazione_buyer = models.DateField( null = True, blank = True )

    def __unicode__( self ):
        return self.numero + ' - ' + self.funzione_origine + '-' + str( self.numero_origine )

    class Meta:
        verbose_name_plural = "Richieste di Acquisto"

class RichiestaDiAcquisto( models.Model ):
    created = models.DateTimeField( auto_now_add = True )
    last_modified = models.DateTimeField( auto_now = True )
    anno = models.IntegerField( default = datetime.now().year )
    numero = models.CharField( "Numero R.d.A.", max_length = 30 )

class ImportoRda( models.Model ):
    anno = models.IntegerField( "Anno" )
    importo_rda = models.DecimalField( "Importo R.d.A.", max_digits = 25, decimal_places = 5 )
    rda = models.ForeignKey( RichiestaDiAcquisto )

    def __unicode__( self ):
        return "Rda: %s - Anno: %s - Importo: %s" % ( str( self.rda ), str( self.anno ), str( self.importo_rda ) )


