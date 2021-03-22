// Task
// Convert a string to an array

public class StringToArray {
  public static String[] stringToArray(String s) {
    String[] words = s.split(" ");
    // System.out.println(Arrays.toString(words));
    return words;
    //your code;
  }
  public static void main(String[] args) {
    System.out.println(stringToArray("Robin Singh"));
  }

}
