import urllib2
from lxml import etree


def getTemperatura(dia):
    return {dia.xpath('temperatura')[0][0].tag : dia.xpath('temperatura')[0][0].text or '', dia.xpath('temperatura')[0][1].tag : dia.xpath('temperatura')[0][1].text or ''}
    

def getSensTermica(dia):
    return {dia.xpath('sens_termica')[0][0].tag : dia.xpath('sens_termica')[0][0].text or '', dia.xpath('sens_termica')[0][1].tag : dia.xpath('sens_termica')[0][1].text or ''}

def getHumedadRelativa(dia):
    return {dia.xpath('humedad_relativa')[0][0].tag : dia.xpath('humedad_relativa')[0][0].text or '', dia.xpath('humedad_relativa')[0][1].tag : dia.xpath('humedad_relativa')[0][1].text or ''}


def getProbPrec(dia):
    
    hiz = {}
    for datu in dia.xpath('prob_precipitacion'):
        if (datu.get('periodo')):
            hiz[datu.get('periodo')] = datu.text or ''
        else:
            hiz['00-24'] = datu.text or ''

    return hiz

def getCotaNieveProb(dia):
   
    hiz = {}
    for datu in dia.xpath('cota_nieve_prov'):
        if (datu.get('periodo')):
            hiz[datu.get('periodo')] = datu.text or ''
        else:
            hiz['00-24'] = datu.text or ''

    return hiz

def getEstadoCielo(dia):
    hiz = {}
    for datu in dia.xpath('estado_cielo'):
        if (datu.get('periodo')):
            hiz[datu.get('periodo')] = { 'valor': datu.text or '' , 'descripcion': datu.get('descripcion')}
        else:
            hiz['00-24'] = { 'valor': datu.text or '' , 'descripcion': datu.get('descripcion')}

    return hiz


def getRachaMax(dia):
    
    hiz = {}
    for datu in dia.xpath('racha_max'):
        if (datu.get('periodo')):
            hiz[datu.get('periodo')] = datu.text or ''
        else:
            hiz['00-24'] = datu.text or ''

    return hiz 
    
def getUvMax(dia):
    if (dia.xpath('uv_max')):
        return dia.xpath('uv_max')[0].text or ''
    else:
        return ''

def getViento(dia):
    hiz = {}
    for datu in dia.xpath('viento'):
        if (datu.get('periodo')):
            hiz[datu.get('periodo')] = {datu[0].tag : datu[0].text or '', datu[1].tag:datu[1].text or ''}
        else:
            
            hiz['00-24'] = {datu[0].tag : datu[0].text or '', datu[1].tag:datu[1].text or ''}
    return hiz


def parseXML(url):
    
    URL_aemet = url 

    doc_aemet = etree.parse(URL_aemet).getroot()
    
    dias = doc_aemet.xpath('//prediccion')[0].getchildren()  
  
    dias_parsed = []

    for dia in dias:
        dia_hiz = {}
        dia_hiz['temperatura'] = getTemperatura(dia)
        dia_hiz['sens_termica'] = getSensTermica(dia)
        dia_hiz['humedad_relativa'] = getHumedadRelativa(dia)    
        dia_hiz['prob_prec'] = getProbPrec(dia)
        dia_hiz['cota_nieve_prob'] = getCotaNieveProb(dia)
        dia_hiz['estado_cielo'] = getEstadoCielo(dia)
        dia_hiz['racha_max'] = getRachaMax(dia)
        dia_hiz['uv_max'] = getUvMax(dia)
        dia_hiz['viento'] = getViento(dia)        
        dia_hiz['fecha'] = dia.get('fecha')
        dias_parsed.append(dia_hiz)
    
    return dias_parsed
