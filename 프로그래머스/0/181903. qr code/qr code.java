class Solution {
    public String solution(int q, int r, String code) {
        String answer = "";
        char[] um = code.toCharArray();
        for(int i = 0; i <um.length; i++){
            if(i%q == r){
                answer += um[i];
            }
        }
        
        return answer;
    }
}