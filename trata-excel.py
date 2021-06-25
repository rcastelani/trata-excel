import os
import re
import operator

regioes_global = [
    #LISTA_GLOBAL
]

regioes_gna = [
   #LISTA_GNA
]

regioes_cta = [
    #LISTA_CTA
]


log_path_global = r"docs\teste\global\\"
log_format_global = r"docs\teste\log_format_global.log"

log_path_cta = r"docs\teste\cta\\"
log_format_cta = r"docs\teste\log_format_cta.log"

log_path_gna = r"docs\teste\gna\\"
log_format_gna = r"docs\teste\log_format_gna.log"

log_result = r"docs\teste\total.csv"
# log_total = r"docs\teste\totaltotal.csv"

"""
def sortFile(fileResult,output_result):
    result = open(output_result, "w")
    file = open(fileResult,"r")
    sort = sorted(file,key=operator.itemgetter(0))
    for line in sort:
        print(line,end="",file=result)
    result.close()
"""


def logDir(log_path, output_format):
    output_format = open(output_format, "w")
    files = os.listdir(log_path)
    pattern = "WORKING"
    for file in files:
        for line in open(log_path + file):
            if re.search(pattern, line):
                fields = line.strip().split()
                novo = fields[0]
                format = novo[:-1]
                output_format.write(line.replace(novo, format))
    output_format.close()


def resultGlobal(list, output_result, output_log):
    result = open(output_result, "w")
    # para cada regiao na lista de regioes globais
    for regiao in list:
        # abre o arqivo de log formatado
        arquivo = open(output_log)
        countv5 = 0
        countgw = 0
        for linha in arquivo:
            if regiao in linha:
                if "V5LOOP" in linha:
                    countv5 += 1
                else:
                    countgw += 1
        print(regiao, "V5", countv5, "GW", countgw, sep=";", file=result)
    result.close()


# lista, arquivo resultado, log_formatado, cnl
def resultLocal(list, output_result, output_log, cnl):
    result = open(output_result, "a")
    totalv5 = 0
    totalgw = 0
    for regiao in list:
        # abre o arqivo de log formatado
        arquivo = open(output_log)
        countv5 = 0
        countgw = 0
        for linha in arquivo:
            if regiao in linha:
                if "V5LOOP" in linha:
                    countv5 += 1
                else:
                    countgw += 1
        totalv5 += countv5
        totalgw += countgw
    print(cnl, "V5", totalv5, "GW", totalgw, sep=";", file=result)
    result.close()


# lista, arquivo resultado, log_formatado, cnl
logDir(log_path_global, log_format_global)
resultGlobal(regioes_global, log_result, log_format_global)

logDir(log_path_cta, log_format_cta)
resultLocal(regioes_cta, log_result, log_format_cta, "CTA")

logDir(log_path_gna, log_format_gna)
resultLocal(regioes_gna, log_result, log_format_gna, "GNA")

# sortFile(log_result,log_total)
