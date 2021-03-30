public class ShortString {
    public static int findShort(String s) {
        int shortStr = 0;
        String[] result = s.split(" ");
        for (int i = 0; i < result.length; i++) {
            if (i == 0) {
                shortStr = result[i].length();
            } else {
                if (shortStr > result[i].length()) {
                    shortStr = result[i].length();
                }
            }
        }

        return shortStr;
    }

    public static void main(String[] args) {
        System.out.println(findShort("bitcoin take over the world maybe who knows perhaps"));
        System.out.println(findShort("turns out random test cases are easier than writing out basic ones"));
    }
}

// public static int findShort(String s) {
//     return Stream.of(s.split(" "))
//       .mapToInt(String::length)
//       .min()
//       .getAsInt();
// }