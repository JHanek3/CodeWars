public class ZywOo {

  public static String howManyDalmatians(int numer) {
  
    String[] dogs = {"Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIANS!!!"};
    
    if (numer <= 10) {
      return dogs[0];
    } else if (numer <= 50) {
      return dogs[1];
    } else if (numer == 101) {
      return dogs[3];
    } else {
      return dogs[2];
    }
  }

  public static void main(String[] args) {
    System.out.println(howManyDalmatians(1));
  }
  
}

// Challenge given Buggy code, fix it
// public class ZywOo {

//   public static String howManyDalmations(numer) :
  
//     String[] dogs {"Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"};
    
//     String respond = number <= 10 ? dogs[0] (number <= 50 ? dogs[1] : (number = 101  dogs[3] : dogs[2]
    
//     return respond
  
// }

// Another way to solve
// class ZywOo {
//   static String howManyDalmatians(int number) {
//     return number <= 10 ? "Hardly any" :
//            number <= 50 ? "More than a handful!" :
//            number == 101 ? "101 DALMATIANS!!!" : "Woah that's a lot of dogs!";
//   }
// }