// Task
// Return true if you are employed and not on vacation, otherwise false

public class set_alarm {
  public static boolean setAlarm(boolean employed, boolean vacation) {
    if (employed == true && vacation == false) {
      return true;
    } else {
      return false;
    }
  }
  public static void main(String[] args) {
    System.out.println(setAlarm(true, true));
    System.out.println(setAlarm(false, false));
    System.out.println(setAlarm(false, false));
    System.out.println(setAlarm(true, false));
  }
}

// Come back to this later
