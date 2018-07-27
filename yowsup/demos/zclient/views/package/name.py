def NameMagic(_Name):
    _NameUpper = _Name.upper()
    q = ""
    q += 'The Hidden Meaning of your name is :\n'
    A,B,C = [65, 77, 66, 73, 84, 73, 79, 85, 83], [66, 82, 65, 86, 69], [67, 76, 69, 86, 69, 82]
    D,E,F = [68, 69, 76, 73, 71, 72, 84, 70, 85, 76],[69, 65, 71, 69, 82],[70, 69, 65, 82, 76, 69, 83, 83]
    G,H,I = [71, 69, 78, 73, 85, 83],[72, 79, 78, 79, 85, 82, 65, 66, 76, 69],[73, 78, 84, 69, 76, 76, 73, 71, 69, 78, 84]
    J,K,L = [74, 69, 65, 76, 79, 85, 83],[75, 73, 78, 68],[76, 65, 90, 89]
    M,N,O = [77, 85, 83, 73, 67, 65, 76],[78, 69, 82, 68],[79, 86, 69, 82, 67, 79, 78, 70, 73, 68, 69, 78, 84]
    P,Q,R = [80, 82, 69, 67, 73, 79, 85, 83],[81, 85, 65, 76, 73, 84, 89],[82, 79, 77, 65, 78, 84, 73, 67]
    S,T,U = [83, 77, 65, 82, 84], [84, 89, 80, 73, 67, 65, 76],[85, 78, 73, 81, 85, 69]
    V,W,X = [86, 69, 78, 84, 85, 82, 79, 85, 83], [87, 73, 76, 68], [88, 69, 78, 79, 80, 72, 79, 66, 69]
    Y,Z   = [89, 69, 65, 83, 84, 89], [90, 69, 65, 76, 79, 85, 83]
    for i in _NameUpper:
        for char in range(65, 91):
            if i == chr(char) and chr(char) == 'A':
                q+=chr(65)+'- '
                for ii in A:
                    q+=chr(ii)
                q+="\n"

            elif i == chr(char) and chr(char) == 'B':
                q+=chr(66)+'- '
                for ii in B:
                    q+=chr(ii)
                q+="\n"

            elif i == chr(char) and chr(char) == 'C':
                q+=chr(67)+'- '
                for ii in C:
                    q+=chr(ii)
                q+="\n"
            elif i == chr(char) and chr(char) == 'D':
                q+=chr(68)+'- '
                for ii in D:
                    q+=chr(ii)
                q+="\n"

            elif i == chr(char) and chr(char) == 'E':
                q+=chr(69)+'- '
                for ii in E:
                    q+=chr(ii)
                q+="\n"
            elif i == chr(char) and chr(char) == 'F':
                q+=chr(70)+'- '
                for ii in F:
                    q+=chr(ii)
                q+="\n"

            elif i == chr(char) and chr(char) == 'G':
                q+=chr(71)+'- '
                for ii in G:
                    q+=chr(ii)
                q+="\n"

            elif i == chr(char) and chr(char) == 'H':
                q+=chr(72)+'- '
                for ii in H:
                    q+=chr(ii)
                q+="\n"

            elif i == chr(char) and chr(char) == 'I':
                q+=chr(73)+'- '
                for ii in I:
                    q+=chr(ii)
                q+="\n"
            elif i == chr(char) and chr(char) == 'J':
                q+=chr(74)+'- '
                for ii in J:
                    q+=chr(ii)
                q+="\n"

            elif i == chr(char) and chr(char) == 'K':
                q+=chr(75)+'- '
                for ii in K:
                    q+=chr(ii)
                q+="\n"
            elif i == chr(char) and chr(char) == 'L':
                q+=chr(76)+'- '
                for ii in L:
                    q+=chr(ii)
                q+="\n"

            elif i == chr(char) and chr(char) == 'M':
                q+=chr(77)+'- '
                for ii in M:
                    q+=chr(ii)
                q+="\n"

            elif i == chr(char) and chr(char) == 'N':
                q+=chr(78)+'- '
                for ii in N:
                    q+=chr(ii)
                q+="\n"

            elif i == chr(char) and chr(char) == 'O':
                q+=chr(79)+'- '
                for ii in O:
                    q+=chr(ii)
                q+="\n"
            elif i == chr(char) and chr(char) == 'P':
                q+=chr(80)+'- '
                for ii in P:
                    q+=chr(ii)
                q+="\n"

            elif i == chr(char) and chr(char) == 'Q':
                q+=chr(81)+'- '
                for ii in Q:
                    q+=chr(ii)
                q+="\n"
            elif i == chr(char) and chr(char) == 'R':
                q+=chr(82)+'- '
                for ii in R:
                    q+=chr(ii)
                q+="\n"

            elif i == chr(char) and chr(char) == 'S':
                q+=chr(83)+'- '
                for ii in S:
                    q+=chr(ii)
                q+="\n"

            elif i == chr(char) and chr(char) == 'T':
                q+=chr(84)+'- '
                for ii in T:
                    q+=chr(ii)
                q+="\n"

            elif i == chr(char) and chr(char) == 'U':
                q+=chr(85)+'- '
                for ii in U:
                    q+=chr(ii)
                q+="\n"
            elif i == chr(char) and chr(char) == 'V':
                q+=chr(86)+'- '
                for ii in V:
                    q+=chr(ii)
                q+="\n"

            elif i == chr(char) and chr(char) == 'W':
                q+=chr(87)+'- '
                for ii in W:
                    q+=chr(ii)
                q+="\n"
            elif i == chr(char) and chr(char) == 'X':
                q+=chr(88)+'- '
                for ii in X:
                    q+=chr(ii)
                q+="\n"

            elif i == chr(char) and chr(char) == 'Y':
                q+=chr(89)+'- '
                for ii in Y:
                    q+=chr(ii)
                q+="\n"
            elif i == chr(char) and chr(char) == 'Z':
                q+=chr(90)+'- '
                for ii in Z:
                    q+=chr(ii)
                q+="\n"
    return q
