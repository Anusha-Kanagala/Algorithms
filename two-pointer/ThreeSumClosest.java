package com.java.learnings;


import java.util.Arrays;

public class ThreeSumClosest {
    public int threeSumClosest(int[] nums, int target) {
        int result=0,stepCount = Integer.MAX_VALUE;
        for(int i=0 ;i<nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                for (int k = j + 1; k < nums.length; k++) {
                    int curr_stepCount = Math.abs((nums[i] + nums[j] + nums[k] - target));
                    if (curr_stepCount <= stepCount || curr_stepCount == 0) {
                        stepCount = curr_stepCount;
                        result = nums[i] + nums[j] + nums[k];
                    }
                    else if(nums.length <=3){
                        stepCount = stepCount;
                        result = nums[i] + nums[j] + nums[k];
                    }
                }
            }
        }
        return result;
    }
}
class ThreeSumClosestDriver {
    public static void main(String args[]) {
        ThreeSumClosest ts = new ThreeSumClosest();
        int[] nums = {-1,2,1,-4};
        //int[] nums = {0,1,2};
        int target = 1;
        int result = ts.threeSumClosest(nums,target);
        System.out.println(result);
    }
}

