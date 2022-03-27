#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int n;
int scv[3] = {0, };
int dp[61][61][61];

void init() {
    cin>>n;
    for (int i=0; i<n; i++) {
        cin>>scv[i];
    }

    for (int i=0; i<=60; i++) {
        for (int j=0; j<=60; j++) {
            for (int k=0; k<=60; k++) dp[i][j][k] = -1;
        }
    }
}

int mutalisk(int x, int y, int z) {
    if (x < 0) return mutalisk(0, y, z);
    if (y < 0) return mutalisk(x, 0, z);
    if (z < 0) return mutalisk(x, y, 0);

    if (x == 0 && y == 0 && z == 0) return 0;

    int& res = dp[x][y][z];
    if (res != -1) return res;

    res = 9999999;
    res = min(res, mutalisk(x - 9, y - 3, z - 1) + 1);
    res = min(res, mutalisk(x - 9, y - 1, z - 3) + 1);
    res = min(res, mutalisk(x - 3, y - 9, z - 1) + 1);
    res = min(res, mutalisk(x - 3, y - 1, z - 9) + 1);
    res = min(res, mutalisk(x - 1, y - 9, z - 3) + 1);
    res = min(res, mutalisk(x - 1, y - 3, z - 9) + 1);
    return res;
}

int main() {
    init();
    cout<<mutalisk(scv[0], scv[1], scv[2])<<endl;
    return 0;
}
