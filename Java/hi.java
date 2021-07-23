public class hi {
    public static void main(String[] args) {
        String s = "";
        if(s == null) {
            System.out.println("\"\"=null\n");
        }
        System.out.println(s);
        System.out.println(System.getProperty("user.home"));
        System.out.println(System.getProperty("java.version"));
        System.out.println(System.getProperty("os.name"));
        System.out.println(System.getProperty("java.vendor.url"));
    }
}