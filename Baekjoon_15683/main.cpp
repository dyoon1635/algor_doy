#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <deque>
#include <math.h>
#include <utility>
using namespace std;

int N,M;
int **office;
int dx[4]={-1,0,1,0}; //clockwise, up_start
int dy[4]={0,1,0,-1};
typedef struct cam {
    int x,y;
    int type;
} cam;
deque<cam> cams;
deque<deque<int> > cases;

void init() {
    cin>>N>>M;
    office=new int*[N];
    for (int i=0; i<N; i++) office[i]=new int[M];

    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            cin>>office[i][j];
            if (office[i][j]!=0 && office[i][j]!=6) {
                cam tmp={i,j,office[i][j]};
                cams.push_back(tmp);
            }
        }
    }
    deque<int> dummy;
    cases.push_back(dummy);
}

void cam_on(int dir, int i) {
    int x=cams[i].x, y=cams[i].y;
    for (int i=0b0001; i<=0b1000; i<<=1) {
        if (dir&i) {
            int idx=log2(i);
            int nx=x, ny=y;
            while(true) {
                if (nx<0 || nx>=N ||
                    ny<0 || ny>=M || office[nx][ny]==6) break;
                if (office[nx][ny]==0) office[nx][ny]=-1;
                nx+=dx[idx];
                ny+=dy[idx];
            }
        }
    }
}

void roll_back() {
    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            if (office[i][j]==-1) office[i][j]=0;
        }
    }
}

int calculate() {
    int res=0;
    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            if (office[i][j]==0) res++;
        }
    } return res;
}

void possible_cases() {
    for (int i=0; i<cams.size(); i++) {
        while (cases.front().size()<=i) {
            switch(cams[i].type) {
            case 1: // 1 2 4 8
                for (int j=0; j<4; j++) {
                    deque<int> tmp(cases.front());
                    tmp.push_back(pow(2,j));
                    cases.push_back(tmp);
                } break;
            case 2: // 5 10
                for (int j=1; j<=2; j++) {
                    deque<int> tmp(cases.front());
                    tmp.push_back(j*5);
                    cases.push_back(tmp);
                } break;
            case 3: // 3 6 9 12
                for (int j=1; j<=4; j++) {
                    deque<int> tmp(cases.front());
                    tmp.push_back(j*3);
                    cases.push_back(tmp);
                } break;
            case 4: // 7 11 13 14
                for (int j=3; j>=0; j--) {
                    deque<int> tmp(cases.front());
                    tmp.push_back(15-pow(2,j));
                    cases.push_back(tmp);
                } break;
            case 5: // 15
                deque<int> tmp(cases.front());
                tmp.push_back(15);
                cases.push_back(tmp);
                break;
            }
            cases.pop_front();
        }
    }
}

void solve() {
    possible_cases();
    int sz=cams.size();
    int min_val=2e9;
    for (int i=0; i<cases.size(); i++) {
        for (int j=0; j<sz; j++) {
            cam_on(cases[i][j],j);
        }
        min_val=min(min_val, calculate());
        if (min_val==0) { cout<<0; return; }
        roll_back();
    }
    cout<<min_val;
}

int main() {
    init();
    solve();
    for (int i=0; i<N; i++) delete [] office[i];
    delete [] office;
    return 0;
}
