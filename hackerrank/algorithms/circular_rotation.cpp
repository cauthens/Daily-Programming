// https://www.hackerrank.com/challenges/circular-array-rotation
// 6 - 4 - 2017
#include <deque>
#include <numeric>
#include <iostream>
#include <algorithm>

using namespace std;


int main(){
    long n,k,q,m,plc;

    cin >> n >> k >> q;
    deque<long> a;
    for(int a_i = 0;a_i < n;a_i++){
       cin >> plc;
       a.push_back(plc);
    }
    for(int k_i = 0; k_i < k; k_i++){
        plc = a.back();
        a.pop_back();
        a.push_front(plc);
    }

    for(int a0 = 0; a0 < q; a0++){
        cin >> m;
        cout << a[m] << endl;
    }
    return 0;
}
