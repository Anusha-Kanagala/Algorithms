package com.java.learnings;
/*You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 */
class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

public class AddNumbersLinkedList {
    ListNode head = new ListNode(0,null);
    ListNode l3 = head;
    int carry = 0;
    int sum = 0;
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        while (l1 != null || l2 != null) {
            int x = (l1!=null) ? l1.val:0;
            int y = (l2!=null) ? l2.val:0;
            sum = x + y+carry;
            carry = sum / 10;
            if (sum > 9) {
                l3 = (l3.next = new ListNode(sum%10));
            } else {

                l3 = (l3.next = new ListNode(sum));
            }
            if(l1!=null)l1 = l1.next;
            if(l2!=null) l2 = l2.next;
        }
        if(carry>0){
            l3.next = new ListNode(carry);
        }
        return head.next;
    }

}
class AddListDriver{
    public static void main(String args[]){
        AddNumbersLinkedList a = new AddNumbersLinkedList();
        ListNode l13 = new ListNode(3,null);
        ListNode l12 = new ListNode(2,l13);
        ListNode l1_head = new ListNode(1,l12);
        ListNode l23 = new ListNode(3,null);
        ListNode l22 = new ListNode(2,l23);
        ListNode l2_head = new ListNode(1,l22);
        a.addTwoNumbers(l1_head,l2_head);
    }
}
