package com.java.learnings;

public class Container_With_Most_Water {
    public int maxArea(int[] height) {
        int area_old = 0, area_new = 0;
        int low = 0, high = height.length -1;
        while (low < high){
            area_new = Math.min(height[low],height[high]) * (high - low);

            if (area_new > area_old){
                area_old = area_new;
            }

            if (height[low] < height [high]){
                low = low +1;
            }
            else{
                high = high -1;
            }
        }


        return area_old;
    }
}
class maxAreaDriver{
    public static void main(String args[]){
        Container_With_Most_Water c = new Container_With_Most_Water();
        int[] height = {1,8,6,2,5,4,8,3,7};
        int maxArea = c.maxArea(height);
        System.out.println(maxArea);
    }
}

