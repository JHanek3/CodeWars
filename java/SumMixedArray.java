// Task
// Return the sum of array of integers and strings

import java.util.List;
import java.util.Arrays;

public class SumMixedArray {
  public static int sum(List<?> mixed) {
    int x = 0;
    for(Object s: mixed){
      x+=Integer.parseInt(s.toString());
    }
    return x;
	}
  public static void main(String[] args) {
    System.out.println(sum(Arrays.asList(9, 3, "7", "3")));
  }
}
