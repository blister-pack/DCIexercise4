def sum():
    #  I'm pretty sure that this function should receive
    #  the numbers as arguments and not like this
    num1 = int(input("first number to sum "))
    num2 = int(input("second number to sum "))
    num3 = int(input("third number to sum "))
    return f"The sum of your numbers is {num1 + num2 + num3}"


def num_comparison(num1, num2):
    if num1 > 10000 and num2 > 10000:
        print(
            "those are some pretty big numbers you got there... yep.. pretty big numbers"
        )
    elif num1 > num2:
        print("the first number is greater than the second")
    elif num1 < num2:
        print("the second number is greater than the first")
    elif num1 == num2:
        print("these numbers are equal :D")


def biggest_of_five():
    print("Let's get you the biggest out of 5 numbers, exciting I know")
    num_list = []
    for i in range(0, 5):
        i = int(input("Gimme a number "))
        num_list.append(i)
    return max(num_list)


def days_in_month(month: str):
    day31_months = ["January", "March", "May", "July", "August", "October", "December"]
    day30_months = ["April", "June", "September", "November"]
    complicated_month = "February"

    if month in day31_months:
        return f"31 days in that month eheh"
    elif month in day30_months:
        return f"30 days in that month, a bit smaller aw"
    elif month == complicated_month:
        return f"Let's not talk about that month, it's weird"
    else:
        return f"idk that month :D"


def even_and_divisible_by3(number):
    if number % 2 == 0 and number % 3 == 0:
        return f"{number} is even and divisible by 3"
    else:
        return f"I hate this number"


# ----------------------------------------------------------
print(sum())
print(
    num_comparison(
        int(input("First number to compare ")), int(input("Second number to compare "))
    )
)
#  I really hate this syntax tbh

print(biggest_of_five())
print(days_in_month(input("Gimme a month aaaaah ")))
print(even_and_divisible_by3(int(input("Give me a pretty number "))))
