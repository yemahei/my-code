from createC1 import createC1
from scanD import scanD
from aprioriGen import aprioriGen
def apriori(dataSet, minSupport=0.5):
    C1 = createC1(dataSet)  # 构建初始候选项集C1
    # D = map( set, dataSet )                                 # 将dataSet集合化，以满足scanD的格式要求
    # D=[var for var in map(set,dataSet)]
    D = [set(var) for var in dataSet]
    L1, suppData = scanD(D, C1, minSupport)  # 构建初始的频繁项集，即所有项集只有一个元素
    L = [L1]  # 最初的L1中的每个项集含有一个元素，新生成的
    k = 2  # 项集应该含有2个元素，所以 k=2

    while (len(L[k - 2]) > 0):
        Ck = aprioriGen(L[k - 2], k)
        Lk, supK = scanD(D, Ck, minSupport)
        suppData.update(supK)  # 将新的项集的支持度数据加入原来的总支持度字典中
        L.append(Lk)  # 将符合最小支持度要求的项集加入L
        k += 1  # 新生成的项集中的元素个数应不断增加
    return L, suppData  # 返回所有满足条件的频繁项集的列表，和所有候选项集的支持度信息
