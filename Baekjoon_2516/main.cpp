#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <deque>
#include <utility>
using namespace std;

int n, num = 0;
deque<deque<int> > dq;
bool *monkey;

void init() {
    cin>>n;
    monkey = (bool*)calloc(n+1, sizeof(bool));
    for (int i=0; i<=n; i++) {
        deque<int> tmp;
        dq.push_back(tmp);
    }

    for (int i=1; i<=n; i++) {
        int tmp;
        cin>>tmp;
        for (int j=0; j<tmp; j++) {
            int rival;
            cin>>rival;
            dq[i].push_back(rival);
        }
    }
}

bool separate() {
    bool is_separated = false;
    for (int i=1; i<=n; i++) {
        if (!monkey[i]) {
            int cnt = 0;
            for (int j=0; j<dq[i].size(); j++) {
                if (!monkey[dq[i][j]]) cnt ++;
            }

            if (cnt > 1) {
                is_separated = true;
                monkey[i] = true;
                num ++;
            }
        }
    }

    for (int i=1; i<=n; i++) {
        if (monkey[i]) {
            int cnt = 0;
            for (int j=0; j<dq[i].size(); j++) {
                if (monkey[dq[i][j]]) cnt ++;
            }

            if (cnt > 1) {
                is_separated = true;
                monkey[i] = false;
                num --;
            }
        }
    }

    return is_separated;
}

void print() {
    cout<<n - num<<" ";
    for (int i=1; i<=n; i++) {
        if (!monkey[i]) cout<<i<<" ";
    } cout<<endl;
    cout<<num<<" ";
    for (int i=1; i<=n; i++) {
        if (monkey[i]) cout<<i<<" ";
    }
}

int main() {
    init();

    while(separate()) {}
    print();

    free(monkey);
    return 0;
}
