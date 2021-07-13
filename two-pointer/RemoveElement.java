package com.java.learnings;

public class RemoveElement {
    public int removeElement(int[] nums, int val) {
        int count =0;
        if(nums.length == 0){
            return 0;
        }
        for(int j = 0; j<nums.length; j++) {
            if(nums[j]!=val) {

                nums[count] = nums[j];
                count++;
            }
        }

        for(int k =0; k<count;k++){
            System.out.println(nums[k]);
        }
        return count;
    }
}
class removeElementDriver{
    public static void main(String args[]){
        RemoveElement r = new RemoveElement();
        int nums[] = {3,2,2,3};
        int value = 3;
        int l = r.removeElement(nums,value);
        System.out.println(l);
    }
}

