# PR. 4 Functional_Treat 

data = []          
is_2d = False
summary = {"count": 0, "mean": 0}  

def flatten(lst):
    
    if lst and isinstance(lst[0], list):
        return [x for row in lst for x in row]
    return lst

def read_numbers(text):
    
    nums = []
    for part in text.split():
        nums.append(float(part) if "." in part else int(part))
    return nums

def update_summary():
    global summary
    flat = flatten(data)
    summary["count"] = len(flat)
    summary["mean"] = sum(flat) / len(flat) if flat else 0

def average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def find_duplicates(numbers):
    dups = []
    for n in numbers:
        if numbers.count(n) > 1 and n not in dups:
            dups.append(n)
    return dups

def unique_values(numbers):
    result = []
    for n in numbers:
        if n not in result:
            result.append(n)
    return result

def show_values(*args):
    print("Values received:", ", ".join(str(a) for a in args))

def print_summary(**kwargs):
    for key, value in kwargs.items():
        print(f"- {key}: {value}")

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
   if n <= 1:
        return n

   return fibonacci(n - 1) + fibonacci(n - 2)

def filter_data(numbers, threshold, keep_above=True):
    
    if keep_above:
        return list(filter(lambda x: x >= threshold, numbers))
    return list(filter(lambda x: x <= threshold, numbers))

def get_statistics(numbers):
    return min(numbers), max(numbers), sum(numbers), average(numbers)

def show_grid(grid):
    width = max(len(str(x)) for row in grid for x in row)
    for row in grid:
        print("  ".join(str(x).rjust(width) for x in row))

def input_data():

    global data, is_2d
    print("\n1. Enter data manually")
    print("2. Use sample data")
    choice = input("Enter your choice: ").strip()

    if choice == "2":
        kind = input("Sample type - 1 for 1D, 2 for 2D: ").strip()
        if kind == "2":
            data = [[34, 12, 56], [78, 43, 21], [90, 12, 5]]
            is_2d = True
        else:
            data = [34, 12, 56, 78, 43, 21, 90]
            is_2d = False
    else:
        kind = input("Is the data 1D or 2D? (1/2): ").strip()
        try:
            if kind == "2":
                rows = int(input("How many rows? "))
                temp = []
                for i in range(rows):
                    line = input(f"Enter row {i + 1} (separated by spaces): ")
                    temp.append(read_numbers(line))
                data = temp
                is_2d = True
            else:
                line = input("Enter data for a 1D array (separated by spaces): ")
                data = read_numbers(line)
                is_2d = False
        except ValueError:
            print("\nInvalid input, numbers only please.")
            data = []
            return

    update_summary()
    if is_2d:
        print("\nYour 2D list:")
        show_grid(data)
    print("\nData has been stored successfully!")

def display_summary():
    flat = flatten(data)
    print("\nData Summary:")
    print("- Total elements:", len(flat))
    print("- Minimum value:", min(flat))
    print("- Maximum value:", max(flat))
    print("- Sum of all values:", sum(flat))
    print(f"- Average value: {average(flat):.2f}")
    print("- Duplicates:", find_duplicates(flat) or "none")
    print("- Unique values:", unique_values(flat))
    print("\nDataset characteristics (**kwargs):")
    print_summary(rows=len(data) if is_2d else 1,
                  global_count=summary["count"],
                  global_mean=round(summary["mean"], 2))
    print()
    show_values(*flat)

def factorial_menu():
    try:
        n = int(input("\nEnter a number to calculate its factorial: "))
    except ValueError:
        print("Please enter a whole number.")
        return
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return
    print(f"\nFactorial of {n} is: {factorial(n)}")
    if n <= 30:
        print(f"Fibonacci number {n} is: {fibonacci(n)}")

def filter_menu():
    flat = flatten(data)
    try:
        t = float(input("\nEnter a threshold value: "))
    except ValueError:
        print("Please enter a number.")
        return
    t = int(t) if t == int(t) else t
    way = input("1. Keep values >= threshold\n2. Keep values <= threshold\nEnter your choice: ").strip()
    if way == "2":
        result = filter_data(flat, t, keep_above=False)
        print(f"\nFiltered Data (values <= {t}):")
    else:
        result = filter_data(flat, t)
        print(f"\nFiltered Data (values >= {t}):")
    print(", ".join(map(str, result)) if result else "No values matched.")

    # map() with a lambda, as the assignment asks
    doubled = list(map(lambda x: x * 2, result))
    if doubled:
        print("Filtered values doubled:", ", ".join(map(str, doubled)))

def sort_menu():
    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")
    choice = input("\nEnter your choice: ").strip()
    rev = choice == "2"
    word = "Descending" if rev else "Ascending"

    if is_2d:
        new_grid = sorted([sorted(row) for row in data], reverse=rev)
        print(f"\nOriginal 2D list (unchanged, sorted() returns a new list):")
        show_grid(data)
        print(f"\nSorted rows in {word} Order:")
        show_grid(new_grid)
    else:
        data.sort(reverse=rev)   # changes the list itself
        print(f"\nSorted Data in {word} Order:")
        print(", ".join(map(str, data)))

def stats_menu():
    low, high, total, avg = get_statistics(flatten(data))
    print("\nDataset Statistics:")
    print("- Minimum value:", low)
    print("- Maximum value:", high)
    print("- Sum of all values:", total)
    print(f"- Average value: {avg:.2f}")

def show_menu():
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

def show_help():
    print("\nWhat each option does:")
    for f in (input_data, display_summary, factorial_menu,
              filter_menu, sort_menu, stats_menu):
        print(f"- {f.__name__}: {f.__doc__}")

def main():
    print("Welcome to the Data Analyzer and Transformer Program")
    show_help()

    while True:
        show_menu()
        choice = input("Please enter your choice: ").strip()

        if choice == "1":
            input_data()
        elif choice in ("2", "4", "5", "6") and not data:
            print("\nNo data yet. Please choose option 1 first.")
        elif choice == "2":
            display_summary()
        elif choice == "3":
            factorial_menu()
        elif choice == "4":
            filter_menu()
        elif choice == "5":
            sort_menu()
        elif choice == "6":
            stats_menu()
        elif choice == "7":
            print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break
        else:
            print("\nInvalid choice, please enter a number from 1 to 7.")
main()
