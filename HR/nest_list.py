if __name__ == '__main__':
    
    names = []
    grades = []
    res = []
    
    for _ in range(int(input())):
            name = input()
            score = float(input())
            names.append((name,score))
            grades.append(score)

    second = list(set(grades))
    second.sort()
    second = second[1]


    for name,score in names:
        if score == second:
            res.append(name)
    
    res.sort()
    print(*res , sep='\n')