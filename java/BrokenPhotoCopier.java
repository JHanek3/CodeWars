// Task
// Switch 0s to 1s and 1s to 0s

public class BrokenPhotoCopier {
    public static String broken(final String x) {
        char one = '1';
        String finStr = "";

        for (int i = 0; i < x.length(); i++) {
            if (x.charAt(i) == one) {
                finStr += "0";
            } else {
                finStr += "1";
            }
        }
        return finStr;
    }

    public static void main(String[] args) {
        System.out.println(broken("0"));
        System.out.println(broken("011101"));
    }
}