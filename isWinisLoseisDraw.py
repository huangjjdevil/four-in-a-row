def isWin( gameState ):
    # 参数当前状态gameState
    # 返回bool类型，是否我们胜利（我们为在棋盘上为0）
    # 还可以改进比如剩余距离和当前连在一起数量小于4，可不查！
    column = False #代表竖着的是否有四个连着的0
    for i in range(7) :#i代表列
        j = 5 
        number_continuuum = 0 #连着0的数量
        while j >= 0 and number_continuuum < 4 : 
            if gameState["Board"][j][i]== 0 :
                number_continuuum += 1
                j -= 1 
            else : 
                number_continuuum = 0
                j -= 1 
        if number_continuuum == 4 : #只检查4个
            column = True
            break

    row = False #代表横着的是否有四个连着的0
    for j in range(5, 0, -1) :#j代表行
        i = 0
        number_continuuum = 0 #连着0的数量
        while i < 7 and number_continuuum < 4 : 
            if gameState["Board"][j][i] == 0 :
                number_continuuum += 1
                i += 1 
            else : 
                number_continuuum = 0
                i += 1 
        if number_continuuum == 4 : #只检查4个
            row = True
            break

    biasl = False #代表携着的是否有四个连着的0,端点在0列的
    for k in range(6) :#k代表可行的斜线
        l = 6 - max( 5 - k , k - 0 ) #代表第k个斜线的长度
        m = 0 
        number_continuuum = 0 #连着0的数量
        if  k < 3 :
            while m < l and number_continuuum < 4 : 
                if gameState["Board"][k+m][m] == 0 :
                    number_continuuum += 1
                    m += 1 
                else : 
                    number_continuuum = 0
                    m += 1 
            if number_continuuum == 4 : #只检查4个
                biasl = True
                break
        else :
            while m < l and number_continuuum < 4 : 
                if gameState["Board"][k-m][m] == 0 :
                    number_continuuum += 1
                    m += 1 
                else : 
                    number_continuuum = 0
                    m += 1 
            if number_continuuum == 4 : #只检查4个
                biasl = True
                break
    
    biasr = False #代表携着的是否有四个连着的0,端点在6列的
    for k in range(6) :#k代表可行的斜线
        l = 6 - max( 5 - k , k - 0 ) #代表第k个斜线的长度
        m = 0 
        number_continuuum = 0 #连着0的数量
        if  k < 3 :
            while m < l and number_continuuum < 4 : 
                if gameState["Board"][k+m][6-m] == 0 :
                    number_continuuum += 1
                    m += 1 
                else : 
                    number_continuuum = 0
                    m += 1 
            if number_continuuum == 4 : #只检查4个
                biasr = True
                break
        else :
            while m < l and number_continuuum < 4 : 
                if gameState["Board"][k-m][6-m] == 0 :
                    number_continuuum += 1
                    m += 1 
                else : 
                    number_continuuum = 0
                    m += 1 
            if number_continuuum == 4 : #只检查4个
                biasr = True
                break
    
    win = column or row or biasl or biasr 
    return win


def isLose( gameState ):
    # 参数当前状态gameState
    # 返回bool类型，是否对方赢（对方在棋盘上为1）
    # 还可以改进比如剩余距离和当前连在一起数量小于4，可不查！
    column = False #代表竖着的是否有四个连着的1
    for i in range(7) :#i代表列
        j = 5 
        number_continuuum = 0 #连着0的数量
        while j >= 0 and number_continuuum < 4 : 
            if gameState["Board"][j][i] == 1 :
                number_continuuum += 1
                j -= 1 
            else : 
                number_continuuum = 0
                j -= 1 
        if number_continuuum == 4 : #只检查4个
            column = True
            break

    row = False #代表横着的是否有四个连着的0
    for j in range(5, 0, -1) :#j代表行
        i = 0
        number_continuuum = 0 #连着0的数量
        while i < 7 and number_continuuum < 4 : 
            if gameState["Board"][j][i] == 1 :
                number_continuuum += 1
                i += 1 
            else : 
                number_continuuum = 0
                i += 1 
        if number_continuuum == 4 : #只检查4个
            row = True
            break

    biasl = False #代表携着的是否有四个连着的1,端点在0列的
    for k in range(6) :#k代表可行的斜线
        l = 6 - max( 5 - k , k - 0 ) #代表第k个斜线的长度
        m = 0 
        number_continuuum = 0 #连着0的数量
        if  k < 3 :
            while m < l and number_continuuum < 4 : 
                if gameState["Board"][k+m][m] == 1 :
                    number_continuuum += 1
                    m += 1 
                else : 
                    number_continuuum = 0
                    m += 1 
            if number_continuuum == 4 : #只检查4个
                biasl = True
                break
        else :
            while m < l and number_continuuum < 4 : 
                if gameState["Board"][k-m][m] == 1:
                    number_continuuum += 1
                    m += 1 
                else : 
                    number_continuuum = 0
                    m += 1 
            if number_continuuum == 4 : #只检查4个
                biasl = True
                break
    
    biasr = False #代表携着的是否有四个连着的0,端点在6列的
    for k in range(6) :#k代表可行的斜线
        l = 6 - max( 5 - k , k - 0 ) #代表第k个斜线的长度
        m = 0 
        number_continuuum = 0 #连着0的数量
        if  k < 3 :
            while m < l and number_continuuum < 4 : 
                if gameState["Board"][k+m][6-m] == 1 :
                    number_continuuum += 1
                    m += 1 
                else : 
                    number_continuuum = 0
                    m += 1 
            if number_continuuum == 4 : #只检查4个
                biasr = True
                break
        else :
            while m < l and number_continuuum < 4 : 
                if gameState["Board"][k-m][6-m] == 1:
                    number_continuuum += 1
                    m += 1 
                else : 
                    number_continuuum = 0
                    m += 1 
            if number_continuuum == 4 : #只检查4个
                biasr = True
                break
    
    lose = column or row or biasl or biasr 
    return lose


def isDraw( gameState ):
    # 参数当前状态gameState
    # 返回bool类型，是否平局
    draw = True 
    # 检查是否有棋子未下
    for j in range(5, 0, -1) :
          for i in range(7) :
              if gameState["Board"][j][i]== -1:
                  draw = False
                  return draw
    
    win = isWin(gameState )
    lose = isLose(gameState )
    if ( win == True ) or ( lose == True ):
        draw = False
    
    return draw