//Find the nth digit of integer num

#include <iostream>
#include <cmath>
int findDigit(int num, int nth){
  if (nth < 1) return -1; //no negative digits
  int base = 10;
  int top = nth-1;
  int value = num / pow(base,top); //get rid of lower digits
  return abs(value%10); //get rid of higher digits and negative values
}