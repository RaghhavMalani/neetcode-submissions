class Solution {
    private boolean isDivisor(int len, String str1, String str2) {
        int l1 = str1.length();
        int l2 = str2.length();

        if (l1 % len != 0 || l2 % len != 0) {
            return false;
        }

        String base = str1.substring(0, len);

        return base.repeat(l1 / len).equals(str1)
            && base.repeat(l2 / len).equals(str2);
    }

    public String gcdOfStrings(String str1, String str2) {
        int limit = Math.min(str1.length(), str2.length());

        for (int i = limit; i >= 1; i--) {
            if (isDivisor(i, str1, str2)) {
                return str1.substring(0, i);
            }
        }

        return "";
    }
}