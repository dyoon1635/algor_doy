#include <iostream>
#include <deque>
#include <utility>
using namespace std;

int m, n;
int dx[4] = {-1,0,1,0}, dy[4] = {0,1,0,-1};
int field[1000][1000];
deque<pair<int, int> > tomato;

void init() {
    cin>>m>>n;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            cin>>field[i][j];
            if (field[i][j] == 1)
                tomato.push_back(make_pair(i, j));
        }
    }
}

bool out_of_bound(int x, int y) {
    if (x < 0 || x >= n || y < 0 || y >= m) return true;
    return false;
}

void print_field() {
    for (int i = 0; i<n; i++) {
        for (int j = 0; j<m; j++)
            cout<<field[i][j]<<" ";
        cout<<endl;
    }cout<<endl;
}

void print_tomato() {
    for (int i = 0; i<tomato.size(); i++) {
        cout<<tomato[i].first<<" "<<tomato[i].second<<endl;
    }
}

bool ripen() {
    bool is_ripen = false;
    int sz = tomato.size();
    for (int i=0; i<sz; i++) {
        int x = tomato.front().first, y = tomato.front().second;
        tomato.pop_front();

        for (int dir=0; dir<4; dir++) {
            int nx = x+dx[dir], ny = y+dy[dir];

            if (out_of_bound(nx, ny)) continue;
            if (field[nx][ny] == 0) {
                field[nx][ny] = 1;
                tomato.push_back(make_pair(nx, ny));
                is_ripen = true;
            }
        }
    }
    return is_ripen;
}

int main() {
    init();
    int cnt = 0;
    while(ripen()) { cnt ++; }

    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            if (field[i][j] == 0) {
                cout<<-1<<endl;
                return 0;
            }
        }
    }
    cout<<cnt<<endl;
    return 0;
}
