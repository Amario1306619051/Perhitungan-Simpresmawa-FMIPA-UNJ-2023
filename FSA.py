#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 21:23:25 2023

@author: amariofausta
"""

import pandas as pd
import numpy as np

Data = pd.read_excel('/Users/amariofausta/Downloads/Book3.xlsx')
DataListJuara= Data.Juara
DataNamaMahasiwa = Data.Nama
DataProdi = Data.Prodi
DataTingkat = Data.Tingkat
DataNIM = Data.Nim
ListJuara = []
ListNama = []
ListProdi = []
ListTingkat = []
ListNIM = []

for i in DataListJuara :
    if i == 'Juara III':
        i = 'Juara 3'
    elif i == 'Juara II':
        i = 'Juara 2'
    elif i == 'Juara I':
        i = 'Juara 1'
    elif i.find('erunggu') > 0:
        i = 'Perunggu'
    elif i.find('ronze') > 0:
        i ='Perunggu'
    elif i.find('erak') > 0 :
        i = 'Perak'
    elif i.find('mas') > 0:
        i = 'Emas'
    elif i.find('Juara 1') > -1:
        i = 'Juara 1'
    elif i.find('Juara 2') > -1:
        i = 'Juara 2'
    elif i.find('Juara 3') > -1:
        i = 'Juara 3'
    elif i.find('arapan') > -1 or i.find('avorit') > -1 or i.find('best') > -1 or i.find('Best') > -1:
        i = 'Kategori'
    elif i.find('OP') > -1 or i.find('op 50') > -1:
        i ='Top 50'
    elif i.find('dana') > -1 or i.find('Dana') > -1:
        i ='Didanai'
    elif i.find('finalis') > -1 or i.find('Finalis') > -1:
        i = 'Grand Final'
    elif i.find('eserta') > -1:
        i = 'Peserta'
        
    ListJuara.append(i)

print('Data fixed')
JenisJenisJuara = list(dict.fromkeys(ListJuara))

for i in DataNamaMahasiwa :
    print('Changing.....')
    ListNama.append(i)
    
for i in DataProdi:
    ListProdi.append(i)
    
for i in DataTingkat:
    ListTingkat.append(i)
    
for i in DataNIM:
    ListNIM.append(i)

    
DataBersih = []
for i in range(len(ListJuara)):  
    DataBersih.append([ListNama[i], ListProdi[i], ListJuara[i], ListTingkat[i]])

arr = np.asarray(DataBersih)
pd.DataFrame(arr).to_csv('sample.csv', index_label = "Index", header  = ['Nama','Prodi','Juara','Tingkat']) 


ListSemiFinal = []
ListNamaKapital = [i.upper() for i in ListNama]
JumlahOrangSementara = list(dict.fromkeys(ListNamaKapital))
JumlahOrang = []
Sesat = []
for i in range(0,len(JumlahOrangSementara)-1):
    if JumlahOrangSementara[i].find(JumlahOrangSementara[i+1][:5]) < -0.1:
        JumlahOrang.append(JumlahOrangSementara[i])
    else:
        Sesat.append(JumlahOrangSementara[i])

ListNIMBersih = list(dict.fromkeys(ListNIM))


JumlahOrang.append('AQSATH AULIA PUTRA')
ProgramStudi = 0
HasilAkhir = []
Banner = []
ListPoin = []
for i in range(len(JumlahOrang)):
    poin = 0
    for k in range(len(ListNamaKapital)):
        if JumlahOrang[i].find(ListNamaKapital[k][0:14]) > -0.1 :
            ProgramStudi = k
            if ListTingkat[k] == 'Nasional':
                if ListJuara[k] == 'Juara 1':
                    poin += 30
                elif ListJuara[k] == 'Juara 2':
                    poin += 25
                elif ListJuara[k] == 'Juara 3':
                    poin += 20
                elif ListJuara[k] == 'Kategori':
                    poin += 16
                elif ListJuara[k] == 'Narasumber':
                    poin += 15
                elif ListJuara[k] == 'Emas':
                    poin += 10
                elif ListJuara[k] == 'Perak':
                    poin += 7
                elif ListJuara[k] == 'Perunggu':
                    poin += 5
                elif ListJuara[k] == 'Peserta':
                    poin += 3
                elif ListJuara[k] == 'Didanai':
                    poin += 3
                elif ListJuara[k] == 'Pemilik HaKI':
                    poin += 3
            elif ListTingkat[k]== 'Internasional':
                if ListJuara[k] == 'Juara 1':
                    poin += 50
                elif ListJuara[k] == 'Juara 2':
                    poin += 45
                elif ListJuara[k] == 'Juara 3':
                    poin += 40
                elif ListJuara[k] == 'Kategori':
                    poin += 32
                elif ListJuara[k] == 'Narasumber':
                    poin += 25
                elif ListJuara[k] == 'Emas':
                    poin += 30
                elif ListJuara[k] == 'Perak':
                    poin += 25
                elif ListJuara[k] == 'Perunggu':
                    poin += 20
                elif ListJuara[k] == 'Peserta':
                    poin += 10
                elif ListJuara[k] == 'Didanai':
                    poin += 10
                elif ListJuara[k] == 'Pemilik HaKI':
                    poin += 10
            
    HasilAkhir.append([JumlahOrang[i],ListProdi[ProgramStudi],poin])
    Banner.append([JumlahOrang[i],ListProdi[ProgramStudi]])
    ListPoin.append(poin)
    print('Nama orang :', JumlahOrang[i],', Poin terhitung : ', poin)
    
arr = np.asarray(Banner)
pd.DataFrame(arr).to_csv('Banner.csv', index_label = "Index", header  = ['Nama','Prodi'])

arr = np.asarray(HasilAkhir)
pd.DataFrame(arr).to_csv('HasilAkhir.csv', index_label = "Index", header  = ['Nama','Prodi','Poin'])

my_list = ListPoin
new_list = []

while my_list:
    maximum = my_list[0]  
    for x in my_list:
        if x > maximum:
            maximum = x
    new_list.append(maximum)
    my_list.remove(maximum)    

print('Hasil mengurutkan poin : ')
print(new_list)


l = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]

for i in range(len(l)):
    for j in range(i + 1, len(l)):

        if l[i] < l[j]:
           l[i], l[j] = l[j], l[i]

print(l)

UrutanProdi = []
ListProdi = [i.upper() for i in ListProdi]
ProdiFMIPA = list(dict.fromkeys(ListProdi))

JumlahOrangNol = 0
for i in range(len(new_list)):
    if new_list[i] == 0:
        JumlahOrangNol += 1
        
for i in range(0,len(HasilAkhir)):
    for k in range(i + 1,len(HasilAkhir)):
        
        if HasilAkhir[i][2] < HasilAkhir[k][2]:
            HasilAkhir[i], HasilAkhir[k] = HasilAkhir[k], HasilAkhir[i]

arr = np.asarray(HasilAkhir)
pd.DataFrame(arr).to_csv('Urutan.csv', index_label = "Index", header  = ['Nama','Prodi','Poin'])


HasilAkhir1 = []
for i in range(len(ProdiFMIPA)):
    poin = 0
    for k in range(len(ListProdi)):
        if ProdiFMIPA[i].find(ListProdi[k][0:14]) > -0.1 and ProdiFMIPA[i].find(ListProdi[k][0:14]) < 11 :
            if ListTingkat[k] == 'Nasional':
                if ListJuara[k] == 'Juara 1':
                    poin += 30
                elif ListJuara[k] == 'Juara 2':
                    poin += 25
                elif ListJuara[k] == 'Juara 3':
                    poin += 20
                elif ListJuara[k] == 'Kategori':
                    poin += 16
                elif ListJuara[k] == 'Narasumber':
                    poin += 15
                elif ListJuara[k] == 'Emas':
                    poin += 10
                elif ListJuara[k] == 'Perak':
                    poin += 7
                elif ListJuara[k] == 'Perunggu':
                    poin += 5
                elif ListJuara[k] == 'Peserta':
                    poin += 3
                elif ListJuara[k] == 'Didanai':
                    poin += 3
                elif ListJuara[k] == 'Pemilik HaKI':
                    poin += 3
            elif ListTingkat[k]== 'Internasional':
                if ListJuara[k] == 'Juara 1':
                    poin += 50
                elif ListJuara[k] == 'Juara 2':
                    poin += 45
                elif ListJuara[k] == 'Juara 3':
                    poin += 40
                elif ListJuara[k] == 'Kategori':
                    poin += 32
                elif ListJuara[k] == 'Narasumber':
                    poin += 25
                elif ListJuara[k] == 'Emas':
                    poin += 30
                elif ListJuara[k] == 'Perak':
                    poin += 25
                elif ListJuara[k] == 'Perunggu':
                    poin += 20
                elif ListJuara[k] == 'Peserta':
                    poin += 10
                elif ListJuara[k] == 'Didanai':
                    poin += 10
                elif ListJuara[k] == 'Pemilik HaKI':
                    poin += 10
    HasilAkhir1.append([ProdiFMIPA[i], poin])
    
PRODI1 = "PENDIDIKAN FISIKA"
print(PRODI1.find('PENDIDIKAN FISIKA'))


for i in range(0,len(HasilAkhir1)):
    for k in range(i + 1,len(HasilAkhir1)):
        
        if HasilAkhir1[i][1] < HasilAkhir1[k][1]:
            HasilAkhir1[i], HasilAkhir1[k] = HasilAkhir1[k], HasilAkhir1[i]
            
arr = np.asarray(HasilAkhir1)
pd.DataFrame(arr).to_csv('UrutanProdi.csv', index_label = "Index", header  = ['Prodi','Poin'])