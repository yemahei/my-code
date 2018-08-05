from aprioriGen import aprioriGen
from calcConf import calcConf

def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.7):
    '''''
        对频繁项集中元素超过2的项集进行合并。
        freqSet(frozenset):频繁项集
        H(frozenset):频繁项集中的所有元素，即可以出现在规则右部的元素
        supportData(dict):所有项集的支持度信息
        brl(tuple):生成的规则
    '''
    m = len(H[0])
    if len(freqSet) > m + 1:  # 查看频繁项集是否足够大，以到于移除大小为 m的子集，否则继续生成m+1大小的频繁项集
        Hmp1 = aprioriGen(H, m + 1)
        Hmp1 = calcConf(freqSet, Hmp1, supportData, brl, minConf)  # 对于新生成的m+1大小的频繁项集，计算新生成的关联规则的右则的集合
        if len(Hmp1) > 1:  # 如果不止一条规则满足要求（新生成的关联规则的右则的集合的大小大于1），进一步递归合并，
            # 这样做的结果就是会有“[1|多]->多”(右边只会是“多”，因为合并的本质是频繁子项集变大，
            # 而calcConf函数的关联结果的右侧就是频繁子项集）的关联结果
            rulesFromConseq(freqSet, Hmp1, supportData, brl, minConf)