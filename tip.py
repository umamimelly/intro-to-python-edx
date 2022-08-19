# .. this has been my least favorite practice project so far. tip calculator that removes the string, converts variable to float, and then math happens.


def main():
    dollars = dollars_to_float(input("How much was the meal?: "))
    percent = percent_to_float(input("What percentage would you like to tip?: "))
    tip = percent*.01*dollars
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollars =  d.strip("$")
    d = float(dollars)
    return d

def percent_to_float(p):
    percent = p.strip("%")
    p = float(percent)
    return p

main()
