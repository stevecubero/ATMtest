transaccion =(input("Desea anadir entradas a la bitacora? : " ))
listaTransacciones = ("Tipo de transaccion:" "\nD = Deposito" "\nR = Retiro" "\nPROCESAR = Procesar todas las transacciones" )
saldo = int (input ("Digite el saldo inicial del dia en colones: ")) 
conteoDepositos  = 0
conteoRetiros = 0 
saldoDepositos = 0 #Cantidad en colones de depositos
saldoRetiros = 0 #Cantidad en colones de retiros
saldoTotalDepositos = 0 #saldo inicial + cantidad en depositos
saldoRetiros = 0 #saldo inicial + cantidad en retiros'''


if transaccion == "si":
    print (listaTransacciones)
    condicion = " "
    while condicion != "PROCESAR":
        condicion = (input ("Digite el tipo de transaccion que quiere ejecutar. Digite PROCESAR para finalizar y hacer el calculo final: "))
        if condicion == "D": 
            saldoDepositos += int (input("Digite el monto del deposito en Colones "))
            conteoDepositos += 1
            saldoTotalDepositos = saldo + saldoDepositos
        elif condicion == "R":
            saldoRetiros += int (input("Digite el monto del retiro en Colones ")) #Cantidad en colones en retiros
            conteoRetiros += conteoRetiros + 1
            saldoTotalRetiros = saldo + saldoRetiros
        elif condicion == "PROCESAR":
            print ("Las transaciones se van a procesar: ")
            break
        else: 
            print ("La seleccion es incorrecta")


print ("El numero de depositos del dia fueron", conteoDepositos, "y la cantidad en colones de los depositos fue de " , saldoDepositos, "colones")
print ("El numero de retiros del dia fueron ", conteoRetiros , "Y la cantidad de colones total en retiros fue de ", saldoRetiros, " colones")
print ("El saldo total de la cuenta para el dia de hoy es de : " , (saldoTotalDepositos - saldoRetiros), "colones. ")
