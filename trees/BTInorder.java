package com.java.learnings;

import apple.laf.JRSUIUtils;

import java.awt.*;
import java.util.ArrayList;
import java.util.List;

class TreeNodeBT {
    int val;
    TreeNodeBT left;
    TreeNodeBT right;

    TreeNodeBT() {
    }

    TreeNodeBT(int val) {
        this.val = val;
    }

    TreeNodeBT(int val, TreeNodeBT left, TreeNodeBT right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
public class BTInorder {
    List<Integer> resultList = new ArrayList<Integer>();
    public List<Integer> inorderTraversal(TreeNodeBT root) {

    if(root == null){
        return resultList;
    }
    if(root.left!= null){
        inorderTraversal(root.left);
    }

    if(root!= null){
        resultList.add(root.val);
    }
    if(root.right !=null){
        inorderTraversal(root.right);
    }

    return resultList;
    }
}
class BTInorderDriver{
    public static void main(String args[]) {
        TreeNodeBT t3 = new TreeNodeBT(3);
        TreeNodeBT t2 = new TreeNodeBT(2, t3, null);
        TreeNodeBT t1 = new TreeNodeBT(1, null, t2);
        BTInorder bt = new BTInorder();
        List<Integer> inorderList = new ArrayList<Integer>();
        inorderList = bt.inorderTraversal(t1);
        for(int i:inorderList){
            System.out.println(i);
        }
    }
}


