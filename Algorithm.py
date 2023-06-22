import networkx as nx
import random

def fatehi_algorithm(network, iterations, source_node, target_node, trust_values):
    ## reward and penalty parameters
    a = 0.009
    b = 0.00009
    R = 5

    total_neighbors = set()
    for node in network:
        total_neighbors = total_neighbors.union(nx.neighbors(network, node))

    ## Phase 1: Constructing DLA Isomorphic to Trust Network
    Automatas = dict()
    action_set = dict()
    action_prob = dict()
    reward = dict()
    W_i = dict()
    for node in network.nodes:
        Automatas[node] = 0
        action_set[node] = list(nx.neighbors(network, node))
        # temp = dict()
        # for item in action_set[node]:
        #     temp[item] = 1/len(action_set[node])
        # action_prob[node] = temp
        action_prob[node] = 1/len(total_neighbors)
        W_i[node] = 0
        reward[node] = 0

    k_n = sum(action_prob.values())

    ## Phase 2: Learning Reliability of Direct Trust Values
    n_r = 0
    k = -1
    path = []
    while k < iterations:
        k += 1
        path = []
        v_k = source_node
        # A_k = Automatas[v_k]
        path.append(source_node)
        Automatas[v_k] = 1

        available_actions = list(action_set[v_k])
        while (not len(available_actions)) or (v_k in action_set[target_node]):
            available_actions = list(action_set[v_k])
            intersection = set(available_actions).intersection(set(path))
            if len(intersection):
                for item in intersection:
                    set(available_actions).remove(item)

            if len(available_actions):
                if v_k == source_node:
                    index = random.randint(0, len(available_actions) - 1)
                    v_k = available_actions[index]
                    path.append(v_k)
                    Automatas[v_k]=1
                else:
                    # values = list(action_prob[v_k].values())
                    # keys = list(action_prob[v_k].keys())
                    # max_p = max(values)
                    # for i in range(len(keys)):
                    #     if (values[i] >= max_p) and (not i in path):
                    #         v_k=i
                    #         print(v_k, path)
                    # path.append(v_k)
                    # Automatas[v_k] = 1
                    temp = dict()
                    keys = list(action_set[v_k])
                    for i in keys:
                        if not i in path:
                            temp[i] = action_prob[i]
                    max_value = max(temp.values())
                    v_k = list(temp.keys())[list(temp.values()).index(max_value)]
                    path.append(v_k)
                    Automatas[v_k] = 1

            ST_sk = 1
            for i in range(0, len(path)-1):
                key = (path[i],path[i+1])
                if key in trust_values.keys():
                    if trust_values[key] <= ST_sk:
                        ST_sk = trust_values[key] #min strategy
                    # ST_sk *= trust_values[key] #multi strategy

            if (v_k in action_set[target_node]) and ST_sk >= W_i[v_k]: ##Favorable
                for n in path:
                    reward[n] = reward[n] + a
                    action_prob[n] = action_prob[n] + a*(1-action_prob[n])
                    if n!=v_k: #j!=i
                        action_prob[n] = (1-a) * action_prob[n]
                W_i[v_k] = ST_sk
                n_r += 1
            else:
                for n in path:   #Punishment
                    reward[n] = reward[n] - b
                    action_prob[n] = (1-b) * action_prob[n]
                    if n!=v_k: #j!=i
                        action_prob[n] = (b/(reward[n]-1)) + (1-b) * action_prob[n]
                n_r = 0

            k_n = sum(action_prob.values())
            for p in action_prob:
                action_prob[p] = action_prob[p]/k_n

    ## Phase3.Aggregating Direct Trust Values
    part_1 = 0
    part_2 = 0
    for item in W_i:
        if W_i[item]:
            key = (item, target_node)
            part_2 += W_i[item]
            if key in trust_values.keys():
                part_1 += (W_i[item]*trust_values[key])

    final_trust_value = part_1/part_2
    return final_trust_value
