#include<iostream>
#include<queue>

using namespace std;

bool visit[100001];
queue<int> q;
int n, m, cnt = 0;

void bfs(int x)
{
    if (visit[x])
        return;
    visit[x] = true;
    int a = x * 2;
    int b = x + 1;
    int c = x - 1;
    if (a == m)
        n = a;

    if (b == m)
        n = b;

    if (c == m)
        n = c;

    q.push(a);
    q.push(b);
    q.push(c);
}

int main()
{
    cin >> n >> m;
    q.push(n);
    while (1)
    {
        if (n == m)
            break;
        int size = q.size();
        cnt += 1;
        for (int i = 0; i < size; i++)
        {
            int x = q.front();
            if (x > 100000 || x < 0)
            {
                q.pop();
                continue;
            }

            bfs(x);
            q.pop();
        }
    }
    
    cout << cnt;

    return 0;
}