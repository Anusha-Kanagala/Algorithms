package com.java.learnings;

import java.util.*;

public class FourSum {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Set<List<Integer>> finalList = new HashSet<List<Integer>>();
        Arrays.sort(nums);
        for (int i=0; i< nums.length; i++){
            for (int j=i+1; j< nums.length; j++){
                int k = j+1;
                int l = nums.length-1;

                while(k<l) {
                    int sum = nums[i]+ nums[j]+nums[k]+ nums[l];
                    if (sum == target) {
                        List<Integer> indexList = new ArrayList<Integer>();
                        indexList.add(nums[i]);
                        indexList.add(nums[j]);
                        indexList.add(nums[k]);
                        indexList.add(nums[l]);
                        finalList.add(indexList);
                        k++;
                        l--;
                    }
                    else if(sum < target){
                        k++;
                    }
                    else{
                        l--;
                    }
                }
            }
        }
        List<List<Integer>> ls = new ArrayList<List<Integer>>();
        for (List<Integer> element: finalList) {
            ls.add(element);
        }
        return ls;
    }

}
class FourSumDriver {
    public static void main(String args[]) {
        FourSum fs = new FourSum();
        List<List<Integer>> finalList = new ArrayList<List<Integer>>();
       // int[] nums = {1,0,-1,0,-2,2};
        //int target = 0;
        int[] nums = {2,2,2,2,2};
        int target =8;
        finalList = fs.fourSum(nums,target);
        for (List<Integer> number : finalList) {
            System.out.print(number);
        }
    }
}

