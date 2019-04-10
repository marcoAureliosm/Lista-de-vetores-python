face1=0;face2=0;face3=0;face4=0;face5=0;face6=0
for i in range(10):
    num=int(input("DIGITE A FACE DO DADO: "))
    if num==1:
        face1+=1
    elif num==2:
        face2+=1
    elif num==3:
        face3+=1
    elif num==4:
        face4+=1
    elif num==5:
        face5+=1
    elif num==6:
        face6+=1
    elif num>6 or num<1:
        print('Valor invalido')
print("Face-01:[{}] Face-02:[{}] Face-03:[{}] Face-04:[{}] Face-05:[{}] Face-06:[{}]".format(face1,face2,face3,face4,face5,face6))
