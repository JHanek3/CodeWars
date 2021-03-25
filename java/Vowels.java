// Task
// Return the number of vowels in a given string
import java.lang.*;

public class Vowels {

    public static int getCount(String str) {
        int vowelsCount = 0;
        char cA = 'a';
        char cE = 'e';
        char cI = 'i';
        char cO = 'o';
        char cU = 'u';


        for (int i = 0; i < str.length(); i++) {
        char c = str.charAt(i);
            if (c == cA || c == cE || c == cI || c == cO || c == cU) {
                vowelsCount++;
            }
        }      
      return vowelsCount;
    }

    public static void main(String[] args) {
        System.out.println(getCount("abracadabra"));
    }
}

// public class Vowels {

//     public static int getCount(String str) {
//       int vowelsCount = 0;
//       for(int i = 0; i < str.length(); i++) {
//           switch(str.charAt(i)) {
//           case 'a':
//           case 'e':
//           case 'i':
//           case 'o':
//           case 'u':
//               vowelsCount++;
//           }
//       }
//       return vowelsCount;
//     }
  
//   }