# Importar pydrs
import pydrs

# Conectar interface serial
drs = pydrs.SerialDRS()
drs.Connect('/dev/ttyUSB0',115200)
 

# Configura quantidade de placas HRADC
#drs.Config_nHRADC(num_placas) 
numero_placas = input("Entre com o numero de placas no bastidor: ")
drs.Config_nHRADC(int(numero_placas))


# Atualizar memória do HRADC# id_hradc: 0 à 3
#drs.UpdateHRADC_BoardData(id_hradc)

for i in range(int(numero_placas)):

    print('\n##Placa:',i,'##\n')
    drs.UpdateHRADC_BoardData(i)

