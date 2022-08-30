import sys

count = int(sys.stdin.readline().strip())

stack = []

def push(x):
    stack.append(x)

def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])
        stack.pop()

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)
    
def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])

def main():
    for i in range(count):
        cmd = sys.stdin.readline().strip()
        if "push" in cmd:
            cm, n = cmd.split()
            n = int(n)
            push(n)
        elif cmd == "pop":
            pop()
        elif cmd == "size":
            size()
        elif cmd == "empty":
            empty()
        elif cmd == "top":
            top()

if __name__ == "__main__":
    main()

    