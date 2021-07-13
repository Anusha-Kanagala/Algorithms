package com.java.learnings;

public class GcdStrings {
    public String gcdOfStrings(String str1, String str2) {

       if(str1.length()<str2.length()){
           return gcdOfStrings(str2,str1);
       }
       else if(!str1.startsWith(str2)){
           return "";
       }
      else if (str2.isEmpty()){
           return str1;
       }

        else{
            return gcdOfStrings(str1.substring(str2.length()),str2);
        }
    }
}
class GCDDriver{
    public static void main(String args[]){
        GcdStrings g = new GcdStrings();
        String str1 = "ABABAB";
        String str2 = "ABAB";
        String result = g.gcdOfStrings(str1,str2);
        System.out.println(result);
    }
}
