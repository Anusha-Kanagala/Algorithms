package com.java.learnings;

class ListNodeMerge {
     int val;
     ListNodeMerge next;
     ListNodeMerge() {}
     ListNodeMerge(int val) { this.val = val; }
     ListNodeMerge(int val, ListNodeMerge next) { this.val = val; this.next = next; }
 }

public class MergeTwoSortedLists {
    public ListNodeMerge mergeTwoLists(ListNodeMerge l1, ListNodeMerge l2) {
        ListNodeMerge head = new ListNodeMerge();
        ListNodeMerge currNode = head;

        while(l1.next != null && l2.next != null){

            if (l1.val <= l2.val) {
                currNode.val = l1.val;
                l1 = l1.next;
            }
            else   {
                    head.val = l2.val;
                    l2 = l2.next;
                }
            ListNodeMerge newNode = new ListNodeMerge();
            currNode.next = newNode;
            currNode = currNode.next;

        }

        if (l1.next == null){
            currNode.next = l2.next;
        }
        else{
            currNode.next = l1.next;
        }

        return head;
    }
}

class SortedListDriver {
    public static void main(String args[]) {
        MergeTwoSortedLists mt = new MergeTwoSortedLists();
        ListNodeMerge l1_3 = new ListNodeMerge(4, null);
        ListNodeMerge l1_2 = new ListNodeMerge(2, l1_3);
        ListNodeMerge l1 = new ListNodeMerge(1, l1_2);
        ListNodeMerge l2_3 = new ListNodeMerge(4, null);
        ListNodeMerge l2_2 = new ListNodeMerge(3, l2_3);
        ListNodeMerge l2 = new ListNodeMerge(1, l2_2);
        mt.mergeTwoLists(l1, l2);
    }
}
