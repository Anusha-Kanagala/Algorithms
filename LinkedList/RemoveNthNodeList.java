package com.java.learnings;

class ListNodeR {
    int val;
    ListNodeR next;
    ListNodeR() {}
    ListNodeR(int val) { this.val = val; }
    ListNodeR(int val, ListNodeR next) { this.val = val; this.next = next; }
}

public class RemoveNthNodeList {
    public ListNodeR removeNthFromEnd(ListNodeR head, int n) {

        ListNodeR dummy = new ListNodeR(0,head);
        ListNodeR dummy2 = new ListNodeR(0,head);
        ListNodeR node = head;
        
        for(int i = 0; i<n;i++){
            if(head.next == null){
                return node.next;
            }
            head = head.next;
            dummy = dummy.next;

        }
        if(head != null){
            head = head.next;
            dummy = dummy.next;
        }
        if(head == dummy){
            return null;
        }
        if(dummy != null)
        {
            dummy.next = dummy.next.next;
            return dummy2.next;
        }
        else{
            return null;
        }

    }

}

class RemoveNodeDriver{
    public static void main(String args[]){
        RemoveNthNodeList  r = new RemoveNthNodeList();
       /* ListNodeR l5 = new ListNodeR(5,null);
        ListNodeR l4 = new ListNodeR(4,l5);
        ListNodeR l3 = new ListNodeR(3,l4);*/
        ListNodeR l2 = new ListNodeR(2,null);
        ListNodeR l1 = new ListNodeR(1,l2);
        r.removeNthFromEnd(l1,2);
    }
}
