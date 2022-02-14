#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <deque>
#define MAX 10
using namespace std;

int N,M,K;
int **A, **field; //A: ���� �߰��� ����� ��, field: ���� ���� ����� ��
/* 1<=N<=10 �̹Ƿ� tree�� MAX��ŭ �Ҵ�
tree ���� �迭�� �� ���� �ڶ�� ������ ������ ���� */
deque<int> tree[MAX][MAX];

void init() {
    // N: ���� ũ��, M: �ʱ� ������ ����, K: the number of year cycle
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
        tree[x-1][y-1].push_back(z); //������ idx�� 1-base�̹Ƿ� 0-base�� ������
    }
}

void spring() {
    /* ���̸�ŭ ����� �԰� ���̰� 1 �ö�
    ����� ������� �ʴٸ� ����� ������� ���ϰ� ��� ���
    ���� ������ ���̴� ������ ǥ�� */
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
    /* ���� ������ ������ ������ ������� ġȯ
    ���� �����Ǵ� ������ �׻� pop_front() �̹Ƿ�
    �ڿ����� ��� ������ ���������� �����.
    �ڿ������� tree�� �˻��ϸ鼭 ���� ������ deque���� ���� */
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
    /* ������ ���̰� 5�� ������ �ش� ������ �������� ����
    ������ �ش� ������ ��ġ ���� �ȹ����� age=1�� ������ �ɴ� �� */
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            /* 1~N , 1~N : ���� ũ�⸸ŭ ��ȸ */
            for (int k=0; k<tree[i][j].size(); k++) { //�ش� ���� �ڶ� �������� ��� üũ
                if (tree[i][j][k]%5==0) {
                    //������ ���̰� 5�� ����� ��� �ȹ��� ��ȿ�������� ���� üũ
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
