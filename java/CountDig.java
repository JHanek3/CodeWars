// Task
// Square all the numbers from 0 to n
// Then search the numbers for integer d
// return the count of all occurances of integer d in the squared numbers


import java.util.ArrayList;

public class CountDig {
    
    public static int nbDig(int n, int d) {
        int count = 0;
        ArrayList<Integer> arrList = new ArrayList<Integer>();
        char ch = Character.forDigit(d, 10);
        
        for (int i = 0; i <= n; i++) {
            arrList.add(i * i);
        }

        for (int i = 0; i < arrList.size(); i++) {
            if (arrList.get(i).toString().contains(Integer.toString(d))) {
                for (int j = 0; j < arrList.get(i).toString().length(); j++) {
                    if (arrList.get(i).toString().charAt(j) == ch) {
                        count++;
                    }
                }
            }
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(nbDig(10, 1));
        System.out.println(nbDig(5750, 0));
    }
}