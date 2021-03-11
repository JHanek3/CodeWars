public class messi_goals_function {
  public static int goals(int laLigaGoals, int copaDelReyGoals, int championsLeagueGoals) {
    return laLigaGoals + copaDelReyGoals + championsLeagueGoals;
  }

  public static void main(String[] args) {
    System.out.println(goals(0, 0, 0));
    System.out.println(goals(43, 10, 5));
  }
} 