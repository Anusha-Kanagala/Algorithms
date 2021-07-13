package com.java.learnings;

class TreeNodeBTValidate {
    int val;
    TreeNodeBTValidate left;
    TreeNodeBTValidate right;

    TreeNodeBTValidate() {
    }

    TreeNodeBTValidate(int val) {
        this.val = val;
    }

    TreeNodeBTValidate(int val, TreeNodeBTValidate left, TreeNodeBTValidate right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class ValidateBST {
    boolean flag1 = false;
    boolean flag2 = false;
    int prev = 0;

    public boolean isValidBST(TreeNodeBTValidate root) {
        prev = root.val;
        return isValidRecu(root);

    }

    private boolean isValidRecu(TreeNodeBTValidate root) {
        if ((root == null || (root.right == null && root.left == null))) {

            return true;
        }

        if (root.left == null || !(root.val <= root.left.val) || root.right.val < prev) {

            flag1 = isValidRecu(root.left);
        }

        if (root.right == null || !(root.val >= root.right.val) &&  root.left.val > prev) {

            flag2 = isValidRecu(root.right);
        }
        return flag1 && flag2;
    }
}

class ValidateBSTDriver {
    public static void main(String args[]) {
        ValidateBST b = new ValidateBST();
        /*TreeNodeBTValidate t2 = new TreeNodeBTValidate(1, null, null);
        TreeNodeBTValidate t3 = new TreeNodeBTValidate(3, null, null);
        TreeNodeBTValidate t1 = new TreeNodeBTValidate(2, t2, t3);*/
       /* TreeNodeBTValidate t2 = new TreeNodeBTValidate(-1,null,null);
        TreeNodeBTValidate t1 = new TreeNodeBTValidate(0,t2,null);*/
        TreeNodeBTValidate t4 = new TreeNodeBTValidate(3,null,null);
        TreeNodeBTValidate t5 = new TreeNodeBTValidate(7,null,null);
        TreeNodeBTValidate t3 = new TreeNodeBTValidate(6,t4,t5);
        TreeNodeBTValidate t2 = new TreeNodeBTValidate(4,null,null);
        TreeNodeBTValidate t1 = new TreeNodeBTValidate(5,t2,t3);
        System.out.println(b.isValidBST(t1));

    }
}
