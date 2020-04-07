print("this is the map of position nos.")
print('\n',7,"|",8,"|",9,'\n',4,"|",5,"|",6,'\n',1,"|",2,"|",3)
b='y'
while b=='y' or b=='Y':
    k=0
    a=[0,0,0,0,0,0,0,0,0]
    x=True
    while x==True:
        if k%2==0:
            b=int(input("player 1 chance-"))
            if b>9 or b<1:
                print("bad input")
                continue
            if a[b-1]!=0:
                print('bad input')
                continue
            a[b-1]=1
        else:
            b=int(input("player 2 chance-"))
            if b>9 or b<1:
                print("bad input")
                continue
            if a[b-1]!=0:
                print('bad input')
                continue
            a[b-1]=2
        f=[]
        for i in range(9):
            if a[i]==1:
                f.append("O")
            elif a[i]==2:
                f.append("X")
            else:
                f.append(" ")
    
        print('\n',f[6],"|",f[7],"|",f[8],'\n',f[3],"|",f[4],"|",f[5],'\n',f[0],"|",f[1],"|",f[2])  
        for i in range(3):
            for j in range(3):
                if (a[i*3+0]==a[i*3+1] and  a[i*3+1]==a[i*3+2]and a[3*i]!=0) or (a[0+i]==a[3+i] and  a[3+i]==a[6+i]and a[6+i]!=0) :
                    print(k%2+1,"player wins")
                    x=False
                    break
                break
                if (a[0]==a[4] and  a[4]==a[8]and a[0]!=0) or (a[2]==a[4] and  a[4]==a[6]and a[2]!=0):
                    print(k%2+1,"player wins")
                    x=False
                    break
                break
            
                
        if 0 not in set(a) and x!=False:
            print("draw")
            x=False
        k=k+1
    b=input("DO YOU WANT TO PLAY AGAIN (ENTER y OR n)-")
    

                
