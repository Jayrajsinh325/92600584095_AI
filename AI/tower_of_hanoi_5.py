# 5.Write a program to solve Towar of Hanoi problem.
# Name :- Jayrajsinh Jadeja
# Enrollment :- 92600584095

# Tower of Hanoi

def tower_of_hanoi (n, source, helper, destination):
    if n==1:
        print("Move Disk 1 from", source, "to", destination)
        return

    tower_of_hanoi(n-1, source, destination, helper)
    print("Move Disk", n,"from", source, "to", destination)
    tower_of_hanoi(n-1, helper, source, destination)

# Number of disks
n=int(input("Enter number of disks: "))

# solve Tower of Hanoi
tower_of_hanoi(n, "A", "B", "C")

# Total number of moves
print("Total moves:",(2 ** n)-1)