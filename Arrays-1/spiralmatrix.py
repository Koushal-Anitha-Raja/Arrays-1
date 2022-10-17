class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    #creating a m cross n matrix 
        m=len(matrix)
        #column accessing in matrix
        n=len(matrix[0])
        
        #assigning the corner values by m and n values
        left=0
        right=n-1
        top=0
        bottom=m-1
        
        
        #creating a result variable to append the values
        result=[0] *(m*n)
        index=0
        
        
        #we need to check both the top,bottom and left ,right crosses each other
        while(index<(m*n)):
            #from left to right
            for i in range (left,right+1):
                #append the i th row matrix in the result 
                result[index]= matrix[top][i]
                index+=1
                #then increment the top by one 
            top+=1   
            
            #top to bottom 
            #iterate from top to bottom as usual in before iteration
            for j in range (top,bottom+1):
                result[index]= matrix[j][right]
                index+=1
                #decrement right by one
            right-=1
            
            if index==(m*n):
                break
            
            
            #right to left
            #reverse iterate through right to left
            for k in range(right,left-1,-1):
                result[index]= matrix[bottom][k]
                index+=1
                #decrement bottom by one
            bottom-=1    
            
            #bottom to top
            #iterate reversevely from bottom to top 
            for l in range (bottom,top-1,-1):
                result[index] =matrix[l][left]
                index+=1
            #increment left by one
            left+=1
                
            
        return result    
            
     #time complexity :o(m*n)
    #space complexity:o(1)
            
            
            
                