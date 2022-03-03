from collections import deque

def main():
    n = int(input())
    for i in range(n):
        string  = deque(input().split(' '))
        string.reverse()
        print("Case #"+str(i+1)+": ", end='')
        for s in string:
            print(s,end=' ')

if __name__ == "__main__":
    main()