public class IntegerToRoman {

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println("result:" + solution.intToRoman(3));
    }
}

/**
 * Value   Symbol 
 * 
 * 1       I       
 * 2       II
 * 3       III
 * 4       IV
 * 5       V
 * 6       VI
 * 7       VII
 * 8       VIII
 * 9       IX
 * 10      X
 * 50      L    
 * 100     C
 * 500     D
 * 1000    M
 **/
class Solution {
    public String getStr(int remainder, int sign) {
        if (remainder <= 3) { // 1-3
            return clone(getUnit(sign), remainder, "");
        } else if (remainder == 9) {
            return getUnit(sign) + getLv(sign);
        } else {
            return clone(getUnit(sign), remainder - 5, getFive(sign));

        }
    }

    /**
     * @param s ��λֵ
     * @param times ѭ������,Ϊ����ʱ��ʾ"��(��)",Ϊ����ʱ��ʾ"��(��)"
     * @param base ��ָ 5 50 500 10 100 1000
     * @return
     */
    public String clone(String s, int times, String base) {
        String str = base;
        if (times > 0) {
            while (times > 0) {
                str += s;
                times--;
            }
        } else {
            while (times < 0) {
                str = s + str;
                times++;
            }
        }
        return str;
    }

    /**
     * ��ָ��������ת�����ַ�
     * @return
     */
    public String getLv(int num) {
        switch (num) {
            case 10:
                return "X";
            case 100:
                return "C";
            case 1000:
                return "M";
            default:
                return "";
        }
    }

    /**
     * �������� 5 50 500
     * @return
     */
    public String getFive(int num) {
        switch (num) {
            case 10:
                return "V";
            case 100:
                return "L";
            case 1000:
                return "D";
            default:
                return "";
        }
    }

    /**
     * ��ȡָ���������ĵ�λֵ
     * @return
     */
    public String getUnit(int num) {
        switch (num) {
            case 10:
                return "I";
            case 100:
                return "X";
            case 1000:
                return "C";
            case 10000:
                return "M";
            default:
                return "";
        }
    }

    /**
     * @param num ��������
     * @return ��1994(M CM XC IV)Ϊ��   
     * ep   num    n      sign 
     * 0    1994   0      10 
     * 1    1990   4      100 
     * 2    1900   90     1000 
     * 3    1000   900    10000 
     * 4    0      1000   100000 
     * (end)
     */
    public String intToRoman(int num) {
        String str = "";
        for (int sign = 10; num > 0; sign = 10 * sign) {
            int remainder = num % sign; // ����
            if (remainder == 0) {
                continue;
            }
            num = num / sign * sign;
            str = getStr(remainder / (sign / 10), sign) + str;
            System.out.println(str);
        }
        return str;
    }
}