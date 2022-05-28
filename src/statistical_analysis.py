
# function for calculate avg value order max
def statistical_analysis_season_max(list):
    dict = {}
    for elem in list:
        if elem[0] not in dict:
            dict[elem[0]] = []
        dict[elem[0]].append(elem[1:])

    for key in dict:
        for i in zip(*dict[key]):
            dict[key] = (sum(i) / 38)

    sort_list = sorted(dict.items(), key=lambda x: x[1], reverse=True)

    return sort_list


# function for calculate avg value order min
def statistical_analysis_season_min(list):
    dict = {}
    for elem in list:
        if elem[0] not in dict:
            dict[elem[0]] = []
        dict[elem[0]].append(elem[1:])

    for key in dict:
        for i in zip(*dict[key]):
            dict[key] = (sum(i) / 38)

    sort_list = sorted(dict.items(), key=lambda x: x[1])

    return sort_list
