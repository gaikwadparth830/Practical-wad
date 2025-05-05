print("Enter no. to be Sorted")
lis=list(map(int,input().split()))
print(lis)

print("Enter a number for Sorting method")
print("1.Bubb")
print("2.sel")
print("3.mer")

a=int(input())

def bubb_sort(lis):
  n =len(lis)

  for i in range(n):
    for j in range(0,n-1):

       if lis[j]>lis[j+1]:
          lis[j],lis[j+1]=lis[j+1],lis[j]
  return lis

def sel_sort(lis):
  n=len(lis)
  for i in range(n):
    min_index=i
    for j in range(i+1,n):
      if lis[j]<lis[min_index]:
         min_index=j
    lis[i],lis[min_index]=lis[min_index],lis[i]
  return lis


if a==1:
  b=bubb_sort(lis)
  print(b)

if a==2:
  c=sel_sort(lis)
  print(c)

