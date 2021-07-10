def arithmetic_arranger(problems,addition=False):
    
    foperand = []
    operator = []
    soperand = []
    add = []
    fline = []
    sline = []
    aline = []
    addline = []
    
    
    for problem in problems:
        problem = problem.lstrip()
        problem = problem.rstrip()
        sproblem = problem.split(" ")

        if len(sproblem[0]) > 4 or len(sproblem[2]) > 4:
            return('Error: Numbers cannot be accepted more than four digits.')    
        if not (sproblem[1] == "+" or sproblem[1] == "-"):
            return('Error: Operator must be \' + \' or \' - \' with spaces.') 
        foperand.append(sproblem[0])
        operator.append(sproblem[1])
        soperand.append(sproblem[2])
        if sproblem[1] == "+":
            add.append(str(int(sproblem[0])+int(sproblem[2])))
        elif sproblem[1] == "-":
            add.append(str(int(sproblem[0])-int(sproblem[2])))

    for i in range(0,len(problems)):
        fline.append(str(foperand[i]).rjust(6)+" ")
        sline.append(" "+str(operator[i]+str(soperand[i]).rjust(4))+" ")
        aline.append(6*"-"+" ")
        addline.append(str(add[i]).rjust(6)+" ")

    if addition == False:
        result = ((''.join(map(str, fline)))+"\n"+(''.join(map(str,sline)))+"\n"+(''.join(map(str,aline))))
    elif addition == True:
        result = ((''.join(map(str, fline)))+"\n"+(''.join(map(str,sline)))+"\n"+(''.join(map(str,aline)))+"\n"+(''.join(map(str, addline))))
    
    return result