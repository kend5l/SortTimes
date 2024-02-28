
import sys, random, time, alg_sorts

#------------------------------- MAIN BEGINS--------------------------------------------
print("Welcome to the test suite of selected sorting algorithms!")

#this will be our mainline function
def main():

    while True:
        
        print("\nSelect the sorting algorithm you want to test.")
        print("\n1. Bubble Sort")
        print("2. Merge Sort")
        print("3. Quick Sort")
        print("4. Shell Sort")
        print("5. Exit")
        chosen_sort = int(input("Select a sorting algorithm: "))

        if chosen_sort == 1:
            bubble_menu()
        elif chosen_sort == 2:
            merge_menu()
        elif chosen_sort == 3:
            quick_menu()
        elif chosen_sort == 4:
            shell_menu()
        elif chosen_sort == 5:
            print("Bye!")
            sys.exit()
        else:
            print("invalid choice. try again: ")

# ------------------------------------ BUBBLE MENU -------------------------------------
def bubble_menu():

    print("Case scenarios for bubble sort:\n")
    print("1. Best Case")
    print("2. Average Case")
    print("3. Worst Case")
    print("4. Exit bubble sort test\n")
    case = int(input("Select the case: "))

    if case == 1:
        # to test best case, we will pass it an already sorted array
        print("In best case,")
        array = alg_sorts.fill_array(100)
        alg_sorts.bubbleSort(array)
        t0 = time.perf_counter()
        alg_sorts.bubbleSort(array)
        t1 = time.perf_counter()
        print(f"For N = 100, it takes {t1-t0} seconds ")

        array = alg_sorts.fill_array(1000)
        alg_sorts.bubbleSort(array)
        t0 = time.perf_counter()
        alg_sorts.bubbleSort(array)
        t1 = time.perf_counter()
        print(f"For N = 1000, it takes {t1-t0} seconds")

        array = alg_sorts.fill_array(10000)
        alg_sorts.bubbleSort(array)
        t0 = time.perf_counter()
        alg_sorts.bubbleSort(array)
        t1 = time.perf_counter()
        print(f"For N = 10000, it takes {t1-t0} seconds")

        n_choice = input("Do you want to input another N? (Y/N): ")

        if n_choice == 'Y':
            n = int(input("What is the n? "))
            array = alg_sorts.fill_array(n)
            alg_sorts.bubbleSort(array)
            t0 = time.perf_counter()
            alg_sorts.bubbleSort(array)
            t1 = time.perf_counter()
            print(f"For N = {n}, it takes {t1-t0} seconds")

        if n_choice == 'N':
            bubble_menu()

    elif case == 2:
        # to test average case, we will pass a randomized array
        print("In average case,")
        array = alg_sorts.fill_array(100)
        t0 = time.perf_counter()
        alg_sorts.bubbleSort(array)
        t1 = time.perf_counter()
        print(f"For N = 100, it takes {t1-t0} seconds ")

        array = alg_sorts.fill_array(1000)
        t0 = time.perf_counter()
        alg_sorts.bubbleSort(array)
        t1 = time.perf_counter()
        print(f"For N = 1000, it takes {t1-t0} seconds")

        array = alg_sorts.fill_array(10000)
        t0 = time.perf_counter()
        alg_sorts.bubbleSort(array)
        t1 = time.perf_counter()
        print(f"For N = 10000, it takes {t1-t0} seconds")

        n_choice = input("Do you want to input another N? (Y/N): ")

        if n_choice == 'Y':
            n = int(input("What is the n? "))
            array = alg_sorts.fill_array(n)
            t0 = time.perf_counter()
            alg_sorts.bubbleSort(array)
            t1 = time.perf_counter()
            print(f"For N = {n}, it takes {t1-t0} seconds")

        if n_choice == 'N':
            bubble_menu()


    elif case == 3:
        # to test worst case, we will provide a reverse sorted array
        print("In worst case,")
        array = alg_sorts.fill_array(100)
        array.reverse()
        t0 = time.perf_counter()
        alg_sorts.bubbleSort(array)
        t1 = time.perf_counter()
        print(f"For N = 100, it takes {t1-t0} seconds ")

        array = alg_sorts.fill_array(1000)
        array.reverse()
        t0 = time.perf_counter()
        alg_sorts.bubbleSort(array)
        t1 = time.perf_counter()
        print(f"For N = 1000, it takes {t1-t0} seconds")

        array = alg_sorts.fill_array(10000)
        array.reverse()
        t0 = time.perf_counter()
        alg_sorts.bubbleSort(array)
        t1 = time.perf_counter()
        print(f"For N = 10000, it takes {t1-t0} seconds")

        n_choice = input("Do you want to input another N? (Y/N): ")

        if n_choice == 'Y':
            n = int(input("What is the n? "))
            array = alg_sorts.fill_array(n)
            array.reverse()
            t0 = time.perf_counter()
            alg_sorts.bubbleSort(array)
            t1 = time.perf_counter()
            print(f"For N = {n}, it takes {t1-t0} seconds")

        if n_choice == 'N':
            bubble_menu()

    elif case == 4:
        main()
    else:
        print("invalid selection. try again: ")

    
#------------------------------------ MERGE MENU -------------------------------------
def merge_menu():
    print("Case scenarios for merge sort:\n")
    print("1. Best Case")
    print("2. Average Case")
    print("3. Worst Case")
    print("4. Exit merge sort test\n")
    case = int(input("Select the case: "))

    if case == 1:
        # to test the best case, we will pass an already sorted array
        print("In best case,")
        array = alg_sorts.fill_array(100)
        alg_sorts.merge_sort(array)
        t0 = time.perf_counter()
        alg_sorts.merge_sort(array)
        t1 = time.perf_counter()
        print(f"For N = 100, it takes {t1-t0} seconds ")

        array = alg_sorts.fill_array(1000)
        alg_sorts.merge_sort(array)
        t0 = time.perf_counter()
        alg_sorts.merge_sort(array)
        t1 = time.perf_counter()
        print(f"For N = 1000, it takes {t1-t0} seconds")

        array = alg_sorts.fill_array(10000)
        alg_sorts.merge_sort(array)
        t0 = time.perf_counter()
        alg_sorts.merge_sort(array)
        t1 = time.perf_counter()
        print(f"For N = 10000, it takes {t1-t0} seconds")

        n_choice = input("Do you want to input another N? (Y/N): ")

        if n_choice == 'Y':
            n = int(input("What is the n? "))
            array = alg_sorts.fill_array(n)
            alg_sorts.merge_sort(array)
            t0 = time.perf_counter()
            alg_sorts.merge_sort(array)
            t1 = time.perf_counter()
            print(f"For N = {n}, it takes {t1-t0} seconds")

        if n_choice == 'N':
            merge_menu()

    elif case == 2:
        # to test the average case, we will pass a randomized array
        print("In average case,")
        array = alg_sorts.fill_array(100)
        t0 = time.perf_counter()
        alg_sorts.merge_sort(array)
        t1 = time.perf_counter()
        print(f"For N = 100, it takes {t1-t0} seconds ")

        array = alg_sorts.fill_array(1000)
        t0 = time.perf_counter()
        alg_sorts.merge_sort(array)
        t1 = time.perf_counter()
        print(f"For N = 1000, it takes {t1-t0} seconds")

        array = alg_sorts.fill_array(10000)
        t0 = time.perf_counter()
        alg_sorts.merge_sort(array)
        t1 = time.perf_counter()
        print(f"For N = 10000, it takes {t1-t0} seconds")

        n_choice = input("Do you want to input another N? (Y/N): ")


        if n_choice == 'Y':
            n = int(input("What is the n? "))
            array = alg_sorts.fill_array(n)
            t0 = time.perf_counter()
            alg_sorts.merge_sort(array)
            t1 = time.perf_counter()
            print(f"For N = {n}, it takes {t1-t0} seconds")

        if n_choice == 'N':
            merge_menu()

    elif case == 3:
        # to test the worst case, we will pass a reverse sorted array
        print("In worst case,")
        array = alg_sorts.fill_array(100)
        array.reverse()
        t0 = time.perf_counter()
        alg_sorts.merge_sort(array)
        t1 = time.perf_counter()
        print(f"For N = 100, it takes {t1-t0} seconds ")

        array = alg_sorts.fill_array(1000)
        array.reverse()
        t0 = time.perf_counter()
        alg_sorts.merge_sort(array)
        t1 = time.perf_counter()
        print(f"For N = 1000, it takes {t1-t0} seconds")

        array = alg_sorts.fill_array(10000)
        array.reverse()
        t0 = time.perf_counter()
        alg_sorts.merge_sort(array)
        t1 = time.perf_counter()
        print(f"For N = 10000, it takes {t1-t0} seconds")

        n_choice = input("Do you want to input another N? (Y/N): ")


        if n_choice == 'Y':
            n = int(input("What is the n? "))
            array = alg_sorts.fill_array(n)
            array.reverse()
            t0 = time.perf_counter()
            alg_sorts.merge_sort(array)
            t1 = time.perf_counter()
            print(f"For N = {n}, it takes {t1-t0} seconds")

        if n_choice == 'N':
            merge_menu()

    elif case == 4:
        main()
    else:
        print("invalid selection. try again: ")

    
 # ------------------------------------ QUICK MENU -------------------------------------    
def quick_menu():
    print("Case scenarios for quick sort:\n")
    print("1. Best Case")
    print("2. Average Case")
    print("3. Worst Case")
    print("4. Exit quick sort test\n")
    case = int(input("Select the case: "))

    if case == 1:
        # to test the best case, we will evenly divide the list
        print("In best case,")
        array = alg_sorts.fill_array(100)
        t0 = time.perf_counter()
        alg_sorts.best_quickSort(array, 0, len(array) - 1)
        t1 = time.perf_counter()
        print(f"For N = 100, it takes {t1-t0} seconds ")

        array = alg_sorts.fill_array(1000)
        t0 = time.perf_counter()
        alg_sorts.best_quickSort(array, 0, len(array) - 1)
        t1 = time.perf_counter()
        print(f"For N = 1000, it takes {t1-t0} seconds ")

        array = alg_sorts.fill_array(10000)
        t0 = time.perf_counter()
        alg_sorts.best_quickSort(array, 0, len(array) - 1)
        t1 = time.perf_counter()
        print(f"For N = 10000, it takes {t1-t0} seconds ")

        n_choice = input("Do you want to input another N? (Y/N): ")

        if n_choice == 'Y':
            n = int(input("What is the n? "))
            array = alg_sorts.fill_array(n)
            t0 = time.perf_counter()
            alg_sorts.best_quickSort(array, 0, len(array) - 1)
            t1 = time.perf_counter()
            print(f"For N = {n}, it takes {t1-t0} seconds")

        if n_choice == 'N':
            quick_menu()


    elif case == 2:
        # to test the average case, we will pass a randomized array
        print("In average case,")
        array = alg_sorts.fill_array(100)
        t0 = time.perf_counter()
        alg_sorts.quickSort(array, 0, len(array) - 1)
        t1 = time.perf_counter()
        print(f"For N = 100, it takes {t1-t0} seconds ")

        array = alg_sorts.fill_array(1000)
        t0 = time.perf_counter()
        alg_sorts.quickSort(array, 0, len(array) - 1)
        t1 = time.perf_counter()
        print(f"For N = 1000, it takes {t1-t0} seconds ")

        array = alg_sorts.fill_array(10000)
        t0 = time.perf_counter()
        alg_sorts.quickSort(array, 0, len(array) - 1)
        t1 = time.perf_counter()
        print(f"For N = 10000, it takes {t1-t0} seconds ")

        n_choice = input("Do you want to input another N? (Y/N): ")

        if n_choice == 'Y':
            n = int(input("What is the n? "))
            array = alg_sorts.fill_array(n)
            t0 = time.perf_counter()
            alg_sorts.quickSort(array, 0, len(array) - 1)
            t1 = time.perf_counter()
            print(f"For N = {n}, it takes {t1-t0} seconds")

        if n_choice == 'N':
            quick_menu()


    elif case == 3:
        print("In worst case,")
        # to test quick sort in its worst case, we will simply pass a reverse sorted array
        # this way it is as unbalanced as possible
        array = alg_sorts.fill_array(100)
        array.reverse()
        t0 = time.perf_counter()
        alg_sorts.quickSort(array, 0, len(array) - 1)
        t1 = time.perf_counter()
        print(f"For N = 100, it takes {t1-t0} seconds ")

        array = alg_sorts.fill_array(1000)
        array.reverse()
        t0 = time.perf_counter()
        alg_sorts.quickSort(array, 0, len(array) - 1)
        t1 = time.perf_counter()
        print(f"For N = 1000, it takes {t1-t0} seconds ")

        array = alg_sorts.fill_array(10000)
        array.reverse()
        t0 = time.perf_counter()
        alg_sorts.quickSort(array, 0, len(array) - 1)
        t1 = time.perf_counter()
        print(f"For N = 10000, it takes {t1-t0} seconds ")

        n_choice = input("Do you want to input another N? (Y/N): ")

        if n_choice == 'Y':
            n = int(input("What is the n? "))
            array = alg_sorts.fill_array(n)
            array.reverse()
            t0 = time.perf_counter()
            alg_sorts.quickSort(array, 0, len(array) - 1)
            t1 = time.perf_counter()
            print(f"For N = {n}, it takes {t1-t0} seconds")

        if n_choice == 'N':
            quick_menu()


    elif case == 4:
        main()
    else:
        print("invalid selection. try again: ")

    
# ------------------------------------ SHELL MENU -------------------------------------
def shell_menu():
    print("Case scenarios for shell sort:\n")
    print("1. Best Case")
    print("2. Average Case")
    print("3. Worst Case")
    print("4. Exit shell sort test\n")
    case = int(input("Select the case: "))

    if case == 1:
        # to test its best case, we will pass an already sorted array
        print("In best case,")
        array = alg_sorts.fill_array(100)
        alg_sorts.shell_sort(array)
        t0 = time.perf_counter()
        alg_sorts.shell_sort(array)
        t1 = time.perf_counter()
        print(f"For N = 100, it takes {t1-t0} seconds")

        array = alg_sorts.fill_array(1000)
        alg_sorts.shell_sort(array)
        t0 = time.perf_counter()
        alg_sorts.shell_sort(array)
        t1 = time.perf_counter()
        print(f"For N = 1000, it takes {t1-t0} seconds")

        array = alg_sorts.fill_array(10000)
        alg_sorts.shell_sort(array)
        t0 = time.perf_counter()
        alg_sorts.shell_sort(array)
        t1 = time.perf_counter()
        print(f"For N = 10000, it takes {t1-t0} seconds")

        n_choice = input("Do you want to input another N? (Y/N): ")

        if n_choice == 'Y':
            n = int(input("What is the n? "))
            array = alg_sorts.fill_array(n)
            alg_sorts.shell_sort(array)
            t0 = time.perf_counter()
            alg_sorts.shell_sort(array)
            t1 = time.perf_counter()
            print(f"For N = {n}, it takes {t1-t0} seconds")

        if n_choice == 'N':
            shell_menu()

    elif case == 2:
        # to test its average case, we will pass it a randomized array
        print("In average case,")
        array = alg_sorts.fill_array(100)
        t0 = time.perf_counter()
        alg_sorts.shell_sort(array)
        t1 = time.perf_counter()
        print(f"For N = 100, it takes {t1-t0} seconds ")

        array = alg_sorts.fill_array(1000)
        t0 = time.perf_counter()
        alg_sorts.shell_sort(array)
        t1 = time.perf_counter()
        print(f"For N = 1000, it takes {t1-t0} seconds")

        array = alg_sorts.fill_array(10000)
        t0 = time.perf_counter()
        alg_sorts.shell_sort(array)
        t1 = time.perf_counter()
        print(f"For N = 10000, it takes {t1-t0} seconds")

        n_choice = input("Do you want to input another N? (Y/N): ")

        if n_choice == 'Y':
            n = int(input("What is the n? "))
            array = alg_sorts.fill_array(n)
            t0 = time.perf_counter()
            alg_sorts.shell_sort(array)
            t1 = time.perf_counter()
            print(f"For N = {n}, it takes {t1-t0} seconds")

        if n_choice == 'N':
            shell_menu()

    elif case == 3:
        # to test it in its worse case, we will pass a reverse ordered array
        print("In worst case,")
        array = alg_sorts.fill_array(100)
        array.reverse()
        t0 = time.perf_counter()
        alg_sorts.shell_sort(array)
        t1 = time.perf_counter()
        print(f"For N = 100, it takes {t1-t0} seconds")

        array = alg_sorts.fill_array(1000)
        array.reverse()
        t0 = time.perf_counter()
        alg_sorts.shell_sort(array)
        t1 = time.perf_counter()
        print(f"For N = 1000, it takes {t1-t0} seconds")

        array = alg_sorts.fill_array(10000)
        array.reverse()
        t0 = time.perf_counter()
        alg_sorts.shell_sort(array)
        t1 = time.perf_counter()
        print(f"For N = 10000, it takes {t1-t0} seconds")

        n_choice = input("Do you want to input another N? (Y/N): ")

        if n_choice == 'Y':
            n = int(input("What is the n? "))
            array = alg_sorts.fill_array(n)
            array.reverse()
            t0 = time.perf_counter()
            alg_sorts.shell_sort(array)
            t1 = time.perf_counter()
            print(f"For N = {n}, it takes {t1-t0} seconds")
            
        if n_choice == 'N':
            shell_menu()
    elif case == 4:
        main()
    else:
        print("invalid selection. try again: ")


# ------------------------------------ PROGRAM START -------------------------------------
if __name__ == "__main__":
    main()