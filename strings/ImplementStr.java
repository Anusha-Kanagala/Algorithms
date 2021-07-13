package com.java.learnings;

public class ImplementStr {
    public int strStr(String haystack, String needle) {
        int indx = 0, count = 0,i = 0;
        if (needle.length() == 0){
            return 0;
        }
        int len_haystack = haystack.length();
        for(int j=0; j<needle.length() && i<len_haystack;){
            if(haystack.charAt(i) == needle.charAt(j)){
                count++;
                j++;
                i++;
            }
            else{
                count =0 ;
                i = Math.abs(Math.abs(count - j) - i -1);
                j=0;
            }


        }
        if(count == 0 || count!= needle.length()){
            return -1;
        }
        else{
            indx = Math.abs(count-i);
            return indx;
        }
    }
}

class ImplementStrDriver{
    public static void main(String args[]){
        ImplementStr  i = new ImplementStr();
        String haystack = "mississippi";
        String needle = "issip";
        int indx  = i.strStr(haystack,needle);
        System.out.println(indx);
    }
}

