"""
* * * * *
* * * *
* * *
* *
*

row = 1, row <= 5
print *, 5 -(row - 1) times
increase row by 1

row         print *         rule
1           5               5 - (1-1) = 5 stars
2           4               5 - (2-1) = 4 stars
3           3               5 - (3-1) = 3 stars
4           2               5 - (4-1) = 2 stars
5           1               5 - (5-1) = 1 stars
"""

for row in range(1, 6):
    for col in range(5 - (row - 1)):
        print('*', end=" ")
    print()