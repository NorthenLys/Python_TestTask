bracket_seq = str(input()) # Works only with '()' and '[]' type of brackets. Ex. for test [((())()(())]]
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
print(*new_seq)