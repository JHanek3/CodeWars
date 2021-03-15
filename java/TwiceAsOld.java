// Task
// Calculate how many years ago the father was twice as old as is his son

public class TwiceAsOld {
  public static int TwiceAsOld(int dadYears, int sonYears){
    if (sonYears == 0) {
      return dadYears;
    } else {
      if (dadYears - sonYears * 2 > 0) {
        return dadYears - sonYears * 2;
      }
      else {
        return (dadYears - sonYears * 2) * -1;
      }
    }
  }
  public static void main(String args[]) {
    System.out.println(TwiceAsOld(30, 0));
    System.out.println(TwiceAsOld(30, 7));
    System.out.println(TwiceAsOld(45, 30));
  }
}

// You can do absolute value
// public static int TwiceAsOld(int dadYears, int sonYears){
//   return Math.abs((sonYears*2)-dadYears);

// }
