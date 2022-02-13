// https://www.acmicpc.net/problem/15684
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <deque>
#include <vector>
#include <utility>
#include <algorithm>
#define endl '\n'
using namespace std;

int N,H,M;
bool **visited; //��ٸ��� ���� �� �ִ� ��ġ(true�� ��� ��ٸ� ��ġ �Ұ� ����)
deque<pair<int,int> > ladder; //������ ���� �ִ� ��ٸ��� ��ġ
deque<pair<int,int> > addedLadder; //���� �߰��� �� �ִ� ��ٸ��� ��ġ

void init() {
    cin>>N>>M>>H;
    for (int i=0; i<M; i++) {
        int a,b;
        cin>>a>>b;
        ladder.push_back(make_pair(a,b));
    } sort(ladder.begin(),ladder.end());
    visited=(bool**)malloc(sizeof(bool*)*(H+1));
    for (int i=0; i<=H; i++)
        visited[i]=(bool*)calloc(N, sizeof(bool));

    for (int i=0; i<ladder.size(); i++) {
        //��ٸ��� ���� ���� �翷�� ��ٸ� ��ġ �Ұ��� ����
        int x=ladder[i].first, y=ladder[i].second;
        visited[x][y]=true;
        visited[x][y-1]=true;
        if (y+1<N) visited[x][y+1]=true;
    }
    for (int i=1; i<=H; i++) {
        //�߰��� ��ٸ��� ���� �� �ִ� ���� üũ
        for (int j=1; j<=N-1; j++) {
            if (!visited[i][j]) {
                addedLadder.push_back(make_pair(i,j));
            }
        }
    }
}

bool possible(deque<pair<int,int> > &dq) { //dq : ���� ���� ��ٸ��� ����
    //�ش� ��ٸ��� ������ ��� �����̸� return true
    //���� ���� ��ٸ��� ������ �ٷ� ���̶� �Ұ��ϴٸ� return false
    for (int i=0; i<dq.size(); i++) {
        if (dq[i].first==dq[i+1].first &&
        dq[i].second==dq[i+1].second-1) { return false; }
    }

    deque<pair<int,int> > tmp(ladder);
    while(!dq.empty()) {
        //���� ��ٸ��� ���ο� ��ٸ��� ��ġ
        tmp.push_back(dq.front());
        dq.pop_front();
    } sort(tmp.begin(),tmp.end());

    int *arr=(int*)malloc(sizeof(int)*(N+1));
    for (int i=1; i<=N; i++) arr[i]=i;
    for (int i=0; i<tmp.size(); i++) {
        //��ٸ��� Ÿ�� ����
        int idx=tmp[i].second;
        swap(arr[idx],arr[idx+1]);
    }
    for (int i=1; i<=N; i++) {
        if (arr[i]!=i) {
            free(arr);
            return false;
        }
    }
    free(arr);
    return true;
}

void solve() {
    deque<pair<int,int> > dummy; //�߰��� ��ٸ��� 0���� ��츦 ���� �ӽ� ����
    if (possible(dummy)) {
        //���� ���� ��ٸ��� ������ 0�� ���
        cout<<0;
        return;
    }
    int res=1, n=addedLadder.size(); //
    while(true) {
        int r=res;
        if (r>3) {
            cout<<-1;
            break;
        }

        vector<int> tmp; //���� ��ٸ��� ���� ����� ������ ������ ���� ����
        //11000�� ��� addedLadder�� 3��°, 4��°, 5��° ��ٸ��� ���� ���´ٴ� ��
        for (int i=0; i<r; i++) tmp.push_back(0);
        for (int i=0; i<n-r; i++) tmp.push_back(1);
        do {
            deque<pair<int,int> > input; //���ο� ��ٸ��� ����
            for (int idx=0; idx<tmp.size(); idx++) {
                if (tmp[idx]!=1) {
                    int x=addedLadder[idx].first, y=addedLadder[idx].second;
                    input.push_back(make_pair(x,y));
                }
            }
            if (possible(input)) { //������ ��츦 ����, ������ ��� ����� ��� �� ����
                cout<<res;
                return ;
            }
        } while(next_permutation(tmp.begin(), tmp.end()));
        res++;
    }
}

int main() {
    init();
    solve();
    for (int i=0; i<=H; i++) free(visited[i]);
    free(visited);
    return 0;
}
