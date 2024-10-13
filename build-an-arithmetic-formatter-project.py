def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    ret=[]
    look=['0','1','2','3','4','5','6','7','8','9']
    for pr in problems:
        tmp = pr.split()
        for num in tmp[0]:
            if num not in look:
                return 'Error: Numbers must only contain digits.'
        for num in tmp[2]:
            if num not in look:
                return 'Error: Numbers must only contain digits.'

        if tmp[1] not in ['+','-']:
            return "Error: Operator must be '+' or '-'."
        if len(tmp[0]) > 4 or len(tmp[2]) > 4 :
            return 'Error: Numbers cannot be more than four digits.'
        
        ret.append(tmp)

    temp = ' '*(max(len(ret[0][0]) , len(ret[0][2]))+2-len(ret[0][0])) + ret[0][0]
    for i in range(1,len(ret)):
        temp += '    ' + ' '*(max(len(ret[i][0]) , len(ret[i][2]))+2-len(ret[i][0])) + ret[i][0]
    temp += '\n'
    
    for i in range (len(ret)):
        if i != 0:
            temp += '    '
        temp += ret[i][1] + ' '*(max(len(ret[i][0]) , len(ret[i][2]))+1-len(ret[i][2])) + ret[i][2]
    temp += '\n'
    for i in range (len(ret)):
        if i != 0:
            temp += '    '
        temp +=  '-'*(max(len(ret[i][0]) , len(ret[i][2]))+2)
    if show_answers:
        temp += '\n'
        for i in range(len(ret)):
            if i != 0:
                temp += '    '
            if ret[i][1] == '+':
                tmp = str(int(ret[i][0]) + int(ret[i][2]))
            else :
                tmp = str(int(ret[i][0]) - int(ret[i][2]))

            temp += ' '*(max(len(ret[i][0]) , len(ret[i][2]))+2-len(tmp)) + tmp


 
    return temp
