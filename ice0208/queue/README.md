# Queue

### Queue 란?

큐는 먼저 삽입된 자료가 먼저 삭제되는 선입 선출 (First In First Out) 구조의 자료구조이다.

### Queue의 예시

- 프린터의 출력 처리
- BFS 문제
- 대기열

### 파이썬에서 큐의 사용

스택과 달리 큐는 자료를 삭제할 때 앞에서부터 삭제해야해서 리스트를 사용하면 시간이 오래걸린다. 그래서 보통 `collections` 모듈의 `deque`를 이용한다.

자주 사용되는 메소드는 아래와 같다.

- append/appendleft
- extend/extendleft
- pop/popleft
- rotate

### 복습해 볼 문제

- [649. Dota2 Senate](https://leetcode.com/problems/dota2-senate/description)  
Queue 유형의 문제인 것을 몰랐으면 좀 어려웠을 것 같은 문제 (2.5/5)
