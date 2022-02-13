#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <deque>
using namespace std;

int N,M;
char **board;
int dx[4]={-1,0,1,0}; //clockwise, up_start
int dy[4]={0,1,0,-1};
bool red_goal=false, blue_goal=false, not_changed=false;
typedef struct INFO {
    int rx,ry,bx,by;
    int cnt,ex_dir;
} INFO;
deque<INFO> dq;

void init() {
    INFO init_info;
    init_info.cnt=0;
    init_info.ex_dir=-1;
    cin>>N>>M;
    board=new char*[N];
    for (int i=0; i<N; i++)
        board[i]=new char[M];
    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            cin>>board[i][j];
            if (board[i][j]=='B') {
                init_info.bx=i;
                init_info.by=j;
            }
            if (board[i][j]=='R') {
                init_info.rx=i;
                init_info.ry=j;
            }
        }
    }
    dq.push_back(init_info);
}

void moving(int dir, INFO& info) {
    red_goal=false, blue_goal=false, not_changed=false;
    int rx=info.rx, ry=info.ry;
    int bx=info.bx, by=info.by;
    while(true) {
        bool red_moved=false, blue_moved=false;
        if (board[rx+dx[dir]][ry+dy[dir]]!='#') {
            rx+=dx[dir];
            ry+=dy[dir];
            red_moved=true;
        }
        if (board[bx+dx[dir]][by+dy[dir]]!='#') {
            bx+=dx[dir];
            by+=dy[dir];
            blue_moved=true;
        }

        if (board[rx][ry]=='O') red_goal=true;
        if (board[bx][by]=='O') blue_goal=true;
        if (!red_moved && !blue_moved) break;
    }
    if (rx==bx && ry==by) {
        switch(dir) {
        case 0:
            if (info.rx>info.bx) rx++;
            else if (info.rx<info.bx) bx++;
            break;
        case 1:
            if (info.ry>info.by) by--;
            else if (info.ry<info.by) ry--;
            break;
        case 2:
            if (info.rx>info.bx) bx--;
            else if (info.rx<info.bx) rx--;
            break;
        case 3:
            if (info.ry>info.by) ry++;
            else if (info.ry<info.by) by++;
            break;
        }
    }

    if (rx==info.rx && bx==info.bx && ry==info.ry && by==info.by)
        not_changed=true;
    info.bx=bx, info.by=by;
    info.rx=rx, info.ry=ry;
    info.cnt++, info.ex_dir=dir;
}

void solve() {
    while (!dq.empty()) {
        if (dq.front().cnt>10) break;
        int nrx=dq.front().rx, nry=dq.front().ry;
        int nbx=dq.front().bx, nby=dq.front().by;

        for (int i=0; i<4; i++) {
            INFO tmp=dq.front();
            if (tmp.ex_dir==(i+2)%4) continue;
            moving(i,tmp);

            if (red_goal && !blue_goal) {
                if (tmp.cnt<=10) cout<<tmp.cnt;
                else cout<<-1;
                return;
            }
            if (!blue_goal && !not_changed) dq.push_back(tmp);
        }
        dq.pop_front();
    } cout<<-1;
}

int main() {
    init();
    solve();
    for (int i=0; i<N; i++) delete [] board[i];
    delete [] board;
    return 0;
}
