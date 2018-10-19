//find the parity outlier in a vector of integers

int FindOutlier(std::vector<int> arr)
{
  int number = 0;
  int same;
  for (int i = 0; i < arr.size(); i++){
    if (abs(arr.at(i)%2) == 0){
      if (number != 0){
        number = 0;
        break;
      }
      same = arr.at(i);
      number++;
    }    
  }
  if (number != 0)
    return same;
  for (int i = 0; i < arr.size(); i++){
    if (abs(arr.at(i)%2) == 1){
      return arr.at(i);
    }
  }
}