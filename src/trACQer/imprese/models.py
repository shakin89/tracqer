from django.db import models

# Create your models here.
class Impresa(models.Model):
    ragione_sociale = models.CharField(max_length=200)
    cf = models.CharField(max_length=20, null=True, blank=True)
    
    def __unicode__(self):
        return "%s" % (self.ragione_sociale)
    
    class Meta():
        verbose_name_plural = "Imprese"