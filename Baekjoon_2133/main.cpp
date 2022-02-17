#include <iostream>
using namespace std;

int main() {
    int N, dp[31]={0,};
    cin>>N;
    dp[0]=1;
    dp[2]=3;
    for (int i=2; i<=30; i+=2) {
        dp[i]=3*dp[i-2];
        for (int j=i-4; j>=0; j-=2) dp[i]+=(2*dp[j]);
    }
    cout<<dp[N];

    return 0;
}
