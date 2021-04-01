// Task
// Find min and max of string array of numbers
public class HighAndLow {
    public static String highAndLow(String numbers) {
        String[] splitted = numbers.split(" ");
        int min = Integer.valueOf(splitted[0]);
        int max = Integer.valueOf(splitted[0]);

        for (int i = 1;  i < splitted.length; i++) {
            if (Integer.valueOf(splitted[i]) < min) {
                min = Integer.valueOf(splitted[i]);
            }
            if (Integer.valueOf(splitted[i]) > max) {
                max = Integer.valueOf(splitted[i]);
            }
        }
        return String.format("%d %d", max, min);
      }
    
    public static void main(String[] args) {
        System.out.println(highAndLow("1 2 3 4 5"));
        System.out.println(highAndLow("8 3 -5 42 -1 0 0 -9 4 7 4 -4"));
    }

}