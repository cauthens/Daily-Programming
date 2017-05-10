#include <map>
#include<iostream>
using std::map;
using std::cout; using std::cin; using std::endl;


int main(){
    long n, plc, max=0;
    cin >> n;
    map<long, long> height;
    for(int height_i = 0;height_i < n;height_i++){
       cin >> plc;
       height[plc]++;
       max = ((plc>max) ? plc : max);

    }
    cout << height[max] << endl;

    return 0;
}
