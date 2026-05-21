def convertUnit(lenMn):

    unitDic = {}

    unitDic['cm'] = lenMn * .1
    unitDic['m'] = lenMn * .001
    unitDic['inch'] = lenMn * .03937
    unitDic['ft'] = lenMn * .003281

    return unitDic