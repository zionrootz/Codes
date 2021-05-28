import speedtest
from datetime import datetime
import pandas as pd
from threading import Timer

print('Testando de velocidade de Internet...')
s = speedtest.Speedtest()
velo_down = s.download(threads=None)*(10**-6)
velo_up = s.upload(threads=None)*(10**-6)
print('Velocidade de Download atual: {} Mbps'.format(round(velo_down)))
print('Velocidade de Upload atual: {} Mbps'.format(round(velo_up)))


# função para gravar dados da velocidade da internet em Excel
#def internet():
#    df = pd.read_excel('dados.xlsx', sheet_name='base')
#    s = speedtest.Speedtest()
#    data_atual = datetime.now().strftime('%d/%m/%Y')
#    hora_atual = datetime.now().strftime('%H:%M')
#    velocidade = s.download(threads=None)*(10**-6)
#    df.loc[len(df)] = [data_atual, hora_atual, round(velocidade)]
#    df.to_excel('dados.xlsx', sheet_name='base', index=False)
#    Timer(30,internet).start()
#internet()
