package com.java.learnings;


import java.util.concurrent.LinkedBlockingQueue;

public class LinkedBlockingQueueSample {
    public static void main(String args[]) throws InterruptedException {
        int capacity = 10;
        LinkedBlockingQueue<Integer> lbq = new LinkedBlockingQueue<Integer>(capacity);

        lbq.add(1);
        lbq.add(2);
        lbq.add(3);
        lbq.add(5);
        lbq.add(100);
        lbq.add(19);
        lbq.add(34);
        lbq.add(56);
        lbq.add(80);
        lbq.add(78);
        lbq.add(78);
        System.out.println("Linked Blocking Queue bounded"+lbq);
        lbq.take();
        System.out.println("After take:"+lbq);
        lbq.put(3);
        System.out.println("After put 3:"+lbq);
        lbq.take();
        System.out.println("After take:"+lbq);
        lbq.offer(4);
        System.out.println("After offer 4:"+lbq);
        lbq.poll();
        System.out.println("After poll:"+lbq);
        if(!lbq.remove(8)){
            System.out.println("object not exists");
        }
        else{
        System.out.println(lbq);}
        if(!lbq.remove(100)){
            System.out.println("object 100 not exists");
        }
        else{

            System.out.println("Object 100 exists:"+lbq);}

    }
}
