def scanD(D, Ck, minSupport):
    '''''
        计算Ck中的项集在数据集合D(记录或者transactions)中的支持度,
        返回满足最小支持度的项集的集合，和所有项集支持度信息的字典。
    '''
    ssCnt = {}
    for tid in D:  # 对于每一条transaction
        for can in Ck:  # 对于每一个候选项集can，检查是否是transaction的一部分 # 即该候选can是否得到transaction的支持
            if can.issubset(tid):  #issubset 集合操作
                ssCnt[can] = ssCnt.get(can, 0) + 1 #获取键的值
    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key] / numItems  # 每个项集的支持度
        if support >= minSupport:  # 将满足最小支持度的项集，加入retList
            retList.insert(0, key)
        supportData[key] = support  # 汇总支持度数据
    return retList, supportData