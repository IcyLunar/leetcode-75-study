Graphs - BFS
===
### BFS를 그래프에서 활용하는 챕터이다.
### 난이도 : ★★★☆☆
### 이해도 : ★★★★★
이전 챕터와 마찬가지로, 이진트리가 아닌 그래프에서 BFS를 사용하는것이다.  
DFS와 다르게 그래프 관련한 문제에서 BFS는 많이 풀어보았기 때문에 해당 챕터는 쉬웠다.  
****
## ● 인상깊은 문제
### 1. 994. Rotting Oranges
썩은 오렌지가 인접한 썩지않은 오렌지를 썩게하며 모든 오렌지가 썩기까지 걸리는 시간을 출력하는 문제이다.  
일반적으로는 Queue에 삽입에 따라 횟수를 증가시키지만 이 문제의 경우에는 인접노드를 모두 방문하였을때 횟수를 증가시키므로  
횟수를 나타내는 변수를 다른 방식으로 사용하여야한다.
