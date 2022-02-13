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
bool **visited; //사다리를 놓을 수 있는 위치(true인 경우 사다리 설치 불가 지역)
deque<pair<int,int> > ladder; //기존에 놓여 있는 사다리의 위치
deque<pair<int,int> > addedLadder; //새로 추가할 수 있는 사다리의 위치

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
        //사다리가 놓인 곳과 양옆을 사다리 설치 불가로 설정
        int x=ladder[i].first, y=ladder[i].second;
        visited[x][y]=true;
        visited[x][y-1]=true;
        if (y+1<N) visited[x][y+1]=true;
    }
    for (int i=1; i<=H; i++) {
        //추가로 사다리를 놓을 수 있는 곳을 체크
        for (int j=1; j<=N-1; j++) {
            if (!visited[i][j]) {
                addedLadder.push_back(make_pair(i,j));
            }
        }
    }
}

bool possible(deque<pair<int,int> > &dq) { //dq : 새로 놓을 사다리의 조합
    //해당 사다리를 놓았을 경우 정답이면 return true
    //새로 놓을 사다리의 조합이 바로 옆이라 불가하다면 return false
    for (int i=0; i<dq.size(); i++) {
        if (dq[i].first==dq[i+1].first &&
        dq[i].second==dq[i+1].second-1) { return false; }
    }

    deque<pair<int,int> > tmp(ladder);
    while(!dq.empty()) {
        //기존 사다리와 새로운 사다리를 설치
        tmp.push_back(dq.front());
        dq.pop_front();
    } sort(tmp.begin(),tmp.end());

    int *arr=(int*)malloc(sizeof(int)*(N+1));
    for (int i=1; i<=N; i++) arr[i]=i;
    for (int i=0; i<tmp.size(); i++) {
        //사다리를 타는 과정
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
    deque<pair<int,int> > dummy; //추가할 사다리가 0개인 경우를 위한 임시 변수
    if (possible(dummy)) {
        //새로 놓을 사다리의 갯수가 0인 경우
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

        vector<int> tmp; //새로 사다리를 놓는 경우의 조합을 따지기 위한 변수
        //11000인 경우 addedLadder의 3번째, 4번째, 5번째 사다리를 새로 놓는다는 것
        for (int i=0; i<r; i++) tmp.push_back(0);
        for (int i=0; i<n-r; i++) tmp.push_back(1);
        do {
            deque<pair<int,int> > input; //새로운 사다리의 조합
            for (int idx=0; idx<tmp.size(); idx++) {
                if (tmp[idx]!=1) {
                    int x=addedLadder[idx].first, y=addedLadder[idx].second;
                    input.push_back(make_pair(x,y));
                }
            }
            if (possible(input)) { //각각의 경우를 보고, 가능한 경우 결과값 출력 후 종료
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
