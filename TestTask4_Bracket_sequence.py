bracket_seq = str(input()) #Works only with '()' and '[]' type of brackets. Ex. for test [((())()(())]]
#Don't work with ()()[] type of brasket sequence: match 'incorrect'. Fix in progress
if len(bracket_seq)%2==0:
    n_start = 0
    n_end = len(bracket_seq)-1
    while n_start < n_end:
        for i in range(len(bracket_seq)):
            if (bracket_seq[n_start] == '(' or bracket_seq[n_start] == '[') and (bracket_seq[n_end] != bracket_seq[n_start]):
                if (bracket_seq[n_start] == '(' and bracket_seq[n_end] == ')') or (bracket_seq[n_start] == '[' and bracket_seq[n_end] == ']'):
                    continue
                else:
                    print('False')
                    exit()
            elif bracket_seq[n_start] == bracket_seq[n_end]:
                print('False')
                exit()
            elif (bracket_seq[n_start] == bracket_seq[n_end-1]) and (bracket_seq[n_start+1] == bracket_seq[n_end]):
                continue
            else:
                print('False')
                exit()
        n_start += 1
        n_end -= 1
    print('True')
elif bracket_seq == ' ':
    print('True')
else:
    print('False')


