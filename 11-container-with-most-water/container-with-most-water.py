class Solution:
    def maxArea(self, height: list[int]) -> int:
        i=0
        j= len(height)-1
        maxi=0
        while (i<j):
            length = min(height[i],height[j])
            breadth = j-i
            area = length * breadth
            if area > maxi:
                maxi=area 
            if height[i]< height[j]:
                i+=1
            else :
                j-=1
        return maxi
        