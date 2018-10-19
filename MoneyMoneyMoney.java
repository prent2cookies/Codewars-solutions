//Calculate the number of years required to get desired money
//given the interest, current money, and taxes

public class Money {
  public static int calculateYears(double principal, double interest,  double tax, double desired) {
    // your code
    int years = 0;
    double current = principal;
    if (desired == principal)
      years = 0;
    else{
      while(current/desired<1){
        current = current + ((current*interest)-((current*interest)*tax));
        years++;}
    }
    return years;   
  }
}