// https://www.hackerrank.com/challenges/cats-and-a-mouse
// 5 - 27 - 2017

#include <numeric>
#include <iostream>
using std::cin; using std::cout; using std::endl;
using std::abs;


int main(){
    int q;
    cin >> q;
    for(int a0 = 0; a0 < q; a0++){
        int x, y, z;
        cin >> x >> y >> z;
        if(abs(x-z) > abs(y-z))
            cout << "Cat B" << endl;
        else if (abs(x-z) < abs(y-z))
            cout << "Cat A" << endl;
        else if (abs(x-z) == abs(y-z))
            cout << "Mouse C" << endl;


    }
    return 0;
}
