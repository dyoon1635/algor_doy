#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;

int n,k;
int *w, *v, **res;

void init() {
    cin>>n>>k;
    w=(int*)calloc(n+1, sizeof(int));
    v=(int*)calloc(n+1, sizeof(int));
    res=(int**)malloc(sizeof(int*)*(n+1));
    for (int i=0; i<=n; i++)
        res[i]=(int*)calloc(k+1,sizeof(int));

    for (int i=1; i<=n; i++)
        cin>>w[i]>>v[i];
}

void dp() {
    for (int i=1; i<=n; i++) {
        for (int j=1; j<=k; j++) {
            if (j-w[i]>=0) res[i][j]=max(res[i-1][j], res[i-1][j-w[i]]+v[i]);
            else res[i][j]=res[i-1][j];
        }
    }
}

void destructor() {
    free(w);
    free(v);
    for (int i=0; i<=n; i++) free(res[i]);
    free(res);
}

int main() {
    init();
    dp();
    cout<<res[n][k];
    destructor();
    return 0;
}
