class Solution {
    public int solution(int a, int b) {
        int answer = 0;

        String str1 = "" + a + b;
        String str2 = "" + (2 * a * b);

        if (Integer.parseInt(str1) < Integer.parseInt(str2)) {
            answer = Integer.parseInt(str2);
        }
        if (Integer.parseInt(str1) >= Integer.parseInt(str2)) {
            answer = Integer.parseInt(str1);
        }
        return answer;
    }
}