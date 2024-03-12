Graphs - DFS
===
### DFS를 그래프에서 이용하는 챕터이다.
### 난이도 : ★★★★★
### 이해도 : ★★★★☆
앞서 풀었던 DFS를 이진트리에서 이용한 챕터보다 난이도가 상당하였다.  
특히 단반향으로 제시된 그래프를 역방향으로 바꾸어 문제에 활용하는 발상을 하지 못하여 어려움이 있었다.  
그래프에서 DFS는 각 노드와의 연관성을 생각하여 푸는것이 중요해보인다.  
****
## ● 인상깊은 문제
### 1. 1466. Reorder Routes to Make All Paths Lead to the City Zero
모든 노드가 키값이 0인 노드를 향하게 만들려고 할때 그래프의 방향을 몇번 바꾸는지 찾는 문제이다.  
사실 처음 접근을 0에서 먼 노드부터 시작할려고 하였지만, 0을 기준으로 역방향으로 만든 그래프를 통해 개수를 찾는것이 맞았다.