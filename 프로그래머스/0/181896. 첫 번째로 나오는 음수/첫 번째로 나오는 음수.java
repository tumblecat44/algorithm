class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int count = 0;
        for (int i : num_list){
            if (i<0){
                return count;
            }
            count++;
        }
        return -1;
    }
}