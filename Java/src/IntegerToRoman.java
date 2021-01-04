import java.util.HashMap;

public class IntegerToRoman {

    public static void main(String[] args){
        Solution solution = new Solution();
        System.out.println("result:"+solution.intToRoman(999));
    }
}
/**
 Symbol Value    Symbol Value    Symbol Value    Symbol Value    Symbol Value
 I      1        9      IX       2      II       20     XX       200    CC
 V      5        90     XC       3      III      30     XXX      300    CCC
 X      10       900    CM       4      IV       40     XL       400    CD
 L      50       2000   MM       6      VI       60     LX       600    DC
 C      100      3000   MMM      7      VII      70     LXX      700    DCC
 D      500                      8      VIII     80     LXXX     800    DCCC
 M      1000
 **/
class Solution {
    public String getStr(int num,int sign){
        String str="";
        switch (num){
            case 9:
                str = "IX";
                break;
            case 90:
                str = "XC";
                break;
            case 900:
                str = "CM";
                break;
            default:
                break;
        }

        if(!str.equals("")){
            return str;
        }

        switch (sign){
            case 10:
                if(num<4){
                    str = clone("I",num/1);
                }else if(num == 5){
                    str = "V";
                }else{
                    str = clone("I",num/1-5);
                }
                break;
            case 100:
                if(num<40){
                    str = clone("I",num/1);
                }else if(num == 50){
                    str = "L";
                }else{
                    str = clone("I",num/1-5);
                }
                break;
            case 1000:
                break;
        }
        return null;
    }
    public String clone(String s,int times){
        String str="";
        while (times>=1){
            str+=s;
            times--;
        }
        return str;
    }

    public String intToRoman(int num) {
        String str="";
        for(int times=1,sign=10;num>0;sign=10*sign,times++){
            int n = num%sign;
            num = num/sign*sign;
            System.out.println("n:"+n+",num:"+num);
            str=getStr(n,sign)+str;
        }
//        char a = str[1];
//        if(num>10){
//            int n=num/10;
//            str=intToRoman(n);
//        }
//        String result=str+String.valueOf(num%10);
//        System.out.println(">"+result);
        return str;
//        StringBuffer str = new StringBuffer();
//        int size=num;
//        HashMap<Integer,String> keyValue = new HashMap<>();
//        keyValue.put(1,"I");
//        keyValue.put(5,"V");
//        keyValue.put(10,"X");
//        keyValue.put(50,"L");
//        keyValue.put(100,"C");
//        keyValue.put(500,"D");
//        keyValue.put(1000,"M");
//        for(int sign=10,unit=0;num>=1;num/=10,unit=num%10,sign*=10){
//            System.out.println(num%10);
//            String s=null;
//
//
//            switch (sign){
//                case 10:
//
//                    str.append("");
//                    break;
//                case 100:
//                    break;
//                case 1000:
//                    break;
//                default:
//                    break;
//            }
//            if(unit==9){  //减法
//
//            }
//        }
//        return str.toString();
    }
}