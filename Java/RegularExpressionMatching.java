import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Set;
import java.util.Map.Entry;

public class RegularExpressionMatching {
    /**
     * .   匹配任意单个字符
     * *   匹配零个或多个前面的字符
     * 解析流程
     *   s 字符串
     *   p 匹配串
     */
    class Solution {
        public boolean isMatch(String s, String p) {
            int si = 0, pi = 0;
            char[] sa = s.toCharArray();
            char[] pa = p.toCharArray();
            List<String> slk = new ArrayList<String>();
            List<String> slv = new ArrayList<String>();
            List<String> slk = new ArrayList<String>();
            List<String> slv = new ArrayList<String>();
            char sc = sa[si], pc = pa[pi];
            int sc_count = 0, pc_count = 0;
            int slen = s.length(), plen = p.length();
            while (true) {
                while (sc == sa[si]) {
                    sc_count++;
                    si++; // 统计 sc 的个数
                }

                while (true) {
                    if(pc == pa[si]){
                        break; 
                    }
                    sc_count++;
                    si++; // 统计 sc 的个数

                    
                }

                sc_count = 0;
                pc_count = 0;
                return false;
            }
            // return false;
        }
    }

    public static void main(String[] args) {
        // String s = "aa", p = "a"; // F
        // String s = "aa", p ="a*"; // T
        // String s = "ab", p =".*"; // T
        // String s = "aab", p ="c*a*b"; // T
        // String s = "mississippi", p ="mis*is*p*."; // F
        // String s = "ab", p = ".*c"; // F
        // String s = "aaa", p ="a*a"; // T
        // String s = "aaa", p ="ab*a*c*a"; // T
        String s = "a", p ="ab*a"; // F

        // RegularExpressionMatching regularExpressionMatching = new RegularExpressionMatching();
        // RegularExpressionMatching.Solution solution = regularExpressionMatching.new Solution();
        // if (solution.isMatch(s, p)) {
        //     System.out.println("true");
        // } else {
        //     System.out.println("false");
        // }

        LinkedHashMap<String, Integer> m = new LinkedHashMap<String, Integer>();
        m.put("aaa", 1);
        m.put("aaa", 1);
        m.put("bbb", 2);
        m.put("ccc", 3);
        m.put("aaa", 1);
        Set<Entry<String, Integer>> set = m.entrySet();
        Iterator<Entry<String, Integer>> i = set.iterator();
        while(i.hasNext()){

        }
    }
}
