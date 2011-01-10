from django.db import models
from datetime import datetime

# Create your models here.

class DirezioneRichiedente( models.Model ):
    created = models.DateTimeField( auto_now_add = datetime.now() )
    last_modified = models.DateTimeField( auto_now = datetime.now() )
    direzione = models.CharField( max_length = 50, unique = True )
    sigla = models.CharField( max_length = 2, unique = True )
    attivo = models.BooleanField()

    def __unicode__( self ):
        return u"(%s) %s" % ( self.sigla, self.direzione )

    class Meta:
        verbose_name_plural = "Direzioni Richiedenti"
        ordering = ['direzione', 'sigla']

class FunzioneRichiedente( models.Model ):
    created = models.DateTimeField( auto_now_add = datetime.now() )
    last_modified = models.DateTimeField( auto_now = datetime.now() )
    funzione = models.CharField( max_length = 100, unique = True )
    sigla = models.CharField( max_length = 20 )
    direzione = models.ForeignKey( DirezioneRichiedente, related_name = "funzioni" )
    funzione_riferimento = models.ForeignKey( 'self', blank = True, null = True )
    attivo = models.BooleanField()

    def __unicode__( self ):
        return u"Dir.: %s / %s (%s)" % ( self.direzione.sigla, self.funzione, self.sigla )

    class Meta:
        verbose_name_plural = "Funzioni Richiedenti"

class Nota( models.Model ):
    created = models.DateTimeField( auto_now_add = datetime.now() )
    last_modified = models.DateTimeField( auto_now = datetime.now() )
    anno = models.IntegerField( default = datetime.now().year )
    direzione_richiedente = models.ForeignKey( DirezioneRichiedente, related_name = "note" )
    numero = models.IntegerField()
    funzione_richiedente = models.ForeignKey( FunzioneRichiedente, related_name = "note", blank = True, null = True )
    numero_ti = models.CharField( max_length = 20, blank = True, null = True )
    protocollo_origine_numero = models.CharField( max_length = 30, blank = True, null = True )
    protocollo_origine_data = models.DateField( blank = True, null = True )
    protocollo_acq_numero = models.CharField( max_length = 30, blank = True, null = True )
    protocollo_acq_data = models.DateField( blank = True, null = True )
    note = models.TextField( blank = True, null = True )


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

