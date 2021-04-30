#weight vector
a = 3
b = -3
wv = [a,b]
#weight matrix
WeightMatrix = [
        [0,0,a,b,0,b,a,0,a],
        [0,0,0,0,0,0,0,a,0],
        [a,0,0,b,0,b,a,0,a],
        [b,0,b,0,0,a,b,0,b],
        [0,0,0,0,0,0,0,b,0],
        [b,0,b,a,0,0,b,0,b],
        [a,0,a,b,0,b,0,0,a],
        [0,a,0,0,b,0,0,0,0],
        [a,0,a,b,0,b,a,0,0]]

input_vec = [-1,-1,-1,1,1,1,-1,-1,-1]

#activation function
actv_func = []
for i in range(9):
    temp=0
    for j in range(9):
        temp = temp+(input_vec[j]*WeightMatrix[j][i])
    actv_func.append(temp)
print(actv_func)

#output vector
out_vec = []
for x in actv_func:
    if x>=0:
        out_vec.append(1)
    if x<0:
        out_vec.append(-1)
print(out_vec)
