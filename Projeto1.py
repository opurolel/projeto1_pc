import math
import random
import datetime
import statistics as stats
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
#ENTRADAS
capital = float(input('Capital inicial: '))
aporte = float(input('Aporte Mensal: '))
meses = int(input('Prazo (meses): '))
cdi_anual = float(input('CDI anual (%): ')) / 100
perc_cdb = float(input('Percentual do CDI (%): ')) / 100
perc_lci = float(input('Percentual do LCI (%): ')) / 100
taxa_fii = float(input('Rentabilidade mensal FII (%): ')) / 100
meta = float(input('Meta financeira (R$): '))

#CONVERSÃO CDI
cdi_mensal = math.pow((1+cdi_anual), 1/12) -1

#TOTAL INVESTIDO
total_investido = capital + (aporte * meses)

#CDB
taxa_cdb = cdi_mensal * perc_cdb
montante_cdb = (capital * math.pow((1+taxa_cdb), meses) + (aporte * meses))
lucro_dbc = montante_cdb - total_investido
montante_cdb_liquido = total_investido + (lucro_dbc * 0.85)

#LCI
taxa_lci = cdi_mensal * perc_lci
montante_lci = (capital * math.pow((1 + taxa_lci), meses) + (aporte * meses))

#POUPANÇA
taxa_poupança = 0.005
montante_poupança = (capital * math.pow((1 + taxa_poupança), meses) + (aporte * meses))

#FII - SIMULAÇÕES
montante_fii = (capital * math.pow((1 + taxa_fii), meses) + (aporte * meses))

variação1 = montante_fii * (1 + random.uniform(-0.03, 0.03))
variação2 = montante_fii * (1 + random.uniform(-0.03, 0.03))
variação3 = montante_fii * (1 + random.uniform(-0.03, 0.03))
variação4 = montante_fii * (1 + random.uniform(-0.03, 0.03))
variação5 = montante_fii * (1 + random.uniform(-0.03, 0.03))

variacoes = [variação1, variação2, variação3, variação4, variação5]
media_fii = stats.mean(variacoes)
mediana_fii = stats.median(variacoes)
desvio_fii = stats.stdev(variacoes)

#Prazo de resgate
agora = datetime.datetime.now().date()
resgate = agora + datetime.timedelta(days = meses * 30)
meta_atingida = {True: True, False: False}[media_fii >= meta]

print(f"""
{'='*40}
{'PyInvest - Simulador de Investimentos':^40}
{'='*40}
Data da simulação: {agora.strftime("%d/%m/%Y")}
Data estimada de resgate: {resgate.strftime("%d/%m/%Y")}
{'='*40}

Total investido: {locale.currency(total_investido, grouping=True)}

{'--- RESULTADOS FINANCEIROS ---'}
CDB: {locale.currency(montante_cdb, grouping=True)}
[{'█' * int(montante_cdb / 1000)}]

LCI/LCA: {locale.currency(montante_lci, grouping=True)}
[{'█' * int(montante_lci / 1000)}]

Poupança: {locale.currency(montante_poupança, grouping=True)}
[{'█' * int(montante_poupança / 1000)}]

FII (média): {locale.currency(media_fii, grouping=True)}
[{'█' * int(media_fii / 1000)}]

--- ESTATÍSTICAS FII ---
Mediana: {locale.currency(mediana_fii, grouping=True)}
Desvio padrão: {locale.currency(desvio_fii, grouping=True)}

Meta atingida? {meta_atingida}
""")