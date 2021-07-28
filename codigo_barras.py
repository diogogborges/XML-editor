# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 09:10:09 2021

@author: bns
"""
import xml.etree.ElementTree as ET

arquivo = "Fitness Brasil - Bioklein NF 1450 - 08-07-2021.xml"

tree = ET.parse(arquivo)
root = tree.getroot()
listaProdutos = []

filtro = "*"

for child in root.iter(filtro):
    xProd = child.tag
    Prod = child.text
    if xProd == "{http://www.portalfiscal.inf.br/nfe}xProd":
        listaProdutos.append(Prod)
        
i = 0

for child in root.iter(filtro):
    cEAN = child.tag
    text = child.text
    if cEAN == "{http://www.portalfiscal.inf.br/nfe}cEAN":
        print(listaProdutos[i])
        text = str(input("Digite o código de barras: "))
        child.text = text
        i += 1
        
tree.write("output.xml")
    
