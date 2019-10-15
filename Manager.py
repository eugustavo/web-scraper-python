import csv
import re
import urllib.request

#gato-javanes-----------------------------------------------------------------------------------------
fp = urllib.request.urlopen("https://www.peritoanimal.com.br/racas-de-gatos/gato-javanes.html")
mybytes = fp.read()

xml_1 = mybytes.decode("utf-8")
fp.close()

#gato-somali-----------------------------------------------------------------------------------------
fp2 = urllib.request.urlopen("https://www.peritoanimal.com.br/racas-de-gatos/gato-somali.html")
mybytes = fp2.read()

xml_2 = mybytes.decode("utf-8")
fp2.close()

#gato-javanes-----------------------------------------------------------------------------------------
def gatoJavanes(xml_1):
    matchTitle = re.findall(r'>(.*?)</h1>',str(xml_1))
    matchDescr = re.findall(r'<p>(.+?) Essas',str(xml_1))
    matchTitleOrigem = re.findall(r'</span>\n([a-zA-Z]+)\n</div>',str(xml_1))
    matchOrigem = re.findall(r'<li>([a-zA-Z\s?]+)</li>',str(xml_1))
    dados = [matchTitle, matchDescr, matchOrigem]
    return dados

#gato-somali-----------------------------------------------------------------------------------------
def gatoSomali(xml_2):
    matchTitle = re.findall(r'>(.*?)</h1>',str(xml_2))[0]
    matchDescr = re.findall(r'<p>(.+?) Nessa',str(xml_2))[0]
    matchTitleOrigem = re.findall(r'</span>\n([a-zA-Z]+)\n</div>',str(xml_2))[0]
    matchOrigem = re.findall(r'<li>(\w+)</li>',str(xml_2))[0]
    dados = [matchTitle, matchDescr, matchOrigem]
    return dados


gatoJavanes = gatoJavanes(xml_1)
gatoSomali = gatoSomali(xml_2)


with open('raca_de_gatos.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(["Titulo", "Descrição", "Origem"])
    employee_writer.writerow([gatoJavanes[0], gatoJavanes[1], gatoJavanes[2]])
    employee_writer.writerow([gatoSomali[0], gatoSomali[1], gatoSomali[2]])


