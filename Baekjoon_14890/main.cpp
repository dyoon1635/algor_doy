#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;

int main() {
    int N,L,result=0;
    int **M;
    cin>>N>>L;
    M=(int**)malloc(sizeof(int*)*N);
    for (int i=0; i<N; i++) M[i]=(int*)malloc(sizeof(int)*N);
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) cin>>M[i][j];
    }

    for (int i=0; i<N; i++) {
        bool possible_route=true,descending=false;
        int asc=1, desc=1;
        for (int j=0; j<N-1; j++) {
            if (abs(M[i][j+1]-M[i][j])>1 || !possible_route) {
                possible_route=false;
                continue;
            }
            else if (M[i][j+1]==M[i][j]) {
                if (descending) {
                    desc++;
                    if (desc==L) {
                        descending=false;
                        desc=1;
                        asc=0;
                    }
                }
                else asc++;
            }
            else if (M[i][j+1]==M[i][j]+1) {
                if (asc<L || descending) {
                    possible_route=false;
                    continue;
                }
                asc=1;
            }
            else if (M[i][j+1]==M[i][j]-1) {
                if (L==1) { asc=0; continue; }
                if (descending) {
                    possible_route=false;
                    continue;
                }
                descending=true;
            }
        }
        if (possible_route && !descending) result++;
    }

        for (int j=0; j<N; j++) {
        bool possible_route=true,descending=false;
        int asc=1, desc=1;
        for (int i=0; i<N-1; i++) {
            if (abs(M[i+1][j]-M[i][j])>1 || !possible_route) {
                possible_route=false;
                continue;
            }
            else if (M[i+1][j]==M[i][j]) {
                if (descending) {
                    desc++;
                    if (desc==L) {
                        descending=false;
                        desc=1;
                        asc=0;
                    }
                }
                else asc++;
            }
            else if (M[i+1][j]==M[i][j]+1) {
                if (asc<L || descending) {
                    possible_route=false;
                    continue;
                }
                asc=1;
            }
            else if (M[i+1][j]==M[i][j]-1) {
                if (L==1) { asc=0; continue; }
                if (descending) {
                    possible_route=false;
                    continue;
                }
                descending=true;
            }
        }
        if (possible_route && !descending) result++;
    }
    cout<<result;
    return 0;
}
