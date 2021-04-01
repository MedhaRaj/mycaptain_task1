n=int(input("Enter number of elements in the list"))
lis=[int(input(f"enter the input number {i}")) for i in range(n)]
lis1=[i for i in lis if i%2==0]
print(lis1)
