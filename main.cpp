#include<iostream>
using namespace std;

int Hn(int var1)
{
    if(var1 == 1){
        return 1;
    }
    return (1/Hn(var1-1) + (1/var1));
}

int Hn()
{
    int var1;
    cout << "Please enter a integer";
    cin >> var1;
    return Hn(var1);
}
