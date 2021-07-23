public class RegularExpressionMatching {
    /**
     * .   匹配任意单个字符
     * *   匹配零个或多个前面的字符
     */
    class Solution {
        public boolean isMatch(String s, String p) {
            int si = 0, pi = 0;
            char[] sc = s.toCharArray();
            char[] pc = p.toCharArray();
            int slen = s.length(), plen = p.length();
            while (true) {
                if (slen == si) {
                    if (plen == pi) {
                        return true;
                    }
                    while (pi < plen) {// p 还未结束
                        if (pc[pi] == '.' || pc[pi] == '*' || (pc[pi - 1] == '*' && pc[pi] == sc[si - 1])) {
                            pi++;
                        } else {
                            return false;
                        }
                    }
                    return true;
                }
                if (pi >= plen && si < slen) {
                    break;
                }
                if (sc[si] == pc[pi]) {
                    si++;
                    pi++;
                    continue;
                } else {
                    if (pc[pi] == '.') {
                        si++;
                        pi++;
                        continue;
                    } else if (pc[pi] == '*' && (pc[pi - 1] == sc[si] || pc[pi - 1] == '.')) {
                        si++;
                        continue;
                    } else {
                        pi++;
                        if (pi >= plen) {
                            break;
                        }
                        if(pc[pi] == '*') {
                            pi++;
                            continue;
                        }
                        continue;
                    }
                }
            }
            return false;
        }
    }

    public static void main(String[] args) {
        String s = "aa", p = "a"; // F
        // String s = "aa", p ="a*"; // T
        // String s = "ab", p =".*"; // T
        // String s = "aab", p ="c*a*b"; // T
        // String s = "mississippi", p ="mis*is*p*."; // F
        // String s = "ab", p = ".*c"; // F
        // String s = "aaa", p ="a*a"; // T
        RegularExpressionMatching regularExpressionMatching = new RegularExpressionMatching();
        RegularExpressionMatching.Solution solution = regularExpressionMatching.new Solution();
        if (solution.isMatch(s, p)) {
            System.out.println("true");
        } else {
            System.out.println("false");
        }
    }
}
