# 5.01s
def judgeCircle(moves):
    """
    :type moves: str
    :rtype: bool
    """
    up=0
    left=0
    for i in moves:
        if i=='U':
            up+=1
        elif i=='D':
            up-=1
        elif i=='L':
            left+=1
        else:
            left-=1

    if up==0 and left==0:
        return True
    else:
        return False

def judgeCircle(self, moves):
    return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
