############################# HEADER ######################################
#
# razred opis.py
#
# podane vrednosti za tehnične podatke, self.podatki:
#
# Hladilni agregat Climaveneta i-BX M 013
# ***Splošni opis enote***
# PROIZVAJALEC: Mitsubishi Electric... S.p.A, Italija
# UVOZNIK: REAM d.o.o., Trzin
#
# TEHNIČNI PODATKI:
# Hladilna moč:    12,90 kW
# EER (EN14511 metoda):    2,74
# ESEER (EN14511 metoda):    4,69
# SEER (Reg. EU 2016/2281):    4,78
# El. priključek:    230V/ 1F/ 50Hz
# Zvočni tlak (SPL):    39 dB(A)
# Zvočna moč (PWL):    70 dB(A)
# Število hladilnih krogov:    1
# Število kompresorjev:    1
# Dolžina:    900 mm
# Širina:    420 mm
# Višina:    1240 mm
# Teža:    125 kg
# 
###########################################################################

import sqlite3

class ExOpis():
    def __init__(self, ex_productID='i-BX M 013'):
        self.ex_productID = ex_productID
        try:
            self.ex_podatki()
        except:
            print('Napaka pri sestavi opisa')

    def ex_vrednosti(self):
        vrednosti = []
        # povezava na bazo
        b = sqlite3.connect("sqlite\SQL_chiller.db")
        baza = b.cursor()
        baza.execute('''SELECT "Cooling capacity" 
                        FROM COOLING_EUROVENT
                        WHERE productID=?''', (self.ex_productID,))
        vrednosti.append(baza.fetchall()[0][0])
        baza.execute('''SELECT "EER", "ESEER" 
                        FROM COOLING_EUROVENT
                        WHERE productID=?''', (self.ex_productID,))
        for i in baza.fetchall()[0]:
            try:
                ba, de = i.split(',')
                vrednosti.append(ba+','+de[:2])
            except:
                if i:
                    vrednosti.append(i)
                else:
                    vrednosti.append('-')
        baza.execute('''SELECT "SEER"
                        FROM SEASONAL_EFF_COOLING
                        WHERE productID=?''', (self.ex_productID,))
        i = baza.fetchall()[0][0].split(',')
        try:
            ba, de = i
            vrednosti.append(ba+','+de[:2])
        except:
            vrednosti.append('-')
        baza.execute('''SELECT "Total power input" 
                        FROM COOLING_GROSS
                        WHERE productID=?''', (self.ex_productID,))
        baza.execute('''SELECT "Power supply"
                        FROM GENERAL
                        WHERE productID=?''', (self.ex_productID,))
        if '400' in baza.fetchall()[0][0]:
            vrednosti.append('400V/ 3F/ 50Hz')
        else:
            vrednosti.append('230V/ 1F/ 50Hz')
        baza.execute('''SELECT "Sound Pressure", 
                        "Sound power level in cooling", "No. Circuits", "Compressors nr.", "A", "B", "H", "Operating weight"
                        FROM GENERAL
                        WHERE productID=?''', (self.ex_productID,))
        vrednosti.extend([i for i in baza.fetchall()[0]])
        b.close()
        return vrednosti

    def ex_teh_podatki(self):
        """
        Vrni seznam s tehnicnimi postavkami za produkt:
        """
        postavke = [('Hladilna moč', 'kW'), ('EER (EN14511 metoda)', ''), 
        ('ESEER (EN14511 metoda)', ''), ('SEER (Reg. EU 2016/2281)', ''),
        ('El. priključek', ''), ('Zvočni tlak (SPL)', 'dB(A)'), 
        ('Zvočna moč (PWL)', 'dB(A)'), ('Število hladilnih krogov', ''), ('Število kompresorjev', ''), ('Dolžina', 'mm'), ('Širina', 'mm'),('Višina', 'mm'), ('Teža', 'kg')]
        vrednosti = self.ex_vrednosti()
        self.teh_podatki = []
        for pos, vred in zip(postavke, vrednosti):
            self.teh_podatki.append(f'{pos[0]}:    {vred} {pos[1]}')
    
    def ex_podatki(self):
        """
        Sestavi seznam z splošnimi podatki
        """
        self.ostali_podatki = ['Hladilni agregat Climaveneta ' + self.ex_productID, '***Splošni opis enote***', 'PROIZVAJALEC: Mitsubishi Electric Hydronics & IT Cooling Systems S.p.A, Italija',
        'UVOZNIK: REAM d.o.o., Trzin', '', 'TEHNIČNI PODATKI:']
        self.ex_teh_podatki()
        self.podatki = self.ostali_podatki + self.teh_podatki