#include <iostream>
#include <deque>
#include <utility>
using namespace std;

int m, n, h;
int dx[4] = {-1,0,1,0}, dy[4] = {0,1,0,-1};
int field[100][100][100];
typedef struct tom {
    int z, x, y;
} tom;
deque<tom> tomato;

void init() {
    cin>>m>>n>>h;
    for (int k=0; k<h; k++) {
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                cin>>field[k][i][j];
                if (field[k][i][j] == 1) {
                    tom tmp = {k, i, j};
                    tomato.push_back(tmp);
                }
            }
        }
    }
}

bool out_of_bound(int z, int x, int y) {
    if (z < 0 || z >= h ||
        x < 0 || x >= n ||
        y < 0 || y >= m)
        return true;
    return false;
}

bool ripen() {
    bool is_ripen = false;
    int sz = tomato.size();
    for (int i=0; i<sz; i++) {
        int z = tomato[0].z, x = tomato[0].x, y = tomato[0].y;
        tomato.pop_front();

        for (int dir=0; dir<4; dir++) {
            int nx = x+dx[dir], ny = y+dy[dir];

            if (out_of_bound(z, nx, ny)) continue;
            if (field[z][nx][ny] == 0) {
                field[z][nx][ny] = 1;
                tom tmp = {z, nx, ny};
                tomato.push_back(tmp);
                is_ripen = true;
            }
        }

        if (!out_of_bound(z + 1, x, y) && field[z + 1][x][y] == 0) {
            field[z+1][x][y] = 1;
            tom tmp = {z+1, x, y};
            tomato.push_back(tmp);
            is_ripen = true;
        }
        if (!out_of_bound(z - 1, x, y) && field[z - 1][x][y] == 0) {
            field[z-1][x][y] = 1;
            tom tmp = {z-1, x, y};
            tomato.push_back(tmp);
            is_ripen = true;
        }

    }
    return is_ripen;
}

int main() {
    init();
    int cnt = 0;
    while(ripen()) { cnt ++; }

    for (int k=0; k<h; k++) {
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                if (field[k][i][j] == 0) {
                    cout<<-1<<endl;
                    return 0;
                }
            }
        }
    }
    cout<<cnt<<endl;
    return 0;
}
