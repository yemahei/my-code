import csv
def loadDataSet():
    '''''创建一个用于测试的简单的数据集'''
    with open("F:/mysite/media/myFile.name", "r") as f:
        li = []
        reader = csv.reader(f)
        for row in reader:
            li.append(row)
    return li