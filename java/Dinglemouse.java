
// Task
// Find the age of cats and dogs equivalance of a human year
public class Dinglemouse {

    public static int[] humanYearsCatYearsDogYears(final int humanYears) {
      // Your code here!
      int catYears = 15;
      int dogYears = 15;
      for (int i = 1; i < humanYears; i++) {
          if (i == 1) {
              catYears += 9;
              dogYears += 9;
          } else {
              catYears += 4;
              dogYears += 5;
          }
      }
      return new int[]{humanYears, catYears,dogYears};
    }
    public static void main(String[] args) {
        humanYearsCatYearsDogYears(1);
        humanYearsCatYearsDogYears(2);
        humanYearsCatYearsDogYears(10);

    }
  
  }