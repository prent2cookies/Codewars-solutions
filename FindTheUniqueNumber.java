//Finds the "unique" number compared to the others in an array

// Make sure your class is public
 public class Kata {
    public static double findUniq(double arr[]) {
      double one = arr[0];
      double two = 0;
      int onecount = 1;
      int twocount = 0;
      for (int i = 1; i < 3; i++){
        if (arr[i] != one){
          two = arr[i];
          twocount++;}
        else
          onecount++;
      }
      
      if (onecount < 3){
        if (onecount < 2)
          return one;
        return two;
      }
      for (int i = 3; i < arr.length; i++){
        if (arr[i] != one)
          return arr[i];
      }
    return 0;
   }
}