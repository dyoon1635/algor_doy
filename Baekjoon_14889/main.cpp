#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <deque>
#include <utility>
using namespace std;

int main() {
    int N, result=9999999;
    int **S;
    deque<string> dq;
    cin>>N;
    S=(int**)malloc(sizeof(int*)*N);
    for (int i=0; i<N; i++) S[i]=(int*)malloc(sizeof(int)*N);
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) cin>>S[i][j];
    }

    dq.push_back("0");
    dq.push_back("1");
    while(true) {
        string tmp=dq.front();
        int len=tmp.length();
        if (len==N) break;
        int zero_cnt=0, one_cnt=0;
        for (int i=0; i<len; i++) {
            if (tmp[i]=='0') zero_cnt++;
            else if (tmp[i]=='1') one_cnt++;
        }
        if (zero_cnt<N/2) dq.push_back(tmp+"0");
        if (one_cnt<N/2) dq.push_back(tmp+"1");
        dq.pop_front();
    }

    while(!dq.empty()) {
        int start=0, link=0;
        string tmp=dq.front();
        for (int i=0; i<N-1; i++) {
            if (tmp[i]=='1') {
                for (int j=i; j<N; j++) {
                    if (tmp[j]=='1') {
                        start+=(S[i][j]+S[j][i]);
                    }
                }
            } else {
                for (int j=i; j<N; j++) {
                    if (tmp[j]=='0') {
                        link+=(S[i][j]+S[j][i]);
                    }
                }
            }
        }
        dq.pop_front();
        result=min(abs(start-link),result);
    }
    cout<<result;
    return 0;
}
