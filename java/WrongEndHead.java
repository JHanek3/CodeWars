// Task
// Reverse an array
import java.util.*;

public class WrongEndHead {
  
  public static String[] fixTheMeerkat(String[] arr) {
    Collections.reverse(Arrays.asList(arr));
    return arr;
  }
  public static void main(String[] args) {
    System.out.println(fixTheMeerkat(new String[]{ "head", "body", "tail" }));
  }
}
