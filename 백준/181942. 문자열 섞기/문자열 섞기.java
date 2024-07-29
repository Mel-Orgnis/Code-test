class Solution {
    public String solution(String str1, String str2) {
        String answer = "";
        
        for (int i = 0; i < str1.length(); i++) {
            answer = answer + str1.charAt(i);
            for (int j = i; j <= i; j++) {
                answer = answer + str2.charAt(j);
            }
        }
        return answer;
    }
}