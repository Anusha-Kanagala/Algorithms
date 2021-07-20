package com.java.learnings;
/*Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 */
class TreeNodeBTEqual {
    int val;
    TreeNodeBTEqual left;
    TreeNodeBTEqual right;

    TreeNodeBTEqual() {
    }

    TreeNodeBTEqual(int val) {
        this.val = val;
    }

    TreeNodeBTEqual(int val, TreeNodeBTEqual left, TreeNodeBTEqual right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
public class EqualBST {
    public boolean isSameTree(TreeNodeBTEqual p, TreeNodeBTEqual q) {

        if(p == null || q== null){
            return true;
        }
        if(p.val != q.val){
            return false;
        }
        return isSameTree(p.right, q.right) && isSameTree(p.left,q.left);
    }
}
class EqualBSTDriver{
    public static void main(String args[]){
        EqualBST e = new EqualBST();
        TreeNodeBTEqual t3 = new TreeNodeBTEqual(2);
        TreeNodeBTEqual t2 = new TreeNodeBTEqual(1);
        //TreeNodeBTEqual t1 = new TreeNodeBTEqual(1, null, t2);
        TreeNodeBTEqual t6 = new TreeNodeBTEqual(2);
        TreeNodeBTEqual t5 = new TreeNodeBTEqual(1,null,t6);
        //TreeNodeBTEqual t4 = new TreeNodeBTEqual(1, null, );
        System.out.println(e.isSameTree(t2,t5));
    }
}
