// Task
//A T are compliments, C G are compliments
// ATTGC returns TAACG

public class DnaStrand {
    public static String makeComplement(String dna) {
        String complimentaryStrand = "";
        for (int i = 0; i < dna.length(); i++) {
            switch(dna.charAt(i)) {
                case 'A':
                    complimentaryStrand += "T";
                    break;
                case 'T':
                    complimentaryStrand += "A";
                    break;
                case 'G':
                    complimentaryStrand += "C";
                    break;
                case 'C':
                    complimentaryStrand += "G";
                    break;
            }
        }
        return complimentaryStrand;
    }
    public static void main(String[] args) {
        System.out.println(makeComplement("ATTGC"));
    }
  }

//   public class DnaStrand {
//     public static String makeComplement(String dna) {
//       dna = dna.replaceAll("A","Z");
//       dna = dna.replaceAll("T","A");
//       dna = dna.replaceAll("Z","T");
//       dna = dna.replaceAll("C","Z");
//       dna = dna.replaceAll("G","C");
//       dna = dna.replaceAll("Z","G");
//       return dna;
//     }
//   }