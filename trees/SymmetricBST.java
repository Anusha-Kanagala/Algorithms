package com.java.learnings;
class TreeNodeBTSymmetric {
    int val;
    TreeNodeBTSymmetric left;
    TreeNodeBTSymmetric right;

    TreeNodeBTSymmetric() {
    }

    TreeNodeBTSymmetric(int val) {
        this.val = val;
    }

    TreeNodeBTSymmetric(int val, TreeNodeBTSymmetric left, TreeNodeBTSymmetric right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
public class SymmetricBST {
    public boolean isSymmetric(TreeNodeBTSymmetric root) {
        TreeNodeBTSymmetric r1 =root,r2 = root;
        return isEqual(r1,r2);
    }

    public boolean isEqual(TreeNodeBTSymmetric n1,TreeNodeBTSymmetric n2){
        if(n1 == null && n2 == null){
            return true;
        }
        if(n1== null || n2 == null){
            return false;
        }

        return (n1.val == n2.val) && isEqual(n1.left,n2.right) && isEqual(n1.right,n2.left);
    }
}
class SymmetricDriver{
    public static void main(String args[]){
        TreeNodeBTSymmetric t = new TreeNodeBTSymmetric();
        SymmetricBST s = new SymmetricBST();
        TreeNodeBTSymmetric t7 = new TreeNodeBTSymmetric(3);
        TreeNodeBTSymmetric t6 = new TreeNodeBTSymmetric(4);
        TreeNodeBTSymmetric t5 = new TreeNodeBTSymmetric(4);
        TreeNodeBTSymmetric t4 = new TreeNodeBTSymmetric(3);
        TreeNodeBTSymmetric t3 = new TreeNodeBTSymmetric(2,t6,t7);
        TreeNodeBTSymmetric t2 = new TreeNodeBTSymmetric(2,t4,t5);
        TreeNodeBTSymmetric t1 = new TreeNodeBTSymmetric(1, t2, t3);
        System.out.println(s.isSymmetric(t1));
    }
}
