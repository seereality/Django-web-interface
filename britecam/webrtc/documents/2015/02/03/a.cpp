#include<bits/stdc++.h>
using namespace std;
int partition(int sum,int lar)
{
    cout << sum << " " << lar << endl;
    if(lar==0)
        return 0;
    if(sum==0)
        return 1;
    if(sum<0)
        return 0;
    return partition(sum,lar-1) + partition(sum-lar,lar);
}
int main()
{
    int sum =4;
    int lar=3;
    cout << partition(sum,lar) << endl;
}
