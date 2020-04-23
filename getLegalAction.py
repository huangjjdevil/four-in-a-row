def getLegalAction(gameState):
    # 返回一个List，List包含可下棋子的列的编号（注意从0开始！）
    # 注意缺少保护！针对特殊情况
    legalActions = []
    for i in range(7):
        if gameState["Board"][0][i] == -1 : #只检查最上面一行
            legalActions.append(i)

    return legalActions