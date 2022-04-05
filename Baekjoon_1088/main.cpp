#include <iostream>
#include <utility>
#include <queue>
#include <math.h>
using namespace std;

int n, m;
long double min_cake = pow(10, 9);
priority_queue<pair<long double, int> > pq;

void init() {
    cin>>n;
    for (int i=0; i<n; i++) {
        long double cake;
        cin>>cake;
        min_cake = min(min_cake, cake);
        pq.push(make_pair(cake, 0));
    } cin>>m;
}

void cutting() {
    long double min_val = pq.top().first - min_cake;
    for (int i=0; i<m; i++) {
        long double cake = pq.top().first;
        int cut_cnt = pq.top().second;
        pq.pop();
        cake *= (cut_cnt + 1);
        cut_cnt ++;
        cake /= (cut_cnt + 1);

        pq.push(make_pair(cake, cut_cnt));
        min_cake = min(min_cake, cake);
        min_val = min(min_val, pq.top().first - min_cake);
    }
    cout<<fixed;
    cout.precision(10);
    cout<<min_val<<endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    init();
    cutting();
    return 0;
}
