#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <deque>
#include <algorithm>
#include <vector>
using namespace std;

int N,M,res=0;
int dx[4]={-1,0,1,0};
int dy[4]={0,1,0,-1};
int **board;
typedef struct block {
    int x,y;
    int ex_dir;
    int sum,sz;
} block;


void init() {
    cin>>N>>M;
    board=new int*[N];
    for (int i=0; i<N; i++)
        board[i]=new int[M];
    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) cin>>board[i][j];
    }
}

void except(deque<block> &dq) {
    vector<int> v;
    for (int dir=0; dir<4; dir++) {
        if (dq.front().ex_dir==(dir+2)%4) continue;
        v.push_back(dir);
    }
    do {
        block tmp=dq.front();
        if (tmp.x+dx[v[0]]>=0 && tmp.x+dx[v[0]]<N &&
            tmp.y+dy[v[0]]>=0 && tmp.y+dy[v[0]]<M &&
            tmp.x+dx[v[1]]>=0 && tmp.x+dx[v[1]]<N &&
            tmp.y+dy[v[1]]>=0 && tmp.y+dy[v[1]]<M) {
            tmp.sum+=(board[tmp.x+dx[v[0]]][tmp.y+dy[v[0]]]);
            tmp.sum+=(board[tmp.x+dx[v[1]]][tmp.y+dy[v[1]]]);
            tmp.sz+=2;
            dq.push_back(tmp);
        }
    } while(next_permutation(v.begin(),v.end()));
}

void solve() {
    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            deque<block> dq;
            block init_block={i,j,-1,board[i][j],1};
            dq.push_back(init_block);
            while(!dq.empty()) {
                if (dq.front().sz==4) {
                    res=max(res,dq.front().sum);
                    dq.pop_front();
                    continue;
                }

                if (dq.front().sz==2) {
                    except(dq);
                }

                for (int dir=0; dir<4; dir++) {
                    block tmp=dq.front();
                    if (tmp.ex_dir==(dir+2)%4) continue;
                    if (tmp.x+dx[dir]>=0 && tmp.x+dx[dir]<N &&
                        tmp.y+dy[dir]>=0 && tmp.y+dy[dir]<M) {
                        tmp.x+=dx[dir];
                        tmp.y+=dy[dir];
                        tmp.sum+=board[tmp.x][tmp.y];
                        tmp.sz++;
                        tmp.ex_dir=dir;
                        dq.push_back(tmp);
                    }
                } dq.pop_front();
            }
        }
    }
}

int main() {
    init();
    solve();
    cout<<res;
    for (int i=0; i<N; i++) delete [] board[i];
    delete [] board;
    return 0;
}
