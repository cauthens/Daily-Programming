#include <cmath>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <limits>
using namespace std;

// 6 - 1 - 2017
// https://www.hackerrank.com/challenges/equality-in-a-array

int main() {

    long n,plc, mode;
    vector<long> v;
    cin >> n;
    long count = 1;
    long max = 0;

    for(auto i = 0; i < n; i++){
        cin >> plc;
        v.push_back(plc);
    }// end for

    sort(v.begin(),v.end());

    for(auto i = 0; i < n; i++){
        if(v[i] == v[i+1]){
            count++;
        }else{
            if(count > max){
                max = count;
            }// end if
            count = 1;
        } // end else
    }// end for

    cout << n-max << endl;
}
