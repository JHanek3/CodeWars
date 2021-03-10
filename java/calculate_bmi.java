

// Task
// Write a function that calculates body mass index (weight/height 2)
// <= 18.5 return underweight
// <= 25.0 return normal
// <= 30.0 return overweight
// > 30 return obese

class BMI {
  public static String bmi(double weight, double height) {
    double bmi = weight / (height * height);
    if (bmi <= 18.5) {
      return "Underweight";
    } 
    else if (bmi <= 25.0) {
      return "Normal";
    }
    else if (bmi <= 30.0) {
      return "Overweight";
    }
    else if (bmi > 30.0) {
      return "Obese";
    }
    else {
      return "";
    }
  }
}

// after seeing submissions
// public class Calculate {
//   public static String bmi(double weight, double height) {
    
//       double bmi = weight / (height * height);

//       if ( bmi <= 18.5) return "Underweight";
//       if ( bmi <= 25) return "Normal";
//       if ( bmi <= 30) return "Overweight";
//       return "Obese";

//   }
// }