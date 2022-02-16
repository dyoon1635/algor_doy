#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;

int main() {
    int N, *num, *dp_asc, *dp_des;
    cin>>N;
    num=(int*)calloc(N,sizeof(int));
    for (int i=0; i<N; i++) cin>>num[i];

    dp_asc=(int*)calloc(N,sizeof(int));
    dp_des=(int*)calloc(N,sizeof(int));

    for (int i=0; i<N; i++) {
        dp_asc[i]=1;
        dp_des[i]=1;
    }

    for (int i=1; i<N; i++) {
        for (int j=0; j<i; j++) {
            if (num[j]<num[i]) {
                dp_asc[i]=max(dp_asc[i],dp_asc[j]+1);
            }
        }
    }

    for (int i=N-2; i>=0; i--) {
        for (int j=N-1; j>i; j--) {
            if (num[i]>num[j]) {
                dp_des[i]=max(dp_des[i],dp_des[j]+1);
            }
        }
    }

    int res=0;
    for (int i=0; i<N; i++) {
        res=max(res, dp_asc[i]+dp_des[i]-1);
    }
    cout<<res;

    return 0;
}
