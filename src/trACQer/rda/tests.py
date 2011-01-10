"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase

###############################################################
# TEST DEI MODELLI
###############################################################
from trACQer.rda.models import RichiestaDiAcquisto, FaseProcessoAcquisti
from trACQer.rda.models import ImportoOda, ImportoRda, SceltaContraente
from trACQer.rda.models import SceltaContraenteDettaglio, StatoRda
from trACQer.rda.models import TipologiaContratto
from decimal import Decimal

class RdaTestCase(TestCase):
    def setUp(self):
        self.rda1 = RichiestaDiAcquisto.objects.create(funzione_origine='TI', 
                    numero_origine='235',
                    numero='2000045723')
        
    def testExist(self):
        self.assertEqual(self.rda1.numero, '2000045723')
        self.assertEqual(self.rda1.funzione_origine, 'TI')
        self.assertEqual(self.rda1.numero_origine, '235')
        self.assertEqual(str(self.rda1), '2000045723 - TI-235')

class FaseProcessoAcqTestCase(TestCase):
    def setUp(self):
        self.fase1 = FaseProcessoAcquisti.objects.create(fase='Manca Rda')
        self.fase2 = FaseProcessoAcquisti.objects.create(fase='Sospesa')
    
    def testExistFase1(self):
        self.assertEqual(self.fase1.fase, 'Manca Rda')
        self.assertNotEqual(self.fase1.fase, 'approvata')
    
    def testExistFase2(self):
        self.assertEqual(self.fase2.fase, 'Sospesa')
        self.assertNotEqual(self.fase2.fase, 'approvata')

class ImportoOdaTestCase(TestCase):
    def setUp(self):
        self.importo1 = ImportoOda.objects.create(anno=2010, \
                                        importo_oda=Decimal('13210.25'))
        self.importo2 = ImportoOda.objects.create(anno=2011, \
                                        importo_oda=Decimal('2000.00'))
        
    def testImporto1(self):
        self.assertEqual(self.importo1.anno, 2010)
        self.assertEqual(self.importo1.importo_oda, Decimal('13210.25'))
    
    def testImporto2(self):
        self.assertEqual(self.importo2.anno, 2011)
        self.assertEqual(self.importo2.importo_oda, Decimal('2000'))
        self.assertEqual(self.importo2.importo_oda, 2000)
        self.assertNotEqual(self.importo2.importo_oda,'2000')
        
class ImportoRdaTestCase(TestCase):
    def setUp(self):
        self.importo1 = ImportoRda.objects.create(anno=2010, \
                                        importo_rda=Decimal('23220.25'))
        self.importo2 = ImportoRda.objects.create(anno=2011, \
                                        importo_rda=Decimal('4000.00'))
        
    def testImporto1(self):
        self.assertEqual(self.importo1.anno, 2010)
        self.assertEqual(self.importo1.importo_rda, Decimal('23220.25'))
    
    def testImporto2(self):
        self.assertEqual(self.importo2.anno, 2011)
        self.assertEqual(self.importo2.importo_rda, Decimal('4000'))
        self.assertEqual(self.importo2.importo_rda, 4000)
        self.assertNotEqual(self.importo2.importo_rda,'4000')
        self.assertNotEqual(self.importo2.importo_rda, 2000)

class SceltaContraenteTestCase(TestCase):
    def setup(self):
        self.scelta1 = SceltaContraente.objects.create(
                                scelta_contraente='GPC-ALBO')
    
    def testScelta1(self):
        self.assertEqual(self.scelta1.scelta_contraente, 'GPC-ALBO')
        self.assertNotEqual(self.scelta1.scelta_contraente, 'GPC-ALBO NEGOZIATA')

class SceltaContraenteDettaglioTestCase(TestCase):
    def setUp(self):
        self.scelta1 = SceltaContraenteDettaglio.objects.create(
                            scelta_contraente_dettaglio='SOTTOSOGLIA')
        
    def testScelta1(self):
        self.assertEqual(self.scelta1.scelta_contraente_dettaglio, 
                         'SOTTOSOGLIA')

class StatoRdaTestCase(TestCase):
    def setUp(self):
        self.stato1 = StatoRda.objects.create(stato='Completa')
        
    def testStato1(self):
        self.assertEqual(self.stato1.stato, 'Completa')

class TipologiaContrattoTestCase(TestCase):
    def setUp(self):
        self.tipo1 = TipologiaContratto.objects.create(tipologia_contratto='Servizi')

    def testTipo1(self):
        self.assertEqual(self.tipo1.tipologia_contratto, 'Servizi')


#===============================================================================
# class SimpleTest(TestCase):
#    def test_basic_addition(self)
#        """
#        Tests that 1 + 1 always equals 2.
#        """
#        self.failUnlessEqual(1 + 1, 2)
# 
# __test__ = {"doctest": """
# Another way to test that 1 + 1 is equal to 2.
# 
# >>> 1 + 1 == 2
# True
# """}
#===============================================================================

