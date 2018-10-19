//Checks to see if number is a "triangle number"
//example: 6 is a triangle number because the numbers 1-6
//can be arranged into an equilateral triangle like so:
//       1
//		2 3
//	   4 5 6

public class TriangleNumbers {

	public static Boolean isTriangleNumber(long number) {
    int current = 0;
    for(int i = 0; number>current; i++){
      current = i*(i+1)/2;
      if(current == number)
        return true;
    }
    return false;
  } 
  
}