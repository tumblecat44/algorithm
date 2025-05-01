class Solution {
    public int[] solution(int[] arr) {
        int first = -1;
        int last = -1;
        
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 2) {
                first = i;
                break;
            }
        }

        for (int i = arr.length - 1; i >= 0; i--) {
            if (arr[i] == 2) {
                last = i;
                break;
            }
        }

        // 2가 없는 경우
        if (first == -1) {
            return new int[]{-1};
        }

 
        int[] answer = new int[last - first + 1];
        for (int i = first; i <= last; i++) {
            answer[i - first] = arr[i];
        }

        return answer;
    }
}
