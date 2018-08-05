def calcConf(freqSet, H, supportData, brl, minConf=0.7):  # 规则生成与评价
    '''''
        计算规则的可信度，返回满足最小可信度的规则。
        freqSet(frozenset):频繁项集
        H(frozenset):频繁项集中所有的元素
        supportData(dic):频繁项集中所有元素的支持度
        brl(tuple):满足可信度条件的关联规则
        minConf(float):最小可信度
    '''
    prunedH = []
    for conseq in H:
        conf = supportData[freqSet] / supportData[freqSet - conseq]
        if conf >= minConf:
            #print(freqSet - conseq, '-->', conseq, 'conf:', conf)
            brl.append([freqSet - conseq, conseq, conf])
            prunedH.append(conseq)
    return prunedH