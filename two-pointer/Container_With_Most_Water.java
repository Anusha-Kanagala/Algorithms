package com.java.learnings;

public class Container_With_Most_Water {
    public int maxArea(int[] height) {
        int area_old = 0, area_new = 0;
        for(int i = 0 ; i< height.length; i++) {
            for (int j = i+1; j < height.length; j++) {
                area_new = (j-i) * Math.min(height[i],height[j]);
                area_old = Math.max(area_new,area_old);
            }
        }
        return area_old;
    }
}
class maxAreaDriver{
    public static void main(String args[]){
        Container_With_Most_Water c = new Container_With_Most_Water();
        int[] height = {1,1};
        int maxArea = c.maxArea(height);
        System.out.println(maxArea);
    }
}

