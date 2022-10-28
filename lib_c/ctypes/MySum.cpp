/*
 * Compute the sum an array
 * @param n number of elements
 * @param array input array
 * @return sum 
*/


extern "C" // required when using C++ compiler


long long mysum(int aN, int* aArray) {
   long long Res = 0;
   for (int i = 0; i < aN; ++i) {
      Res += aArray[i];
   }
   return Res;
}


