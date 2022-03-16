#include <queue>
#include <stdio.h>
#include <iostream>
using namespace std;

int main() {
    int n;
    long long res = 0;
    priority_queue<long long> pq;

    scanf("%d", &n);
    for (int i=0; i<n; i++) {
        int tmp;
        scanf("%d", &tmp);
        pq.push(-tmp);
    }

    while (pq.size() != 1) {
        long long tmp = pq.top();
        pq.pop();
        tmp += pq.top();
        pq.pop();
        pq.push(tmp);
        res -= tmp;
    }
    cout<<res;
    return 0;
}
