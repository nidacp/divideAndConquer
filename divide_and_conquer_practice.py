import math

def new_array(size: int):
    L = [0] * size
    return L

def printGrid(grid:list) -> None:
    for i in grid:
        for j in i:
            print(j, end=" ")
        print()

# Problem 1: SQUARES
def squares(grid:list) -> None:
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            # for every white unvisited box in grid, print the size of its cluster
            if grid[i][j]=='w':
                print(count(grid, j, i))


def count(grid:list, x:int, y:int) -> int:
    # if square is outside bounds, return 0
    if y>=len(grid) or y<0 or x>=len(grid[0]) or x<0:
        return 0
    # if square is black or already visited, return 0
    if grid[y][x]=='b' or grid[y][x]=='W':
        return 0
    # if the square is white and unvisited, mark it as visited and call recursively
    if grid[y][x]=='w':
        grid[y][x]='W'
        return 1 + count(grid, x+1, y) + count(grid, x-1, y) + count(grid, x, y+1) + count(grid, x, y-1)

    # oh no! the function hasn't returned yet so there's a square that isn't 'w', 'W', or 'b' somehow.
    print("Something has gone wrong while checking x=" + str(x) + ", y=" + str(y))
    return 0




# Problem 2: INVERSIONS
def inversions(arr:list) -> int:
    return invSort(arr,0,len(arr)-1)

# Break down the list
# Re-merge list
# While re-merging: if it's smaller than the largest number of the other array, add that pair. If it's smaller than the second to largest, add that pair. etc.


def invSort(arr:list, left:int, right:int) -> int:
    #print("BACK IN INVSORT.")
    if left<right:
        mid = (left+right)//2
        #print("    calling with arr = " + str(arr) + ", left = " + str(left) + ", mid = " + str(mid))

        linv = invSort(arr, left, mid)
        #print("    calling with arr = " + str(arr) + ", mid+1 = " + str(mid+1) + " , right = " + str(right))

        rinv = invSort(arr, mid+1, right)
        #print("    linv = ", linv, " rinv = ", rinv)

        return linv+rinv+weirdInversionMerge(arr, left, mid, right)
    return 0



def weirdInversionMerge(arr:list, left:int, mid:int, right:int) -> int:
    #print("BACK IN WEIRDINVERSIONMERGE.")
    # creating temp arrays. larr = left array, rarr = right array
    larr = splice(arr, left, mid+1)
    rarr = splice(arr, mid+1, right+1)

    # combine the temp arrays back into arr
    i = 0
    j = 0
    k = left
    # total number of inversions
    inv = 0
    while i < len(larr) and j < len(rarr):
        #if the left element is smaller, all is right with the world. just add it
        if larr[i] <= rarr[j]:
            arr[k] = larr[i]
            i += 1
        #if the right element is smaller, something unsorted and annatural has happened.
        #add to the inversion count the amount of left elements that are larger than the right element
        else:
            arr[k] = rarr[j]
            j += 1
            inv += (len(larr) - i)
        k+=1
        #print("    i=", i, ", j=", j, ", k=", k, ", inversions=", inv)

    # copy over remaining elements of larr and rarr
    while i < len(larr):
        arr[k] = larr[i]
        i+=1
        k+=1
    while j < len(rarr):
        arr[k] = rarr[j]
        j+=1
        k+=1

    return inv


def mergeSortY(arr:list, left:int, right:int) -> None:
    if left<right:
        mid = (left+right)//2
        mergeSortY(arr, left, mid)
        mergeSortY(arr, mid+1, right)
        merge(arr, left, mid, right, 1)


def merge(arr:list, left:int, mid:int, right:int, axis:int) -> None:
    #print("Running merge. arr=", arr)
    # creating temp arrays
    larr = [[0] * 2 for _ in range(mid - left + 1)]
    rarr = [[0] * 2 for _ in range(right - mid)]

    #filling temp arrays
    for i in range(0, len(larr)):
        larr[i][0] = arr[left + i][0]
        larr[i][1] = arr[left + i][1]

    for j in range(0, len(rarr)):
        rarr[j][0] = arr[mid + 1 + j][0]
        rarr[j][1] = arr[mid + 1 + j][1]

    # combine the temp arrays back into arr
    i = 0
    j = 0
    k = left
    while i < len(larr) and j < len(rarr):
        if larr[i][axis] <= rarr[j][axis]:
            arr[k] = larr[i]
            i += 1
        else:
            arr[k] = rarr[j]
            j += 1
        k+=1

    # copy over remaining elements of larr and rarr
    while i < len(larr):
        arr[k] = larr[i]
        i+=1
        k+=1
    while j < len(rarr):
        arr[k] = rarr[j]
        j+=1
        k+=1

def mergeSortX(arr:list, left:int, right:int) -> None:
    if left<right:
        mid = (left+right)//2
        mergeSortX(arr, left, mid)
        mergeSortX(arr, mid+1, right)
        merge(arr, left, mid, right, 0)


# Problem 3: POINTS
def points(point_list:list) -> None:
    #Sort by Y and then by X
    mergeSortY(point_list, 0, len(point_list)-1)
    mergeSortX(point_list, 0, len(point_list)-1)
    # check the middle of everything. Smallest distance from left and right halves
    short = smallestPoints(point_list)
    #d = math.dist(short[0], short[1])

    print(str(short) + " are the two closest points.")

def smallestPoints(point_list:list) -> list:
    # Base case: 2 or 3 points
    if (len(point_list)==1):
        raise Exception("Only one point???? NOOOOOO!!!!!!! (Sorry, but we can't compare distance between a single point.)")
    if len(point_list)==2:
        return [point_list[0], point_list[1]]
    if len(point_list)==3:
        dist1 = math.dist(point_list[0], point_list[1])
        dist2 = math.dist(point_list[0], point_list[2])
        dist3 = math.dist(point_list[1], point_list[2])

        if min(dist3, min(dist1, dist2)) == dist3:
            return [point_list[1], point_list[2]]
        if min(dist3, min(dist1, dist2)) == dist2:
            return [point_list[0], point_list[2]]
        else:
            return [point_list[0], point_list[1]]


    else:
        # break in half and call smallest points
        median = (int)(len(point_list)/2)
        half1 = splice(point_list, 0, median)
        half2 = splice(point_list, median, len(point_list))
        # return smallest distance between the smallest points in the left and right
        # Recursively find the closest pairs in both halves
        lclosest = smallestPoints(half1)
        rclosest = smallestPoints(half2)

        # Find the smaller distance of the two
        ldist = math.dist(lclosest[0], lclosest[1])
        rdist = math.dist(rclosest[0], rclosest[1])
        min_dist = min(ldist, rdist)

        if min_dist == ldist:
            closest = lclosest
        else:
            closest = rclosest

        #checking in the middle strip in case the closest points are split by the median
        strip = [point for point in point_list if abs(point[0]-point_list[median][0]) < min_dist]
        for i in range(len(strip)):
            for j in range(i+1, len(strip)):
                temp_dist = math.dist(strip[i], strip[j])
                if temp_dist < min_dist:
                    min_dist = temp_dist
                    closest = [strip[i], strip[j]]

        return closest


# return a new list with the elements from l[lower] to l[upper]
def splice(l:list, lower:int, upper:int) -> list:
    #create a new list and fill it with the elements in the inputted range
    new_list = [0] * (upper-lower)
    for i in range(0, upper-lower):
        new_list[i]=l[lower+i]
    return new_list

def main(): # Test your code here.
    example_grid = [["b","b","b","b","b","b","b","b","b","b"],
        ["b","w","b","b","w","w","b","w","w","b"],
        ["b","b","b","b","b","w","b","w","w","b"],
        ["b","w","w","w","b","b","w","w","w","b"],
        ["b","w","b","w","b","w","w","b","b","b"],
        ["b","w","b","w","w","w","b","w","b","b"],
        ["b","w","b","b","b","b","w","w","w","b"],
        ["b","w","b","w","b","b","w","w","w","b"],
        ["b","w","b","w","b","b","w","w","w","b"],
        ["b","b","b","b","b","b","b","b","b","b"]]
    printGrid(example_grid)
    squares(example_grid)
    #Should be 1,3,21,10,2

    all_w = [["w","w","w","w","w"],
            ["w","w","w","w","w"],
            ["w","w","w","w","w"],
            ["w","w","w","w","w"],
            ["w","w","w","w","w"]]
    diag_w = [["w","w","w","w","b"],
             ["w","w","w","b","w"],
             ["w","w","b","w","w"],
             ["w","b","w","w","w"],
             ["b","w","w","w","w"]]
    all_b = [["b", "b", "b", "b", "b"],
            ["b", "b", "b", "b", "b"],
            ["b", "b", "b", "b", "b"],
            ["b", "b", "b", "b", "b"],
            ["b", "b", "b", "b", "b"]]
    printGrid(all_w)
    squares(all_w)
    #Should be 25
    printGrid(diag_w)
    squares(diag_w)
    #Should be 10,10
    printGrid(all_b)
    squares(all_b)
    #Should be 0

    print()
    example_array = [1,3,5,2,4,6]
    print("In ", example_array, ", there are :")
    print("", inversions(example_array), " inversions.")
    #Scrambled. Should be 3
    example_array2 = [1,3,5,8,7,2,4,6]
    print("In ", example_array2, ", there are :")
    print("", inversions(example_array2), " inversions.")
    #Scrambled. Should be 10
    sorted_arr = [1,2,3,4,5,6]
    print("In ", sorted_arr, ", there are :")
    print("", inversions(sorted_arr), " inversions.")
    #In order. Should be 0
    reversed_arr = [6, 5, 4, 3, 2, 1]
    print("In ", reversed_arr, ", there are :")
    print("", inversions(reversed_arr), " inversions.")
    #Reverse order. Should be 15
    print()

    # out of order, pair is split across median
    scrambled_points = [(1,1),(3,3),(-2,2),(5,2),(-2,0),(0,0),(4,0)]
    #out of order, pair is on the left of median
    left_points = [(30,30),(-1,-2),(60,60),(-2,-2),(0,0)]
    # out of order, pair is on the right of median
    right_points = [(1,1), (-100,100), (2,1), (50, 50), (-30, -17), (-50, -25), (-100, -10)]
    #given example
    example_points = [(-2,2),(-2,0),(0,0),(1,1),(3,3),(4,0),(5,2)]

    points(scrambled_points)
    # should be (0,0) and (1,1)
    points(left_points)
    #should be (-1, -2) and (-2, -2)
    points(right_points)
    #should be (1,1) and (2,1)
    points(example_points)
    # should be (0,0) and (1,1)




if __name__ == "__main__":
    main()


