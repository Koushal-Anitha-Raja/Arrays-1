class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        #creating a m cross n matrix 
        m=len(mat)
        #column accessing in matrix
        n=len(mat[0])
        #assigning all the matrix values to be zero
        result=[0] * (m*n)
        #initially flag is zero because we will go upwards first 
        flag=1
        #index for iterating in the matrix
        index=0
        #row and column is going to change so
        r=0
        c=0
        
        #check all the elements in m * n ie 12 elements here
        while(index<len(result)):
            #accessing the first element
            result[index]=mat[r][c]
            #up
            
            if flag==1:
                #if the column hits the last column
                if c==n-1:
                    #incrementing the row by one
                    r+=1
                    #and changing the flag varible to -1 if going upward
                    flag=-1
                    #if the row hits the first row
                elif r==0:
                    #increment colum by one
                    c+=1
                    # #and changing the flag varible to -1 if going upward
                    flag=-1
                #increment the column and decrement the row at every upward movement    
                else:
                    r-=1
                    c+=1
                    
            #downwards
            else:
                #if the downward approach hit the last row 
                if r==m-1:
                    c+=1
                #change the flag variable to 1 if moving downwards
                    flag=1
                # #if the downward approach hit the last column    
                elif c==0:
                    r+=1
                    #change the flag variable to 1 if moving downwards
                    flag=1
                #increment the row and decrement the column at each downward move
                else:
                    c=-1
                    r+=1
                    
            index+=1      
                    
        return result          
#time complexity:o(m*n)
#space complexity:o(m+n)