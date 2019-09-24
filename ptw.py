def menu():
    print("1.selection");
    print("2.bubble");
    print("3.inserction");
    print("0.exit");

def choice(a):
    print("enter choice");
    ch=int(input());
    return ch;

def selectionsort(a):
    for i in range(0, len(a) - 1):
        small = i;
        for j in range(i + 1, len(a)):
            if a[j] < a[small]:
                small = j;
        a[i], a[small] = a[small], a[i];
    a = input('Enter the list of numbers: ').split();
    a = [int(x) for x in a];
    selectionsort(a);
    print('Sorted list: ', end='');
    print(a);


def bubble_sort(a):
    for i in range(len(a) - 1, 0, -1):
        no_swap = True
        for j in range(0, i):
            if a[j + 1] < a[j]:
                a[j], a[j + 1] = a[j + 1], a[j]
                no_swap = False
        if no_swap:
            return
    a = input('Enter the list of numbers: ').split()
    a = [int(x) for x in a]
    bubble_sort(a)
    print('Sorted list: ', end='')
    print(a)

def insertion_sort(a):
    for i in range(1, len(a)):
        temp = a[i]
        j = i - 1
        while (j >= 0 and temp < a[j]):
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = temp
    a = input('Enter the list of numbers: ').split()
    a = [int(x) for x in a]
    insertion_sort(a)
    print('Sorted list: ', end='')
    print(a)

a=[];
ch=0;
while(ch!=0):
    menu();
    ch=choice(a);
    
    if(ch==1):
        selectionsort(a);
    if(ch==2):
        bubble_sort(a);
    if(ch==3):
        insertion_sort(a);
        
print("buy");
