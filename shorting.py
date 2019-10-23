def choic():
    print('1.selectionsort');
    print('2.bubblesort');
    print('3.insertionsort');
    print('4.margesort');
    print('0.exit');

def selectionsort(a):
    for i in range(0, len(a) - 1):
        small = i;
        for j in range(i + 1, len(a)):
            if a[j] < a[small]:
                small = j;
        a[i], a[small] = a[small], a[i];


def bubble_sort(a):
    for i in range(len(a) - 1, 0, -1):
        for j in range(0, i):
            if a[j]>a[j+1]:
                tmp=a[j];
                a[j]=a[j+1];
                a[j+1]=tmp;

def insertion_sort(a):
    for i in range(1, len(a)):
        temp = a[i];
        j = i - 1;
        while (j >= 0 and temp < a[j]):
            a[j + 1] = a[j];
            j = j - 1;
        a[j + 1] = temp;

def merge_sort(a, first, last):
    if last - first > 1:
        mid = (first + last)//2;
        merge_sort(a, first, mid);
        merge_sort(a, mid, last);
        merge_list(a, first, mid, last);
 
def merge_list(a, first, mid, last):
    left = a[first:mid];
    right = a[mid:last];
    k = first;
    i = 0;
    j = 0;
    while (first + i < mid and mid + j < last):
        if (left[i] <= right[j]):
            a[k] = left[i];
            i = i + 1;
        else:
            a[k] = right[j];
            j = j + 1;
        k = k + 1;
    if first + i < mid:
        while k < last:
            a[k] = left[i];
            i = i + 1;
            k = k + 1;
    else:
        while k < last:
            a[k] = right[j];
            j = j + 1;
            k = k + 1;



choic();
ch=1;
while(ch!=0):
    ch=int(input("Enter the choice:"));
    if(ch==1):
        a = input('Enter the list of numbers for selection sort: ').split();
        a = [int(x) for x in a];
        selectionsort(a);
        print('Sorted list: ', end='');
        print(a);
    elif(ch==2):
        a = input('Enter the list of numbers for bubble sort: ').split();
        a = [int(x) for x in a];
        bubble_sort(a);
        print('Sorted list: ', end='');
        print(a);
    elif(ch==3):
        a = input('Enter the list of numbers for insertion sort: ').split();
        a = [int(x) for x in a];
        insertion_sort(a);
        print('Sorted list: ', end='');
        print(a);
    elif(ch==4):
        a = input('Enter the list of numbers for marge sort: ').split();
        a = [int(x) for x in a];
        merge_sort(a, 0, len(a));
        print('Sorted list: ', end='');
        print(a);
    
    
        
