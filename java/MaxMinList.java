import java.util.Arrays;

public class MaxMinList {
  public static int min(int[] list) {
    Arrays.sort(list);
    return list[0];
  }
  
  public static int max(int[] list) {
    Arrays.sort(list);
    return list[list.length - 1];
  }

  public static void main(String[] args) {
    System.out.println(min(new int[]{-52, 56, 30, 29, -54, 0, -110}));
    System.out.println(min(new int[]{42, 54, 65, 87, 0}));
    System.out.println(max(new int[]{4,6,2,1,9,63,-134,566}));
    System.out.println(max(new int[]{5}));
  }
}
