bracket_seq = str(input()) # Works only with '()' and '[]' type of brackets. Ex. for test [((())()(())]]
#Don't work with ()()[] type of brasket sequence: match 'incorrect'. Fix in progress
circle_s = "("
circle_e = ")"
square_s = "["
square_e = "]"
def find_wrong_seq():
    if len(bracket_seq)%2==0:
        n_start = 0
        n_end = len(bracket_seq)-1
        while n_start < n_end:
            for i in range(len(bracket_seq)):
                if (bracket_seq[n_start] == '(' or bracket_seq[n_start] == '[') and (bracket_seq[n_end] != bracket_seq[n_start]):
                    if (bracket_seq[n_start] == '(' and bracket_seq[n_end] == ')') or (bracket_seq[n_start] == '[' and bracket_seq[n_end] == ']'):
                        continue
                    else:
                        return False
                elif bracket_seq[n_start] == bracket_seq[n_end]:
                    print('False')
                    exit()
                elif (bracket_seq[n_start] == bracket_seq[n_end - 1]) and (bracket_seq[n_start + 1] == bracket_seq[n_end]):
                    continue
                else:
                    return False
            n_start += 1
            n_end -= 1
        return True
    elif bracket_seq == ' ':
        return True
#Fix in progress, can be wrong:
    elif len(bracket_seq)%2==0:
        count_cs = bracket_seq.count(circle_s)
        count_ce = bracket_seq.count(circle_e)
        count_ss = bracket_seq.count(square_s)
        count_se = bracket_seq(square_e)
        if count_cs == count_ce and count_ss == count_se:
            return True
    else:
        return False

def fix_wrong_seq():
    new_seq = []
    n_bracket_seq = 0
    for i in range(0,len(bracket_seq)):
        if bracket_seq[n_bracket_seq] == '(' or bracket_seq[n_bracket_seq]==')':
           new_seq.append('(')
           new_seq.append(')')
        elif bracket_seq[n_bracket_seq] == '[' or bracket_seq[n_bracket_seq]==']':
            new_seq.append('[')
            new_seq.append(']')
        n_bracket_seq+=1
    return new_seq

ans = find_wrong_seq()
if ans == False:
    fixed_seq = fix_wrong_seq()
    print('Bracket sequence was incorrect. It is a possible correction for this:',*fixed_seq)
else:
    print('Bracket sequence is correct!')


