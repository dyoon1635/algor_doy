#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <deque>
using namespace std;

int N;
bool board[101][101]={{false,},};
int dx[4]={1,0,-1,0};
int dy[4]={0,-1,0,1};
typedef struct dragon_curve {
    int x,y,dir;
    int gen;
} dragon_curve;
deque<dragon_curve> dq;

void init() {
    cin>>N;
    for (int i=0; i<N; i++) {
        int x,y,d,g;
        cin>>x>>y>>d>>g;
        dragon_curve tmp={x,y,d,g};
        dq.push_back(tmp);
    }
}

deque<int> N_generation(int n, int dir) {
    deque<int> v;
    v.push_back(dir);
    for (int i=0; i<n; i++) {
        int sz=v.size()-1;
        for (int j=sz; j>=0; j--)
            v.push_back((v[j]+1)%4);
    }
    return v;
}

void travel(dragon_curve dc) {
    int x=dc.x, y=dc.y;
    board[y][x]=true;
    deque<int> v=N_generation(dc.gen,dc.dir);

    for (int i=0; i<v.size(); i++) {
        x+=dx[v[i]];
        y+=dy[v[i]];
        if (x>=0 && x<=100 && y>=0 && y<=100) board[y][x]=true;
    }
}

void solve() {
    int res=0;
    for (int i=0; i<dq.size(); i++) travel(dq[i]);
    for (int i=0; i<=99; i++) {
        for (int j=0; j<=99; j++) {
            if (board[i][j] && board[i+1][j] &&
                board[i][j+1] && board[i+1][j+1]) res++;
        }
    }
    cout<<res;
}

int main() {
    init();
    solve();
    return 0;
}
