//https://leetcode.com/problems/container-with-most-water/

class Solution {
    public int maxArea(int[] height) {        
        
        int breadth = height.length-1;
        
        if (height.length < 2)
            return 0;
        else if (height.length == 2)
            return Math.min(height[0], height[1])*breadth;
        
        int i = 0, j = breadth, area = 0;
        int left = height[i], right = height[j];         
        area = Math.min(left, right)*breadth;
        
        while (i<j){          
            if(left <= right){
                i++;
                left = height[i];                   
            }
            else{
                j--;
                right = height[j];   
            }            
            breadth--;                       
            area = Math.max(area, Math.min(left, right)*breadth);            
        }           
        return area;        
    }
}
