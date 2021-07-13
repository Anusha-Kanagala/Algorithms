package com.java.learnings;
import java.lang.Math;

public class LongestSubstring {

    public int lengthOfLongestSubstring(String S) {
        int n = S.length(),str_len = 0;
        String str_old = "" ,str_new="";
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                String c = String.valueOf(S.charAt(j));
                str_new = c;
                while (j+1 != n) {
                    if (S.charAt(j) == S.charAt(j + 1) || str_new.contains(String.valueOf(S.charAt(j + 1)))) {
                        if(str_new.length() > str_old.length())
                            str_old = str_new;
                        j=n-2;

                    } else if (S.charAt(j) != S.charAt(j + 1)) {
                        str_new += String.valueOf(S.charAt(j+1));
                    }
                    j++;
                    if(str_new.length() > str_old.length())
                    str_old = str_new;

                }
            }
        }
        str_len = str_old.length();
        //System.out.println(str_old + " " + str_new);
      return str_len;
    }
}
class LSDriver{
    public static void main(String args[]){
        LongestSubstring l = new LongestSubstring();
        String LS = new String();
        LS = "pwwkew";
        int s=l.lengthOfLongestSubstring(LS);
        System.out.println(s);
    }
}

