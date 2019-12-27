############################# HEADER ######################################
#
# beri obstojeco sqlite bazo
# vrni podatke za prikaz ve menijih uporabniskega vmesnika
# 
# vracaj skupine, izvedbe, velikosti
# dosegljive izvedbe glede na skupini, velikosti glede na izvedbo
#
###########################################################################

# imports
from collections import defaultdict
import sqlite3
import os


class Baza():
    def __init__(self):
        self.segment='chiller'

    def povezi_bazo(self):
        """Preveri povezavo z bazo sqlite.
        """
        f_path = os.path.dirname(os.path.abspath(__file__))
        b_path = "SQL_" + self.segment + ".db"
        self.pot_baza = os.path.join(f_path,b_path)

    def poisci_modele(self):
        """Poisci vse izvedbe za 
        """
        b = sqlite3.connect(self.pot_baza)
        baza = b.cursor()
        baza.execute('''SELECT DISTINCT "{}" 
                        FROM "GENERAL" 
                        ORDER BY NumID'''.format('Group'))
        self.modeli = [i[0] for i in baza.fetchall()]
        b.close()
        return self.modeli

    def poisci_izvedbe(self, mo):
        b = sqlite3.connect(self.pot_baza)
        baza = b.cursor()   
        baza.execute('''SELECT DISTINCT "{}" 
                        FROM "GENERAL"
                        WHERE "Group"="{}"
                        ORDER BY NumID'''.format('Version', mo))
        izvedbe = [i[0] for i in baza.fetchall()]
        b.close()
        return izvedbe

    def poisci_velikost(self, mo, iz):
        b = sqlite3.connect(self.pot_baza)
        baza = b.cursor()
        baza.execute('''SELECT DISTINCT "{}" 
                        FROM "GENERAL"
                        WHERE "Group"="{}" AND Version="{}"
                        ORDER BY NumID'''.format('Size', mo, iz))
        velikosti = [i[0] for i in baza.fetchall() if i[0][-1] != 'T']
        b.close()
        return velikosti

    def baza_slovar(self):
        self.enote = defaultdict(list)
        b = sqlite3.connect(self.pot_baza)
        baza = b.cursor()
        for mo in self.poisci_modele():
            for vr in self.poisci_izvedbe(mo):
                self.enote[(mo, iz)] = self.poisci_velikost(mo, iz)
        b.close()


    def baza_slovar_cevni(self):
        self.enote_cevni = defaultdict(list)
        for sk in self.poisci_modele():
            for iz in self.poisci_izvedbe(mo):
                b = sqlite3.connect(self.pot_baza)
                baza = b.cursor()
                baza.execute('''SELECT DISTINCT "{}" 
                        FROM "GENERAL"
                        WHERE "Group"="{}" AND Version="{}"
                        ORDER BY NumID'''.format('Size', mo, iz))
                velikosti = [i[0] for i in baza.fetchall() if i[0][-1] == 'T']
                if velikosti:
                    self.enote_cevni[(mo, iz)] = velikosti
        b.close()