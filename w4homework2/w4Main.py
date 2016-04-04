def playgame(u1, u2):
    if u1 ==u2:
        result="draw"
    elif u1 == 'scissor' and u2 == 'paper':
        result="scissor won."
    elif u1 == 'scissor' and u2 == 'rock':
        result="rock won."
    elif u1 == 'rock' and  u2 == 'scissor':
        result="rock won."
    elif u1 == 'rock' and  u2 == 'paper':
        result="paper won."
    elif u1 == 'paper' and u2 == 'scissor':
        result="scissor won."
    elif u1 == 'paper' and u2 == 'rock':
        result="paper won."
    else:
        result="Error"
    return result


def lab4():
    sel1 = raw_input("frist rock,scissor,paper:")
    sel2 = raw_input("second rock,scissor,paper: ")
    print playgame(sel1,sel2)
def main():
    lab4()
 
if __name__=="__main__": 
     main() 
  