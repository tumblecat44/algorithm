class Solution {
    public int[] solution(String my_string) {
        int[] um = new int[52]; 
        char[] charArray = my_string.toCharArray();
        int[] answer = {};
        for(char ch: charArray){
            if (ch >= 'A' && ch <= 'Z') {
                um[ch - 'A'] += 1;  
            } else if (ch >= 'a' && ch <= 'z') {
                um[ch - 'a' + 26] += 1; 
            }
        }
        return um;
    }
}