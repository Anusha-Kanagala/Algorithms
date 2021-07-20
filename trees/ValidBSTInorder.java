package com.java.learnings;

class TreeNodeBTInorder {
    int val;
    TreeNodeBTInorder left;
    TreeNodeBTInorder right;

    TreeNodeBTInorder() {
    }

    TreeNodeBTInorder(int val) {
        this.val = val;
    }

    TreeNodeBTInorder(int val, TreeNodeBTInorder left, TreeNodeBTInorder right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class ValidBSTInorder {
    Integer prev;
    public boolean isValidBSTInorder(TreeNodeBTInorder root){
        prev = null;
        return inOrderBST(root);

    }
    public boolean inOrderBST(TreeNodeBTInorder root){
        if(root == null){
            return true;
        }
        if(inOrderBST(root.left) == false){
            return false;
        }
        if(prev != null && root.val <= prev)
        {
            return false;
        }
        prev = root.val;
        return inOrderBST(root.right);
    }
}
class ValidateInorderBSTDriver {
    public static void main(String args[]) {
        ValidBSTInorder b = new ValidBSTInorder();
        /*TreeNodeBTInorder t2 = new TreeNodeBTInorder(1, null, null);
        TreeNodeBTInorder t3 = new TreeNodeBTInorder(3, null, null);
        TreeNodeBTInorder t1 = new TreeNodeBTInorder(2, t2, t3);*/
       /* TreeNodeBTInorder t2 = new TreeNodeBTInorder(-1,null,null);
        TreeNodeBTInorder t1 = new TreeNodeBTInorder(0,t2,null);*/
        TreeNodeBTInorder t4 = new TreeNodeBTInorder(3,null,null);
        TreeNodeBTInorder t5 = new TreeNodeBTInorder(7,null,null);
        TreeNodeBTInorder t3 = new TreeNodeBTInorder(6,t4,t5);
        TreeNodeBTInorder t2 = new TreeNodeBTInorder(4,null,null);
        TreeNodeBTInorder t1 = new TreeNodeBTInorder(5,t2,t3);
        System.out.println(b.isValidBSTInorder(t1));

    }
}
