/*
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
*/


// solution vertically scans the strings
public class Solution {

    public String longestCommonPrefix(String[] strs){
        if (strs.length == 0)   return "";
        int strlen = 0, index = 0, count = 0;
        int mL = strs[0].length();
        if (strs.length == 1)   return strs[0];
        String str0 = strs[0];
        for (String s: strs)    mL = (s.length() < mL) ? s.length() : mL;
        if (mL == 0)    return "";
        for (int i = 0; i < mL; i++){
            for (String s: strs){
                if (str0.charAt(i) == s.charAt(i))  strlen++;
            }
            if (strlen == strs.length){
                strlen = 0; count++; 
            } else  break;
        }   
        return strs[0].substring(0, count);
    }    

}
