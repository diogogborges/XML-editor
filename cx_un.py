# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 08:43:14 2021

@author: bns
"""

import xml.etree.ElementTree as ET

arquivo = #insert filename

tree = ET.parse(arquivo)
root = tree.getroot()
listaProdutos = []

filtro = "*"
filtro2 = "*"

for child in root.iter(filtro):
    xProd = child.tag
    Prod = child.text
    if xProd == "{http://www.portalfiscal.inf.br/nfe}xProd":
        listaProdutos.append(Prod)
        
i = 0

for child in root.iter(filtro):
    uCom = child.tag
    qCom = child.tag
    if uCom == "{http://www.portalfiscal.inf.br/nfe}uCom":
        child.text = "UN"
    if qCom == "{http://www.portalfiscal.inf.br/nfe}qCom":
        valor = child.text
        print(listaProdutos[i])
        text = str(input("Digite o número de unidades: "))
        child.text = text
        i += 1
        
tree.write("output2.xml")
