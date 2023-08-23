def find_next_empty(puzzle):
    """find next row,col on the puzzle that's not filled yet (which will be -1) return (None,None) if there is none"""
    for i in range(9):
        for j in range(9):
            if puzzle[i][j]==-1:
                return (i,j)
    return (None,None)

def is_valid(puzzle,row,col,guess):
    '''return that guess at row/col is valid or not'''
    for i in range(9):
        if puzzle[row][i]==guess:
            return False
        if puzzle[i][col]==guess:
            return False
    outerboxrow=row//3
    outerboxcol=col//3
    for i in range(outerboxrow*3,outerboxrow*3+3):
        for j in range(outerboxcol*3,outerboxcol*3+3):
            if puzzle[i][j]==guess:
                return False
    return True
    
def solve_suduko(puzzle):
    """puzzle is a list of list , where each inner list is row of puzzle
    it will return the solution of suduko if it exists"""
    
    row,col=find_next_empty(puzzle) #step 1: choose a place where we have to make a guess
    if row==None:
        return True
    
    # step 2: if there is a place to guess ,try between 1 and 9
    for guess in range(1,10):
        if is_valid(puzzle,row,col,guess):
            # if this is valid guess place it on puzzle
            puzzle[row][col]=guess
            # now recurse using this puzzle
            # recursively call the function
            if solve_suduko(puzzle):
                return True
        #if not valid  ,then we need to backtrack
        puzzle[row][col]=-1
        
    #if none of our combinations we try not worked
    return False
if __name__=="__main__":
    test_board=[[3,9,-1,  -1,5,-1,  -1,-1,-1],
                [-1,-1,-1, 2,-1,-1, -1,-1,5],
                [-1,-1,-1, 7,1,9,   -1,8,-1],
                
                [-1,5,-1,  -1,6,8,  -1,-1,-1],
                [2,-1,6,  -1,-1,3,  -1,-1,-1],
                [-1,-1,-1, -1,-1,-1, -1,-1,4],
                
                [5,-1,-1, -1,-1,-1, -1,-1,-1],
                [6,7,-1,   1,-1,5,  -1,4,-1],
                [1,-1,9,  -1,-1,-1,  2,-1,-1]]
    print(solve_suduko(test_board))
    print(test_board)