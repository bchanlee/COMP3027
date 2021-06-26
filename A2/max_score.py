from typing import List

"""
returns the max score from a traversal of the grid
:param height - height of grid (n)
:param width - width of grid (m)
:param grid - matrix of vertices (n x m)
:param budget - maximum budget allowed
"""
def max_score(
        height: int,
        width: int,
        grid: List[List[int]],
        cost_right: int,
        cost_up: int,
        budget: int) -> int:
        
    # Initialise OPT(i,j,b) =  M[i][j][b][0]
    # Initialise C(i,j,b) = M[i][j][b][1]
    M = [[[(-1,-1) for b in range(budget+1)] for j in range(height)] for i in range(width)]

    for i in range(width):
        for j in range(height):
            for b in range(budget+1):
                # base case OPT(0,0,b)
                if i == 0 and j == 0:
                    M[i][j][b] = (grid[j][i], 0)
                    continue
                # recurrence cases - grid[j][i] chosen
                tmp_max = float('-inf')
                tmp_max_cost = float('-inf')
                tmp_up = float('-inf')
                tmp_up_cost = float('-inf')
                tmp_right = float('-inf')
                tmp_right_cost = float('-inf')
                # recurrence cases - grid[j][i] not chosen
                tmp_not_up = float('-inf')
                tmp_not_up_cost = float('-inf')
                tmp_not_right = float('-inf')
                tmp_not_right_cost = float('-inf')
                tmp_not_max = float('-inf')
                tmp_not_max_cost = float('-inf')

                # case for right
                if i > 0:
                    # chosen
                    if b - cost_right >= 0:
                        tmp_right_cost = cost_right + M[i-1][j][b-cost_right][1]
                        if b - tmp_right_cost >= 0:
                            tmp_right = M[i-1][j][b-cost_right][0]
                    # not chosen
                    tmp_not_right = M[i-1][j][b][0]
                    tmp_not_right_cost = cost_right + M[i-1][j][b][1]
                # case for up
                if j > 0:
                    # chosen
                    if b - cost_up >= 0:
                        tmp_up_cost = cost_up + M[i][j-1][b-cost_up][1]
                        if b - tmp_up_cost >= 0:
                            tmp_up = M[i][j-1][b-cost_up][0]
                    # not chosen
                    tmp_not_up = M[i][j-1][b][0]
                    tmp_not_up_cost = cost_up + M[i][j-1][b][1]

                # find max of not chosen
                if tmp_not_right >= tmp_not_up:
                    tmp_not_max = tmp_not_right
                    tmp_not_max_cost = tmp_not_right_cost
                if tmp_not_right < tmp_not_up:
                    tmp_not_max = tmp_not_up
                    tmp_not_max_cost = tmp_not_up_cost
                # find max of chosen
                if tmp_right >= tmp_up:
                    tmp_max = tmp_right
                    tmp_max_cost = tmp_right_cost
                if tmp_right < tmp_up:
                    tmp_max = tmp_up
                    tmp_max_cost = tmp_up_cost
                tmp_max += grid[j][i]
                # find max of chosen and not chosen
                if tmp_max >= tmp_not_max:
                    M[i][j][b] = (tmp_max, tmp_max_cost)
                if tmp_max < tmp_not_max:
                    M[i][j][b] = (tmp_not_max, tmp_not_max_cost)

    return M[width-1][height-1][budget][0]

# TESTCASES
if __name__ == "__main__":
    # Test 1
    h = 3
    w = 3
    g1 = [
        [1,2,1],
        [1,2,2],
        [1,1,2]
    ]
    cr = 3
    cu = 2
    b = 10
    res1 = max_score(h, w, g1, cr, cu, b)
    assert(9 == res1)
    
    # Test 2
    h = 4
    w = 4
    g2 = [
        [5,4,6,8],
        [3,100,7,9],
        [8,3,3,10],
        [2,1,4,5]
    ]
    cr = 1
    cu = 3
    b = 10
    res2 = max_score(h, w, g2, cr, cu, b)
    assert(135 == res2)
    
    # Test 3
    h = 10
    w = 10
    g3 = [
        [4, 8, 7, 6, 5, 6, 7, 8, 7, 6],
        [5, 2, 8, 5, 5, 7, 6, 4, 8, 1],
        [6, 7, 7, 5, 6, 4, 5, 3, 2, 6],
        [7, 6, 6, 20, 8, 7, 6, 5, 3, 5],
        [8, 5, 6, 8, 0, 1, 2, 4, 5, 6],
        [9, 4, 8, 71, 6, 9, 5, 7, 8, 9],
        [1, 3, 5, 17, 1, 5, 8, 0, 8, 9],
        [3, 2, 5, 4, 5, 6, 76, 4, 34, 23],
        [6, 13, 7, 8, 9, 0, 5, 10, 10, 10],
        [2, 3, 4, 5, 6, 7, 10, 10, 10, 10]
    ]
    cr = 5
    cu = 5
    b = 40
    res3 = max_score(h, w, g3, cr, cu, b)
    assert(139 == res3)
