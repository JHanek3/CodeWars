// Task
// Find the stray number

public class StrayNumber {
    static int stray(int[] numbers) {
        // Find duplicate
        int dup = 0;
        int standOut = 0;
        for (int i = 0; i < numbers.length; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                if (numbers[i] == numbers[j]) {
                    dup = numbers[i];
                    break;
                }
            }
        }

        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] != dup) {
                standOut = numbers[i];
            }
        }
        return standOut;
    }
    public static void main(String[] args) {
        int[] myArray = {1, 1, 2};
        System.out.println(stray(myArray));
    }
    
}