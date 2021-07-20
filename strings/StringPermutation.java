package com.java.learnings;

public class StringPermutation {
    public void stringPerm(String str, String remaining) {
        if (remaining == "") {
            System.out.println("\t"+str + " ");
        } else {
            for (int i = 0; i < remaining.length(); i++) {
                String next = str + remaining.charAt(i);
                String remaining_str = remaining.substring(0,i)+remaining.substring(i + 1);

                stringPerm(next, remaining_str);

            }
        }
    }
}
class StringPermDriver{
    public static void main(String args[]){
        StringPermutation s = new StringPermutation();
        s.stringPerm("","ABC");
    }
}
