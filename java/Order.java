// Task
//  The string of words contains a number in them to determine the order
// return the string with the words correctly ordered
// J2n H1 -> H1 J2n

import java.util.ArrayList;

public class Order {
    public static String order(String words) {
        ArrayList<String> sortedList = new ArrayList<String>();
        String[] split = words.split(" ");

        if (words.equals("")) {
            return "";
        }
        
        int start = 1;
        while (start <= split.length) {
            for (int i = 0; i < split.length; i++ ) {
                if (split[i].contains(Integer.toString(start))) {
                    sortedList.add(split[i]);
                    start++;
                }  
            }
        }
        return String.join(" ", sortedList);
    }

    public static void main(String[] args) {
        System.out.println(order("is2 Thi1s T4est 3a"));
        System.out.println(order("4of Fo1r pe6ople g3ood th5e the2"));
    }
  }