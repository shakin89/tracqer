
from trACQer.rda.models import SceltaContraente, RichiestaDiAcquisto
from trACQer.rda.models import SceltaContraenteDettaglio, StatoRda
from trACQer.rda.models import FaseProcessoAcquisti, TipologiaContratto
from trACQer.rda.models import DirezioneRichiedente, TipoDataRda

def loadInitialData():
    stati_rda = ('Completa',
                 'In approvazione',
                 'In attesa',
                 'Manca ShC'
                 )

    for stato in stati_rda:
        s = StatoRda()
        s.stato = stato
        s.save()
        del s

    fase_processo_acq = ('Rifiutata dal Buyer',
                'In attesa autorizzazione AD',
                'In attesa approvazione ADI',
                'Sospesa',
                'Manca RDA',
                 'In formalizzazione',
                 'In formalizzazione CEO',
                 'Gara Comunitaria'
                )

    for fase in fase_processo_acq:
        f = FaseProcessoAcquisti()
        f.fase = fase
        f.save()
        del f

    scelta_contraente = ('GPC-ALBO',
                       'GPC-ALBO NEGOZIATA',
                       'GPC- PROCEDURA APERTA',
                       'GPC-PROCEDURA NEGOZIATA',
                       'GPC-PROCEDURA NEGOZIATA SPOT',
                       'GPC-PROCEDURA RISTRETTA',
                       'GP- PROCEDURA APERTA',
                       'GP-PROCEDURA NEGOZIATA',
                       'GP-PROCEDURA NEGOZIATA SPOT',
                       'GP-PROCEDURA RISTRETTA',
                       'GU-GARA UFFICIOSA',
                       'GU-GARA UFFICIOSA DA ALBO',
                       'GU-GARA UFFICIOSA ON LINE ALBO',
                       'RD-RICONOSCIMENTO DI DEBITO',
                       'TD-ALTRO',
                       'TD-DEROGA',
                       'TD-INFRAFRUPPO',
                       'TD-SOTTOSOGLIA REGOLAMENTO'
                       )
    for scelta in scelta_contraente:
        s = SceltaContraente()
        s.scelta_contraente = scelta
        s.save()
        del s

    dettaglio_scelta_contraente = ('AA-ENTRO V D\'OBBL',
                'AA-OPZIONE',
                'ACQ.INFRAGRUPPO',
                'BC/BE DA CONTRATTO',
                'BENI/SERV.COMPLEM',
                'CONTRATTO ATTIVO',
                'CONTRATTO PONTE',
                'FORNITORE DETERMINATO',
                'OFF.INAPPR.IN GARA',
                'PROCEDURA DI GARA',
                'RICERCA',
                'RICONOSC.DEBITO',
                'RINNOVO',
                'RIPETIZIONE',
                'SOTTOSOGLIA ',
                'URGENZA'
                )
    for dett in dettaglio_scelta_contraente:
        d = SceltaContraenteDettaglio()
        d.scelta_contraente_dettaglio = dett
        d.save()
        del d

    tipologia_contratto = ('Fornitura',
                           'Materiali',
                           'Servizi')
    for tipologia in tipologia_contratto:
        t = TipologiaContratto()
        t.tipologia_contratto = tipologia
        t.save()
        del t

    dir_ric = (('TI', "Tecnologie dell'informazione"),
               ('AL', 'Altre'),
               ('TA', 'Tutela Aziendale'),
               )

    for dr in dir_ric:
        d = DirezioneRichiedente()
        d.direzione_richiedente = dr[0]
        d.sigla = dr[1]
        d.attivo = True
        d.save()
        del d

    tipo_data_rda = ('Data Rda SAP',
            "Data Firma RF 3° Livello",
            "Data Firma RF 2° Livello",
            "Data Firma RF 1° Livello",
            "Data Firma A.D.",
                   )
    for tdr in tipo_data_rda:
        t1 = TipoDataRda()
        t1.tipo_data = tdr
        t1.save()
        del t1

    import datetime
    r = RichiestaDiAcquisto()
    r.funzione_origine = 'TI'
    r.numero_richiedente = 'TI-645'
    r.numero = '2000054665'
    r.data_arrivo_acq = datetime.date(2010, 10, 20)
    r.numero_ti = '2010_912'
    r.save()
    del r
    #creo una nuova rda
    r = RichiestaDiAcquisto()
    r.funzione_origine = 'TI'
    r.numero_richiedente = 'TI-533'
    r.numero = '2000041893'
    r.data_arrivo_acq = datetime.date(2010, 9, 3)
    r.numero_ti = '2010_792'
    r.importo_rda_totale = "33122.00"
    r.anno = 2010
    r.save()
    del r
    #creo una nuova rda
    r = RichiestaDiAcquisto()
    r.funzione_origine = 'TA'
    r.numero_richiedente = 'TA-002'
    r.numero = '2000037586'
    r.data_arrivo_acq = datetime.date(2010, 11, 13)
    r.anno = 2010
    r.importo_rda_totale = "245322.23"
    r.save()
    del r


