class Solution {
    public String solution(String my_string, int[] indices) {
        String answer = "";
        char[] a = my_string.toCharArray();
        for(int i : indices){
            a[i] = '!';
        }
        for(char str : a){
            if(str != '!'){
                answer += str;
            }
        }
        return answer;
    }
}