// Task
// Remove all vowels from a string

public class Troll {
    public static String disemvowel(String str) {
        str = str.replaceAll("[AaEeIiOoUu]", "");
        return str;
    }

    public static void main(String[] args) {
        System.out.println(disemvowel("This website is for losers LOL!"));
    }
}