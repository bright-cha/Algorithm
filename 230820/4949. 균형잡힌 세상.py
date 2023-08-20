'''
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
.

'''
while True:
    word = input()
    if word == '.':
        break
    stack = []
    for i in word:
        if i in '()[]':
            if i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    print('no')
                    break
            elif i == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    print('no')
                    break
            else:
                stack.append(i)
    else:
        if not stack:
            print('yes')
        else:
            print('no')