def hentoi(n,f,m,l):
    print("from ",f ,'to' ,l)
    if n==1:
        return 1
    hentoi(n-1,f,l,m)
    hentoi(1,f,m,l)
    hentoi(n-1,m,f,l)
print(hentoi(12,'A','B','C'))


