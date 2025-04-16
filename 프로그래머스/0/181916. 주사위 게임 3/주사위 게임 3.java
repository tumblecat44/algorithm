import java.util.*;

class Solution {
    public int solution(int a, int b, int c, int d) {
        int[] arr = {a, b, c, d};
        Map<Integer, Integer> count = new HashMap<>();

        // 각 숫자의 등장 횟수 세기
        for (int num : arr) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        // 경우의 수 분기
        if (count.size() == 1) {
            // 1. 네 개 모두 같은 경우
            return 1111 * a;
        } else if (count.size() == 2) {
            // 2. (3,1) or (2,2)
            for (int key : count.keySet()) {
                int freq = count.get(key);
                if (freq == 3) {
                    // 2-1. (3,1) 형태
                    int p = key;
                    int q = getOtherKey(count, key);
                    return (int) Math.pow(10 * p + q, 2);
                }
            }
            // 2-2. (2,2) 형태
            List<Integer> keys = new ArrayList<>(count.keySet());
            int p = keys.get(0);
            int q = keys.get(1);
            return (p + q) * Math.abs(p - q);
        } else if (count.size() == 3) {
            // 3. (2,1,1) 형태
            int pair = 0;
            List<Integer> others = new ArrayList<>();
            for (int key : count.keySet()) {
                if (count.get(key) == 2) {
                    pair = key;
                } else {
                    others.add(key);
                }
            }
            return others.get(0) * others.get(1);
        } else {
            // 4. 모두 다름
            return Arrays.stream(arr).min().getAsInt();
        }
    }

    private int getOtherKey(Map<Integer, Integer> map, int excludeKey) {
        for (int key : map.keySet()) {
            if (key != excludeKey) {
                return key;
            }
        }
        return -1; 
    }
}
