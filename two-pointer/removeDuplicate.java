package com.java.learnings;

import org.apache.commons.lang3.ArrayUtils;
import sun.lwawt.macosx.CSystemTray;


public class removeDuplicate {
    public int removeDuplicates(int[] nums) {
        int count =0;
            for(int j = 1; j<nums.length; j++) {
                if(nums[j]!=nums[count]) {
                    count++;
                    nums[count] = nums[j];
                }
            }

        for(int k =0; k<=count;k++){
            System.out.println(nums[k]);
        }
        return count+1;
    }
}
class removeDuplicateDriver{
    public static void main(String args[]){
        removeDuplicate r = new removeDuplicate();
        int nums[] = {0,0,1,1,1,2,2,3,3,4};
        int l = r.removeDuplicates(nums);
        System.out.println(l);

    }
}
