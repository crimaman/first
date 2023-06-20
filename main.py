def func7(arg33, arg34):
    var38 = func8(arg33, arg34)
    var51 = func10(arg33, var38)
    var52 = arg34 ^ arg33
    var53 = arg34 ^ (324 | (arg34 & var51 & arg34 + 1593370165) ^ (((var51 + (var38 | (arg34 - 257818463 & arg34 ^ 12 & var38 | arg34))) & 862952252 & var38 - arg33 - 84) + arg34 - arg34) ^ arg34) - 1289575261
    var54 = var38 | (arg33 + (var53 & var53 - 903283786 ^ ((358 ^ var38 - (var51 + (var53 - arg33)) - var38) | ((534 | arg34) - arg34)) ^ (((var51 + var53) - -2136194734) - var52 | var53) & var53 ^ -473 | arg33))
    var55 = arg33 + var52 | ((var38 + arg33 & (1409011794 + 787 | var52 & (var52 ^ (var52 + (arg34 & var53))))) & var51 & arg33 + var51 | (1980677426 | arg33) & (var53 ^ var51) + var54 ^ 1539244798) & var54 | 92044385
    result = -1858975048 - -1917243751 ^ var38 - arg33
    return result
def func10(arg39, arg40):
    var41 = 510 + arg40
    var42 = 327 ^ (var41 ^ -2075768791 | arg40)
    var43 = (var42 - (497 - -441826618)) + 22
    var44 = ((var43 + var43) + arg39) | 259
    var45 = ((var42 ^ -944540647) + -683) ^ arg39
    var46 = (var41 + var43 - 610641838) ^ arg39
    var47 = var42 - arg39
    if arg39 < var42:
        var48 = -645 + 246 - arg40
    else:
        var48 = var43 + var47
    var49 = (var42 | (var44 - arg40)) + arg39
    var50 = (var44 + -12535331) & var46
    result = (((var45 | var43) - (var50 - var46 & var43 + -239 + var47) | -921 - arg39 | var41) + arg39) + var44
    return result
def func1(arg1, arg2):
    var6 = func2(arg1, arg2)
    var7 = func6()
    var8 = ((var6 + arg2) - var6) - arg2
    if arg1 < var6:
        var9 = var8 | ((var6 | var8) | -1652201041)
    else:
        var9 = (arg1 | var7) | arg1
    var10 = var6 | -991
    var11 = -294 + -490 - 1539689310 & var8
    var12 = arg2 | (arg1 - var8 ^ arg1)
    var13 = var7 & (var12 | var11)
    var14 = arg2 ^ (var8 ^ var6) - var10
    var15 = var14 ^ var12 ^ var10 + var8
    if arg1 < var6:
        var16 = var6 - var15 + var13 - var12
    else:
        var16 = 202851397 - (var10 + var8 + var8)
    var17 = (-1378328269 | var7) + var13 ^ var10
    var18 = ((var6 - var7) | var15) + 923519521
    var19 = -86024924 + arg2 ^ var14
    var20 = arg1 - var11
    var21 = var7 + (arg2 - var12)
    if var14 < var6:
        var22 = var12 & var21 - var18 + var17
    else:
        var22 = var21 + var8
    var23 = (var13 & var18) | var18
    var24 = var10 - var19 | arg1 - var20
    if var17 < var8:
        var25 = (var24 - var10) - var11 & var8
    else:
        var25 = (var7 & var24 | var19) | var11
    var26 = (var21 + var7) ^ -974 ^ var10
    var27 = var10 + var26
    var28 = var14 & 999091958 + var14 ^ var20
    var29 = 894 | var7
    var30 = var27 | (var28 - arg1) + var23
    var31 = var8 + (var19 | var26 + var14)
    var32 = (var15 | var28 | var31) ^ var30
    result = var8 ^ arg1
    return result
def func6():
    func4()
    result = len([(7 & (((2 - (((-7 & (-4 ^ 2) ^ 0) + 2) - 2) - 7) | 2) + -2)) ^ -4 for i in xrange(8)])
    func5()
    return result
def func5():
    global len
    del len
def func4():
    global len
    len = lambda x : 9
def func2(arg3, arg4):
    def func3(acc, rest):
        var5 = -8 + 0
        if acc == 0:
            return var5
        else:
            result = func3(acc - 1, var5)
            return result
    result = func3(10, 0)
    return result
def func8(arg35, arg36):
    def func9(acc, rest):
        var37 = 0 & 0
        if acc == 0:
            return var37
        else:
            result = func9(acc - 1, var37)
            return result
    result = func9(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 3'
    print 'func_number: 7'
    print 'arg_number: 33'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
    print 'prog_size: 5'
    print 'func_number: 11'
    print 'arg_number: 56'
    for i in xrange(25000):
        x = 5
        x = func7(x, i)
        print x,
