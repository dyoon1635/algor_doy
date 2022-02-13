#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <deque>
#include <utility>
#include <string>
#include <math.h>
using namespace std;
deque<int> rotate_(deque<int> dq, int dir);

void print(deque<deque<int> > dq) {
    for (int i=0; i<4; i++) {
        for (int j=0; j<8; j++) cout<<dq[i][j];
        cout<<endl;
    } cout<<endl;
}

int main() {
    int K,result=0;
    deque<deque<int> > dq;
    deque<pair<int,int> > rot;
    for (int i=0; i<4; i++) {
        string gear;
        deque<int> tmp;
        cin>>gear;
        for (int j=0; j<8; j++) {
            tmp.push_back(gear[j]-'0');
        } dq.push_back(tmp);
    }
    cin>>K;
    for (int i=0; i<K; i++) {
        int num,dir;
        cin>>num>>dir;
        rot.push_back(make_pair(num,dir));
    }

    while(!rot.empty()) {
        int num,dir,left,right;
        num=rot.front().first-1;
        dir=rot.front().second;
        left=dq[num][6];
        right=dq[num][2];
        dq[num]=rotate_(dq[num],dir);

        while(true) {
            if (num+1>=4 || right==dq[num+1][6]) break;
            right=dq[num+1][2];
            dq[num+1]=rotate_(dq[num+1],-dir);
            num++; dir*=(-1);
        } //print(dq);
        num=rot.front().first-1;
        dir=rot.front().second;
        while(true) {
            if (num-1<0 || left==dq[num-1][2]) break;
            left=dq[num-1][6];
            dq[num-1]=rotate_(dq[num-1],-dir);
            num--; dir*=(-1);
        } //print(dq);
        rot.pop_front();
    }
    result=dq[0][0];
    for (int i=1; i<4; i++) result+=(pow(2,i)*dq[i][0]);
    //print(dq);
    cout<<result;
    return 0;
}

deque<int> rotate_(deque<int> dq, int dir) {
    if (dir==1) {
        dq.push_front(dq.back());
        dq.pop_back();
    } else if (dir==-1) {
        dq.push_back(dq.front());
        dq.pop_front();
    } return dq;
}
