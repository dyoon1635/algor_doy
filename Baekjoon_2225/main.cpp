#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;

int main() {
    int N,K;
    long long dp[201]={0,};
    cin>>N>>K;

    dp[0]=1;
    for (int i=1; i<=K; i++) {
        for (int j=1; j<=N; j++) {
            dp[j]+=dp[j-1];
            dp[j]%=1000000000;
        }
        //for (int r=0; r<=N; r++) cout<<dp[r]<<" ";
        //cout<<endl;
    }

    cout<<dp[N];
    return 0;
}
