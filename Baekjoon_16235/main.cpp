#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <deque>
#define MAX 10
using namespace std;

int N,M,K;
int **A, **field; //A: 매해 추가할 양분의 양, field: 현재 땅에 양분의 양
/* 1<=N<=10 이므로 tree를 MAX만큼 할당
tree 이중 배열은 각 땅에 자라는 나무의 나이의 집합 */
deque<int> tree[MAX][MAX];

void init() {
    // N: 땅의 크기, M: 초기 나무의 갯수, K: the number of year cycle
    cin>>N>>M>>K;
    A=(int**)malloc(sizeof(int*)*N);
    field=(int**)malloc(sizeof(int*)*N);
    for (int i=0; i<N; i++) {
        A[i]=(int*)malloc(sizeof(int)*N);
        field[i]=(int*)malloc(sizeof(int)*N);
    }

    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin>>A[i][j];
            field[i][j]=5;
        }
    }

    for (int i=0; i<M; i++) {
        int x,y,z;
        cin>>x>>y>>z;
        tree[x-1][y-1].push_back(z); //문제에 idx는 1-base이므로 0-base로 맞춰줌
    }
}

void spring() {
    /* 나이만큼 양분을 먹고 나이가 1 올라감
    양분이 충분하지 않다면 양분을 흡수하지 못하고 즉시 사망
    죽은 나무의 나이는 음수로 표기 */
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            for (int k=0; k<tree[i][j].size(); k++) {
                if (field[i][j]-tree[i][j][k]>=0) {
                    field[i][j]-=tree[i][j][k];
                    tree[i][j][k]++;
                }
                else tree[i][j][k]*=(-1);
            }
        }
    }
}

void summer() {
    /* 죽은 나무는 나이의 절반을 양분으로 치환
    새로 생성되는 나무는 항상 pop_front() 이므로
    자연스레 어느 정도의 오름차순이 보장됨.
    뒤에서부터 tree를 검사하면서 죽은 나무는 deque에서 빼줌 */
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            for (int k=tree[i][j].size()-1; k>=0; k--) {
                if (tree[i][j][k]<0) {
                    field[i][j]+=((-tree[i][j][k])/2);
                    tree[i][j].pop_back();
                }
            }
        }
    }
}

void autumn() {
    /* 나무의 나이가 5의 배수라면 해당 나무를 기준으로 번식
    번식은 해당 나무의 위치 기준 팔방으로 age=1인 나무를 심는 것 */
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            /* 1~N , 1~N : 땅의 크기만큼 순회 */
            for (int k=0; k<tree[i][j].size(); k++) { //해당 땅에 자란 나무들을 모두 체크
                if (tree[i][j][k]%5==0) {
                    //나무의 나이가 5의 배수인 경우 팔방이 유효범위인지 각각 체크
                    for (int r=-1; r<=1; r++) {
                        for (int c=-1; c<=1; c++) {
                            if ((i+r>=0 && i+r<N) &&
                                (j+c>=0 && j+c<N) &&
                                (c!=0 || r!=0)) {
                                tree[i+r][j+c].push_front(1);
                            }
                        }
                    }
                }
            }
        }
    }
}

void winter() {
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) field[i][j]+=A[i][j];
    }
}

void destructor() {
    for (int i=0; i<N; i++) {
        free(A[i]);
        free(field[i]);
    }
    free(A);
    free(field);
}

int result() {
    int res=0;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            res+=tree[i][j].size();
        }
    }
    return res;
}

int main() {
    init();
    for (int i=0; i<K; i++) {
        spring();
        summer();
        autumn();
        winter();
    }
    cout<<result();
    destructor();
    return 0;
}
