import csv
import sys

cabecalho_arq_esperado = ['Municipio',
                          'População residente (Pessoas)',
                          'Área da unidade territorial (Quilômetros quadrados)',
                          'Densidade demográfica (Habitante por quilômetro quadrado)'
                          ]

with open('data\censo-demografico-municipios-2022.csv',mode='r',encoding='UTF8') as arq_censo_demo:
    arq_leitor = csv.reader(arq_censo_demo, delimiter=';')
    cabe_arq = next(arq_leitor)
    
    if cabecalho_arq_esperado != cabe_arq:
        
        print(f"Cabeçalho inválido")
        
        sys.exit()
        
    municipios_agrupados = {}
    
    for linha in arq_leitor:
    
        linha_dici = {
            'municipio': linha[0],
            'populacao': int(linha[1]),
            'area_territorial': int(linha[2]),
            'dens_demogra': float(linha[3].replace(',','.'))
        }

        est = linha_dici.get('municipio')[-4:].replace('(','').replace(')','')
        
        if municipios_agrupados.get(est):
            
            municipios_agrupados[est].append(linha_dici)
        else:
            municipios_agrupados[est] = [linha_dici]
            
