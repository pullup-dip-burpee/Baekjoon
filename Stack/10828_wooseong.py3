import sys

N = int(input())
user_input = [sys.stdin.readline().rsplit() for i in range(N)]
lst = []
for i in range(N):
	order = user_input[i]
	if order[0] == "push":
		a = int(order[1])
		lst.append(a)
	elif order[0] == "pop":
		if len(lst)==0:
			print(-1)
		else:
			print(lst.pop())
	elif order[0] == "size":
		print(len(lst))
	elif order[0] == "empty":
		if len(lst)==0:
			print(1)
		else:
			print(0)
	elif order[0] == "top":
		if len(lst)==0:
			print(-1)
		else:
			print(lst[-1])
