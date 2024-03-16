# Heap / Priority Queue

`큐`는 먼저 들어오는 데이터가 먼저 나가는 자료구조라면, `우선순위 큐`는 우선순위가 높은 데이터가 먼저 나가는 자료구조이다.  
우선순위 큐는 일반적으로 힙을 이용하여 구현한다.

힙은 완전 이진트리 형태의 자료구조이다. 여러 개의 데이터 중 최댓값 혹은 최솟값을 찾아내는 연산이 빠르다.

- 최대 힙: 부모 노드의 키 값이 자식 노드보다 크거나 같은 완전 이진트리이다.
- 최소 힙: 부모 노드의 키 값이 자식 노드보다 작거나 같은 이진 트리이다.

### 복습해 볼 문제

- [2542. Maximum Subsequence Score](https://leetcode.com/problems/maximum-subsequence-score)  
문제를 어떻게 접근해야 할지 생각도 못했다. (4/5)
- [2462. Total Cost to Hire K Workers](https://leetcode.com/problems/total-cost-to-hire-k-workers)  
문제는 이해했지만 코드를 너무 더럽게 작성하였다. (3.5/5)