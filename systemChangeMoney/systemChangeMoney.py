# EJEMPLO DE WEBSCRAPPING CON PYTHON
from bs4 import BeautifulSoup
import requests

from datetime import date
from datetime import datetime
 
import os
salir='no'
while(salir == 'no'):
   os.remove("cambioActual.txt")
   
   print('*' *50)
   print('El sistema mostrara las conversion en:')
   print('*' *50)
   print('=>Dólar de N.A.')
   print('=>Libra Esterlina')
   print('=>Peso Mexicano')
   print('=>Euro')
   print('*' *50)
   miMonto=input('Ingresa monto en soles a convertir: ')
   print('*' *50)
   print('Mostrando el tipo de cambio para HOY')
   
   listaCambios=[] 
   url = requests.get(
       "https://www.sbs.gob.pe/app/pp/sistip_portal/paginas/publicacion/tipocambiopromedio.aspx")
   
   status_code = url.status_code
   if status_code == 200:
       fa = open('historiaCambios.txt','a')
       fb = open('cambioActual.txt','a')
       
       html = BeautifulSoup(url.text, "html.parser")    
       empresas = html.find_all('tr', {'class': 'rgRow'})
       i=1
       for empresa in empresas:        
           moneda = empresa.find('td', {'class': 'APLI_fila3'})
           tipocambio = empresa.find('td', {'class': 'APLI_fila2'})   
           stringMoneda=str(moneda)
           stringTipocambio=str(tipocambio) 
           if stringMoneda.find('COMPRA') == -1:
               if stringMoneda.find('VENTA') == -1:
                  if stringMoneda.find('None') == -1:   
                     monedaList=stringMoneda[stringMoneda.index('%')+3:stringMoneda.index('</td')]       
                     tipocambioList=stringTipocambio[stringTipocambio.index('%')+3:stringTipocambio.index('</td')]         
                     now = datetime.now()
                     format = now.strftime('%d-%m-%Y %H:%M')    
                     # carga historial                       
                     fa.write(monedaList + "," + tipocambioList + "," + format + '\n')  
                     # carga data actual          
                     fb.write(monedaList + "," + tipocambioList + "," + miMonto + '\n')    
                     # listando el tipo de cambio
                     print(str(i) + "-" + monedaList + " ==> " + tipocambioList)
                     listaCambios= str(i) + "-" + monedaList + " ==> " + tipocambioList + '\n'
                     i+=1
       fa.close() 
       fb.close()                
   else:
       print("error nro" + str(status_code))
       
   print('*'*50)
   print('Mostrando Resultado de la conversion')
   print('*'*50)
   fr = open('cambioActual.txt','r')
   montoFinal = fr.read()
   resultados=[]
   resultados = montoFinal.splitlines()
   
   for objCambio in resultados:
       lstObjAlumno = objCambio.split(',')
       print('En ',lstObjAlumno[0], 'tu conversion es ', float(miMonto)/float(lstObjAlumno[1])) 
   fr.close()
   print('*'*50)
   print('Desea salir del programa si/no')
   salir=input()

