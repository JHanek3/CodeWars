// Task
// Find the first empty room
// "0" means empty
import java.util.Arrays;
  

public class TheOffice {
    public static Object meeting(char[] x) {
        char o = 'O';
        int iterator = 0;
        int index = 0;
        boolean match = false;
        for (char ch: x) {
            if (ch == o) {
                index = iterator;
                match = true;
                break;
            }
            iterator++;
        }
        if (match) {
            return index;
        } else {
            return "None available!";
        }
    }

    


    public static void main(String[] args) {
        System.out.println(meeting(new char[] {'X', 'O', 'X'}));
    }
  }

  // I knew there was a shorter way
//   public class TheOffice {

//     public static Object meeting(char[] x) {
//       int i = new String(x).indexOf('O');
//       return i < 0 ? "None available!" : i;
//     }
  
//   }