import copy
def getSuccessor(gameState , action , color):
    # 参数action 代表新的棋子所在列的编号（注意从0开始！）
    # 参数color 代表新的棋子的颜色
    # 返回一个gameState 表示操作后的状态
    # 注意缺少保护！针对特殊情况
    # 检查是否非法
    if  gameState["Board"][0][action] != -1  :
        return Exception #不处理只抛出异常！可以继续修改

    state = copy.deepcopy(gameState) #Json 对象的深拷贝
    i = 5 #从最底层找新棋子的位置
    while i >= 0 : 
        if state["Board"][i][action] != -1  :
            i -= 1
            continue
        else :
            state["Board"][i][action] = color 
            break

    return  state     