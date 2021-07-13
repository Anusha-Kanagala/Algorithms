package com.java.learnings;

import java.util.HashSet;
import java.util.Set;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class BinaryTreeSum {
    public boolean findTarget(TreeNode root, int k) {
        Set <Integer> targetSet = new HashSet<Integer>();
        if (root == null) {
            return false;
        } else {

        boolean flag = ifSumExists(root,k,targetSet);
            return flag;
        }
    }

    public boolean ifSumExists(TreeNode node, int k, Set< Integer > targetSet){
        //boolean exists=false;
        if(node == null){
            return false;
        }
        if(targetSet.contains(k-node.val)){
            return true;
        }
        targetSet.add(node.val);
        return ifSumExists(node.left,k,targetSet) || ifSumExists(node.right,k,targetSet);
        /*if(node.left != null){
          exists = ifSumExists(node.left,k,targetSet);
        }
        if(node.right != null){
            exists = ifSumExists(node.right,k,targetSet);
        }
        return exists;*/
    }
}
class BinaryTreeSumDriver{
    public static void main(String args[]){
        TreeNode t4 = new TreeNode(2);
        TreeNode t5 = new TreeNode(4);
        TreeNode t6 = new TreeNode(7);
        TreeNode t3 = new TreeNode(6,null,t6);
        TreeNode t2 = new TreeNode(3,t4,t5);
        TreeNode t1 = new TreeNode(5,t2,t3);
        BinaryTreeSum b = new BinaryTreeSum();
        boolean flag = b.findTarget(t1,9);
        System.out.println(flag);
    }
}



