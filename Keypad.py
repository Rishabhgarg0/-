keypad = ["","","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]

def printcom(combination, current, output, n):
    if (current == n):
        print(* output, sep=",")
        return
    for i in range (len(keypad[combination[current]])):
        output.append(keypad[combination[current]][i])
        printcom(combination, current+1, output, n)
        output.pop()
        if (combination [current] == 0 or combination[current] == 1):
            return

combination = [4,2,5]
n = len(combination)
printcom(combination,0,[],n)