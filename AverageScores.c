//Average scores

#include <stddef.h>
#include <math.h>

int average(const int *values, size_t count){
  int average = 0;
  int counts = count;
  for (int i = 0; i < count; i++){
    average = average + values[i];
  }
  if (average % count > (count/2))
    return average/count + 1;
  return average/count;
}