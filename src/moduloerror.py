 #!/usr/bin/python
 #!encoding: UTF-8
import sys 
import modulopi

def error(interv,n_test,umbral):
    resta=0.0  
    y = modulopi.PI        
    for i in range(0,n_test):
      x = modulopi.funcion(interv)
      resta = abs(x -y)   
      if resta > umbral:
	print "La aproximacion es : " porcentaje)
      else 
        print "La aproximacion es: " funcion)
	
      return resta
    
if __name__ == "__main__":
   if len(sys.argv) == 4:
      n = int (sys.argv[1])
      m = int (sys.argv[2])
      u = int (sys.argv[3])
   else:
      n = int (raw_input('Introduzca la cantidad de intervalos en los que desea que se aplique la aproximación de pi:'))
      m = int (raw_input ('Introduzca la cantidad de veces que quiere realizarlo: '))  
      u = int (raw_input('Introduzca el valor del umbral:'))