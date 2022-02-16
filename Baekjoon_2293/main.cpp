#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;

int main() {
    int N,K,*coin,*dp;

    cin>>N>>K;
    coin=(int*)malloc(sizeof(int)*(N+1));
    dp=(int*)calloc(K+1,sizeof(int));
    for (int i=1; i<=N; i++)
        cin>>coin[i];
    dp[0]=1;

    for (int i=1; i<=N; i++) {
        for (int j=0; j<=K; j++) {
            if (coin[i]<=j)
                dp[j]+=dp[j-coin[i]];
        }
        //for (int k=0; k<=K; k++) cout<<dp[k]<<" ";
        //cout<<endl;
    }

    cout<<dp[K];
    free(coin);
    free(dp);
    return 0;
}
