// Task
// Car can handle about 15 more bumps, if more than 15 return car dead else return woohoo

public class BumpsTheRoad {
    public static String bumps(final String road) {
        int count = 0;
        char n = 'n';
        for (int i = 0; i < road.length(); i++) {
            if (road.charAt(i) == n) {
                count++;
            }
        }
        if (count > 15) {
            return "Car Dead";
        } else {
            return "Woohoo!";
        }
    }

    public static void main(String[] args) {
        System.out.println(bumps("n"));
    }
  }