#calculate e=mc^2. user inputs a figure, run number against formula, should output Energy.
def main():

    mass = int(input("m: "))
    print("E: ", energy(mass))

def energy(m):
    return (300000000**2) * m

main()
