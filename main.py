import re
import time
import networkx as nx
from nina_fatehi.Algorithm import *

def read_advogato():
    file_main = open("./DataSet/advogato/advogato_full_reformed.txt", 'r')
    read = file_main.readlines()
    file_main.close()

    advogato = dict()
    for item in read:
        line = re.split('\n',item)[0]
        line = re.split(' ', line)
        if len(line)>1 and line[0] != line[1]:
            advogato[(line[0],line[1])] = float(line[2])

    return advogato

def read_BitCoin():
    file = open("./Data/soc-sign-bitcoinalpha.csv", 'r')
    read = file.readlines()
    file.close()
    trust_values = dict()
    for line in read[1:]:
        items = re.split(',', line)
        trust_values[(items[0],items[1])] = (int(items[2])+10)/20
    return trust_values

if __name__ == '__main__':
    time_base = time.time()
    # advogato = read_advogato()
    # advogato_duplicate = advogato.copy()
    # network = nx.Graph(list(advogato.keys()))

    trust_values = read_BitCoin()
    list_of_keys = list(trust_values.keys())
    trust_values_duplicate = trust_values.copy()
    network = nx.Graph(list(trust_values.keys()))

    number_iteration = 700
    # source = "itamar"
    # target = "carmstro"
    # fatehi_algorithm(network,number_iteration, source, target, advogato)

    trust = dict()
    for item in list(trust_values.keys()):    ##all paths
        # advogato = advogato_duplicate.copy()
        advogato = trust_values_duplicate.copy()
        network = nx.Graph(list(advogato.keys()))

        source = item[0]
        target = item[1]

        print(list(advogato.keys()).index(item),"---- Source:", source, "and Target:", target,"----")

        if source != target:
            t_check = advogato[(source,target)]
            advogato.pop((source,target))

            trust[item] = fatehi_algorithm(network,number_iteration, source, target, advogato)
            print(trust[item], t_check)


        file = open("results_fatehi_temp.txt", 'w')
        for key in trust.keys():
            string = str(key[0])+ " "+ str(key[1]) + " "+ str(trust[key])+ " \n"
            file.writelines(string)
        file.close()

    print("The whole process, from top to bottom, took", (time.time()-time_base)/3600, "hours")
