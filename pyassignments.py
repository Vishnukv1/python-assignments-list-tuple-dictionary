#first question
n= int(input("enter length of list :"))
arr =[]
for i in range(n):
    a = int(input('Enter first element in the {} tuple:'.format(i)))
    b = int(input('Enter second element in the {} tuple: '.format(i)))
    arr.append((a,b))
#arr = [(2,5),(1,2),(4,4),(2,3),(2,1)]
n = len(arr)
for i in range(n-1) :
    for j in range(0,n-i-1):
        if arr[j][1]>arr[j+1][1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)
