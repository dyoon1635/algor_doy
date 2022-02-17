#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <cstring>
using namespace std;

string A,B;
int **arr;

void init() {
    cin>>A>>B;
    arr=(int**)malloc(sizeof(int*)*(A.size()+1));
    for (int i=0; i<=A.size(); i++)
        arr[i]=(int*)calloc(B.size()+1,sizeof(int));
}

void LCS() {
    int alen=A.size(), blen=B.size(),max_val=0;
    for (int i=1; i<=alen; i++) {
        for (int j=1; j<=blen; j++) {
            if (A[i-1]==B[j-1]) arr[i][j]=arr[i-1][j-1]+1;
            else arr[i][j]=max(arr[i-1][j],arr[i][j-1]);
            max_val=max(max_val,arr[i][j]);
        }
    }
    for (int i=0; i<=A.size(); i++) free(arr[i]);
    free(arr);
    cout<<max_val;
}

int main() {
    init();
    LCS();
    return 0;
}
