#include <iostream>
#include <algorithm>
#include <vector>


using namespace std;


int main(){
    int n,k;
    cin >> n >> k;
    vector<int> height(n);
    for(int height_i = 0; height_i < n; height_i++){
       cin >> height[height_i];
    }
    auto max = max_element(height.begin(),height.end());
    if(*max > k)
        cout << (*max-k) << endl;
    else
        cout << 0 << endl;
    // your code goes here
    return 0;
}
