// 6 - 3 - 2017
// https://www.hackerrank.com/challenges/array-left-rotation
#include <cmath>
#include <cstdio>
#include <deque>
#include <iostream>
#include <sstream>
#include <algorithm>
using namespace std;


int main() {
   /* Enter your code here. Read input from STDIN. Print output to STDOUT */
   long n, d, plc;
   deque<long> deq;
   cin >> n;
   cin >> d;
   for(auto i = 0; i < n; i++){
       cin >> plc;
       deq.push_back(plc);
   }
   for(auto i = 0; i < d; i++){
       plc = deq.front();
       deq.pop_front();
       deq.push_back(plc);
   }
   for(auto i = 0; i < n; i++){
       cout << deq.front() << " ";
       deq.pop_front();
   }
   return 0;
}
