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


// lcp of first two string is lcp of their lcp and the ith string's lcp
public class Solution {


    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0){
            return "";
        }
        if (strs.length == 1){
            return strs[0];
        }
        String lcp = strs[0];
        for (int i = 1; i < strs.length; i++){
            lcp = LCPhelp(strs[i], lcp);
            if (lcp == ""){
                return "";
            }
        }
        return lcp;
    }
    
    public String LCPhelp(String str1, String lcp){
        if (str1.length() == 0 || lcp.length() == 0){
            return "";
        }
        int mL = (str1.length() < lcp.length()) ? str1.length() : lcp.length();
        int count = 0;
        for (int i = 0; i < mL; i++){
            if (str1.charAt(i) == lcp.charAt(i)){
                count++;
            } else{
                break;
            }
        }
        return lcp.substring(0,count);
    }
}
