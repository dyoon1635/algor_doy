#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <queue>
#include <utility>
using namespace std;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

int n, m;
int board[1000][1000];
int visited[1000][1000][2] = {0,};
typedef struct coord {
    int x, y;
    bool broken;
} coord;
queue<coord> q;

void init() {
    scanf("%d %d", &n, &m);
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++)
            scanf("%1d", &board[i][j]);
    }
    visited[0][0][0] = 1;
    coord tmp = {0, 0, false};
    q.push(tmp);
}

bool valid(int x, int y) {
    if (x < 0 || x >= n || y < 0 || y >= m) return false;
    return true;
}

void bfs() {
    while(!q.empty()) {
        int x = q.front().x, y = q.front().y;
        bool broken = q.front().broken;
        q.pop();
        for (int i=0; i<4; i++) {
            int nx = x + dx[i], ny = y + dy[i];
            if (valid(nx, ny)) {
                if (nx == n - 1 && ny == m - 1) {
                    cout<<visited[x][y][broken] + 1<<endl;
                    return ;
                }

                if (board[nx][ny] == 0  && visited[nx][ny][broken] == 0) {
                    visited[nx][ny][broken] = visited[x][y][broken] + 1;
                    coord tmp = {nx, ny, broken};
                    q.push(tmp);
                }
                else if (board[nx][ny] == 1 && !broken) {
                    visited[nx][ny][1] = visited[x][y][0] + 1;
                    coord tmp = {nx, ny, true};
                    q.push(tmp);
                }
            }
        }
    } cout<<-1<<endl;
}

int main() {
    init();
    if (n == 1 && m == 1) {
        cout<<1<<endl;
        return 0;
    }
    bfs();
    return 0;
}
