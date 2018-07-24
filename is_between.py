# is_between
def main():
    pass
    n=input()
    x=list(map(int,input().split()))
    k=x[0]
    l=x[1]
    o=int(n)
    temp=int(0)
    for i in range (k,l):
        if(i==o):
            temp=+1
    if(temp==1):
        print("yes")
    else:
        print("no")
if __name__ == '__main__':
    main()
