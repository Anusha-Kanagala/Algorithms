package com.java.learnings;

import apple.laf.JRSUIConstants;
import sun.jvm.hotspot.types.CIntegerField;

import java.util.ArrayList;
import java.util.List;

public class TwoSum {

    public int[] twoSum(int[] nums, int target) {
        int [] res = new int[2];
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    res[0] = i;
                    res[1] = j;
                }

            }
        }
        return res;
    }

    public static void main(String[] args) {
        TwoSum s = new TwoSum();
        int[] nums = new int[]{2, 7, 11, 15};
        int[] result = new int[2];
        result = s.twoSum(nums, 9);

        for(int i=0; i<result.length; i++)
        {
            System.out.println(result[i]);
        }
    }
}

