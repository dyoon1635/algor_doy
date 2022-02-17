#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;

int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};
int N,M,**arr,**dp;

int dfs(int r, int c) {
    if (r>=N || r<0 || c>=M || c<0) return 0;
    if (dp[r][c]!=-1) return dp[r][c];
    if (r==0 && c==0) return 1;

    dp[r][c]=0;
    for (int i=0; i<4; i++) {
        int nx=r+dx[i], ny=c+dy[i];
        if (nx>=N || nx<0 || ny>=M || ny<0) continue;
        if (arr[nx][ny]>arr[r][c]) dp[r][c]+=dfs(nx,ny);
    }
    return dp[r][c];
}

int main() {
    cin>>N>>M;
    arr=(int**)malloc(sizeof(int*)*N);
    dp=(int**)malloc(sizeof(int*)*N);
    for (int i=0; i<N; i++) {
        arr[i]=(int*)malloc(sizeof(int)*M);
        dp[i]=(int*)malloc(sizeof(int)*M);
    }
    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            cin>>arr[i][j];
            dp[i][j]=-1;
        }
    }

    cout<<dfs(N-1,M-1);
    for (int i=0; i<N; i++) {
        free(arr[i]);
        free(dp[i]);
    }
    free(arr);
    free(dp);
    return 0;
}
