from datetime import datetime
from time import sleep

data=datetime.now()
ano=datetime(year=2021, month=1, day=1)
while(data.year != ano.year):
    print()
    sleep(120)
else:
    print('Instaling all packages...')
    sleep(30)
    print('Done!')
    print('Rebooting System...')
    sleep(15)
    print('Inicializing all services...')
    sleep(10)
    print('Done!')
    print('starting Project Zero...')
    sleep(21)
    print('LINK START!')