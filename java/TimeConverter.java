// Task
// Convert seconds to hours and minutes

public class TimeConverter{
    public static String toTime(int seconds){
        int remainder = 0;
        int hours = 0;
        int minutes = 0;
        if (seconds >= 3600) {
            hours = seconds / 3600;
            remainder = seconds - hours * 3600;
            minutes = remainder / 60;

        } else {
            minutes = seconds / 60;
        }

        return String.format("%d hour(s) and %d minute(s)", hours, minutes);
    }

    public static void main(String[] args) {
        System.out.println(toTime(3600));
        System.out.println(toTime(3601));
        System.out.println(toTime(3500));
        System.out.println(toTime(323500));
        System.out.println(toTime(0));
    }
}