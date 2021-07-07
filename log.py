import os
import re

output_format = r"docs\teste\total.csv"

log_path_global = r"docs\teste\global"
log_path_cta01 = log_path_aps01 = log_path_apu01 = log_path_auc01 = log_path_cbx01 = log_path_lda01 = log_path_cab01 = log_path_pni01 = log_path_rla01 = log_path_sjp01 = r"docs\teste\global\CTA01_1706"
log_path_bsa01 = log_path_tag01 = log_path_vpi01 = r"docs\teste\global\BSA01_2206"
log_path_aps02 = log_path_apu02 = log_path_lda02 = r"docs\teste\global\LDA_1706"
log_path_auc05 = log_path_cab05 = log_path_cbx05 = log_path_rla05 = log_path_sjp05 = log_path_pni05 = log_path_cta05 = r"docs\teste\global\CTA05_1706"
log_path_bsa04 = log_path_tag04 = log_path_vpi04 = r"docs\teste\global\BSA04_LNINV_JUNHO2021"
log_path_rjo04 = log_path_nri04 = r"docs\teste\global\RJO04_LNINV_JUNHO2021"
log_path_nri05 = log_path_rjo05 = r"docs\teste\global\RJO05_2506"
log_path_gna = r"docs\teste\gna"

regioes_global = [
   ###
]

regioes_cta01 = [
   ###
]

regioes_cta05 = [
###
]

regioes_gna = [
    ###
]

regioes_aps01 = regioes_aps02 = ["APS"]
regioes_apu01 = regioes_apu02 = ["APU"]
regioes_auc01 = regioes_auc05 = ["AUC"]
regioes_bsa01 = regioes_bsa04 = ["BSA"]
regioes_cab01 = regioes_cab05 = ["CAB"]
regioes_cbx01 = regioes_cbx05 = ["CBX"]
regioes_lda01 = regioes_lda02 = ["LDA"]
regioes_nri04 = regioes_nri05 = ["NRI"]
regioes_pni01 = regioes_pni05 = ["PNI"]
regioes_rjo04 = regioes_rjo05 = ["RJO"]
regioes_rla01 = regioes_rla05 = ["RLA"]
regioes_sjp01 = regioes_sjp05 = ["SJP"]
regioes_tag01 = regioes_tag04 = ["TAG"]
regioes_vpi01 = regioes_vpi04 = ["VPI"]


def ListDir(log_path):
    arr = []
    for path, subdirs, files in os.walk(log_path):
        for name in files:
            arr.append(os.path.join(path, name))
            # return os.path.join(path,name)
    return arr

def CarregaArquivo(log_path):
    pattern = "WORKING"
    linhas = []
    file = open(log_path)
    for files in file:
        if re.search(pattern, files):
            fields = files.strip().split()
            novo = fields[0]
            format = novo[:-1]
            linhas.append(files.replace(novo, format))
    return linhas

#def ReadFile(listaDePaths):
#    pattern = "WORKING"
#    linhas = []
#    for path in listaDePaths:
#        fullpath = open(path)
#        for files in fullpath:
#            if re.search(pattern, files):
#                linhas.append(files)
#    return linhas

def ReadFile(listaDePaths):
    pattern = "WORKING"
    linhas = []
    for path in listaDePaths:
        fullpath = open(path)
        for files in fullpath:
            if re.search(pattern, files):
                fields = files.strip().split()
                novo = fields[0]
                format = novo[:-1]
                linhas.append(files.replace(novo, format))
    return linhas

def FiltraLinhas(linhas, regioes, cnl, output_format):
    output_format = open(output_format, "a")
    count_v5 = 0
    count_gw = 0
    for regiao in regioes:
        countv5 = 0
        countgw = 0
        for linha in linhas:
            if regiao in linha:
                if "V5LOOP" in linha:
                    countv5 += 1
                else:
                    countgw += 1
        count_v5 += countv5
        count_gw += countgw
        # print(regiao[:3], "V5: ", countv5, "GW; ", countgw)
    print(cnl, "V5", count_v5, "GW", count_gw, sep=";", file=output_format)
    output_format.close()


def FiltraLinhasGlobal(linhas, regioes, output_format):
    output_format = open(output_format, "a")
    for regiao in regioes:
        countv5 = 0
        countgw = 0
        for linha in linhas:
            if regiao in linha:
                if "V5LOOP" in linha:
                    countv5 += 1
                else:
                    countgw += 1
        print(regiao, "V5 ", countv5, "GW ", countgw, sep=";", file=output_format)
    output_format.close()

FiltraLinhasGlobal(ReadFile(ListDir(log_path_global)), regioes_global, output_format)
FiltraLinhas(ReadFile(ListDir(log_path_gna)), regioes_gna, "GNA", output_format)
FiltraLinhas(CarregaArquivo(log_path_cta01), regioes_cta01, "CTA01", output_format)
FiltraLinhas(CarregaArquivo(log_path_cta05), regioes_cta05, "CTA05", output_format)
FiltraLinhas(CarregaArquivo(log_path_aps01), regioes_aps01, "APS01", output_format)
FiltraLinhas(CarregaArquivo(log_path_aps02), regioes_aps02, "APS02", output_format)
FiltraLinhas(CarregaArquivo(log_path_apu01), regioes_apu01, "APU01", output_format)
FiltraLinhas(CarregaArquivo(log_path_apu02), regioes_apu02, "APU02", output_format)
FiltraLinhas(CarregaArquivo(log_path_auc01), regioes_auc01, "AUC01", output_format)
FiltraLinhas(CarregaArquivo(log_path_auc05), regioes_auc05, "AUC05", output_format)
FiltraLinhas(CarregaArquivo(log_path_bsa01), regioes_bsa01, "BSA01", output_format)
FiltraLinhas(CarregaArquivo(log_path_bsa04), regioes_bsa04, "BSA04", output_format)
FiltraLinhas(CarregaArquivo(log_path_cab01), regioes_cab01, "CAB01", output_format)
FiltraLinhas(CarregaArquivo(log_path_cab05), regioes_cab05, "CAB05", output_format)
FiltraLinhas(CarregaArquivo(log_path_cbx01), regioes_cbx01, "CBX01", output_format)
FiltraLinhas(CarregaArquivo(log_path_cbx05), regioes_cbx05, "CBX05", output_format)
FiltraLinhas(CarregaArquivo(log_path_lda01), regioes_lda01, "LDA01", output_format)
FiltraLinhas(CarregaArquivo(log_path_lda02), regioes_lda02, "LDA02", output_format)
FiltraLinhas(CarregaArquivo(log_path_nri04), regioes_nri04, "NRI04", output_format)
FiltraLinhas(CarregaArquivo(log_path_nri05), regioes_nri05, "NRI05", output_format)
FiltraLinhas(CarregaArquivo(log_path_pni01), regioes_pni01, "PNI01", output_format)
FiltraLinhas(CarregaArquivo(log_path_pni05), regioes_pni05, "PNI05", output_format)
FiltraLinhas(CarregaArquivo(log_path_rjo04), regioes_rjo04, "RJO04", output_format)
FiltraLinhas(CarregaArquivo(log_path_rjo05), regioes_rjo05, "RJO05", output_format)
FiltraLinhas(CarregaArquivo(log_path_rla01), regioes_rla01, "RLA01", output_format)
FiltraLinhas(CarregaArquivo(log_path_rla05), regioes_rla05, "RLA05", output_format)
FiltraLinhas(CarregaArquivo(log_path_sjp01), regioes_sjp01, "SJP01", output_format)
FiltraLinhas(CarregaArquivo(log_path_sjp05), regioes_sjp05, "SJP05", output_format)
FiltraLinhas(CarregaArquivo(log_path_tag01), regioes_tag01, "TAG01", output_format)
FiltraLinhas(CarregaArquivo(log_path_tag04), regioes_tag04, "TAG04", output_format)
FiltraLinhas(CarregaArquivo(log_path_vpi01), regioes_vpi01, "VPI01", output_format)
FiltraLinhas(CarregaArquivo(log_path_vpi04), regioes_vpi04, "VPI04", output_format)