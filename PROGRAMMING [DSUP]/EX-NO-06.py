def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


n = int(input("Enter the number of elements in the list: "))
a = []

for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    a.append(element)

print("Original list:", a)
bubble_sort(a)
print("Sorted list:", a)
