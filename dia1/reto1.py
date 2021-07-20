while True:
  print("=========================================")
  print("=======Bienvenido al juego===============")
  print("usted debe elegir una de las opciones:")
  print("1 es piedra")
  print("2 es papel")
  print("3 es tijera")
    
  try:
      a=int(input("ingrese su opcion: ..."))
  except ValueError:
      print("=====> ¡¡¡¡¡¡¡ No existe esa opcion, intentalo nuevamente !!!!!!!!!!!!!!!")
      continue
  
  jugadorA=""
  if a==1:    
      jugadorA="piedra"
  elif a==2:
      jugadorA="papel"
  elif a==3:
      jugadorA="tijera"
  else:
      print("=====> ¡¡¡¡¡¡¡ No existe esa opcion: ", jugadorA , ",  intentalo nuevamente !!!!!!!!!!!!!!!")
      continue
      
      
  print("Usted eligio: ", jugadorA)
  
  import random
  b=random.randint(1,3)
  jugadorB=""
  if b==1:    
      jugadorB="piedra"
  elif b==2:
      jugadorB="papel"
  elif b==3:
      jugadorB="tijera"
  print("La maquina eligio:", jugadorB)
  
  
  ganador=0
  if a==1 and b==2:
      ganador=b
  elif a==2 and b==1:
      ganador=a
  elif a==2 and b==3:
      ganador=b
  elif a==3 and b==2:
      ganador=a
  elif a==3 and b==1:
      ganador=b
  elif a==1 and b==3:
      ganador=1
  elif a==1 and b==2:
      ganador=b
  
  if ganador==a:    
      print("============================================================")
      print(" =====> ¡¡¡¡¡¡¡  Resultado: gana " , jugadorA , "***** usted es ganador ******")
      print("============================================================")      
  elif ganador==b:    
      print("============================================================")
      print(" =====> ¡¡¡¡¡¡¡  Resultado: gana " , jugadorB , "***** Maquina es ganador ******")
      print("============================================================")
  else:
      print("============================================================")
      print(" =====> ¡¡¡¡¡¡¡  Resultado: ***** Esto es empate, intentelo nuevamente ******")
      print("============================================================")
      continue

  print("================================================================")
  print("Desea jugar otra vez: escriba si para continuar")
  c=input()
  if c=="si":
      continue
  else:
      print("Usted finalizo el juego")
      break




  

