#include <iostream>
using std::cin; using std::cout;
using std::endl;


int main(){
    float neg=0,pos=0,ze=0,n,hold;
    cin >> n;
    while(cin >> hold){
        if(hold < 0){
            ++neg;
        }else if(hold>0){
            ++pos;
        }else{
            ++ze;
        }
    }

    cout << pos/n << endl << neg/n << endl << ze/n;

}
