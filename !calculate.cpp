#include <iostream>
using namespace std;

int main(){
    int a,c;
    cin >> a;
    c=1;
    for (int b=a;b>0;b--){
        c=c*b;
    }
    cout << c;
    return 0;
}