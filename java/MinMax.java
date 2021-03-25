// Task
// Write a function that returns both the minimum and maximum number of the given list/array.

import java.util.Arrays;

class MinMax {
  public static int[] minMax(int[] arr) {
    Arrays.sort(arr);
    int[] listFin = {arr[0], arr[arr.length - 1]};
    // System.out.println(Arrays.toString(listFin));
    // return new int[]{arr[0],arr[arr.length-1]};
    return listFin;
  }
  public static void main(String[] args) {
    System.out.println(minMax(new int[]{1,2,3,4,5}));
  }
}