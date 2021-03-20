public class CountPositivesSumNegatives {
  public static int[] countPositivesSumNegatives(int[] input)
    { 
      if (input == null) {
        return new int[] {};
      }
      if (input.length == 0) {
        return new int[] {};
      } else {
        int numPos = 0;
        int sum = 0;
        for (int i = 0; i < input.length; i++) {
          if (input[i] > 0) {
            numPos += 1;
          } else {
            sum += input[i];
          }
        }
        return new int[] {numPos, sum};
      }
    }
  public static void main(String[] args) {
    System.out.println(countPositivesSumNegatives(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15}));
  }
}