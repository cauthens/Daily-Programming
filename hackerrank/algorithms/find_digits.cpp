// 5 - 31 - 3017
// https://www.hackerrank.com/challenges/find-digits

#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
using std::string; using std::cin; using std::cout;
using std::endl;

int main(){
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        // store n as an int and a count of the numbers
        int n;
        cin >> n;
        int count = 0;
        // make a copy of n as a string
        string str_n = std::to_string(n);
        for(auto ch: str_n){
            int converted = ch - '0';
            if(converted != 0 and n%converted == 0)
                count++;


        }// end for 2
        cout << count << endl;
    }// end for 1
   ;
    return 0;
}
