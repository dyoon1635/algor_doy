#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <deque>
#include <utility>
#include <math.h>
#include <algorithm>
using namespace std;

int N,M;
deque<pair<int,int> > house;
deque<pair<int,int> > chicken;

void init() {
    cin>>N>>M;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            int x;
            cin>>x;
            if (x==1) house.push_back(make_pair(i,j));
            if (x==2) chicken.push_back(make_pair(i,j));
        }
    }
}

int distance(deque<pair<int,int> > &chick) {
    int res=0;
    for (int i=0; i<house.size(); i++) {
        int house_dist=2e9;
        for (int j=0; j<chick.size(); j++) {
            int x=abs(house[i].first-chick[j].first);
            int y=abs(house[i].second-chick[j].second);
            house_dist=min(house_dist,x+y);
        }
        res+=house_dist;
    }
    return res;
}

void solve() {
    int res=2e9;
    deque<int> dq;
    for (int i=0; i<chicken.size()-M; i++) dq.push_back(0);
    for (int i=0; i<M; i++) dq.push_back(1);
    do {
        deque<pair<int,int> > chick;
        for (int i=0; i<dq.size(); i++) {
            if (dq[i]==1) {
                chick.push_back(make_pair(chicken[i].first,chicken[i].second));
            }
        }
        res=min(res,distance(chick));
    } while(next_permutation(dq.begin(),dq.end()));
    cout<<res;
}

int main() {
    init();
    solve();
    return 0;
}
