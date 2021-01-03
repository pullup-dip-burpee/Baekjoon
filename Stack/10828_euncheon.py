import sys
n = int(sys.stdin.readline())
stack = []
for i in range (n):
    line = sys.stdin.readline()
    cmd = line[:-1]
    if cmd == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif cmd[0:4] == 'push':
        num = int(cmd[5:])
        stack.append(num)


