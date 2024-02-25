Hash Map / Set
===
### Hashing이 이용된 자료구조이다.  
### 난이도 : ★★★☆☆
### 이해도 : ★★☆☆☆
특징으로는, Map의 경우 Key와 Value값이 있으며 Set의 경우 Key값이 유일하다.
두 구조 모두 Key값의 경우 중복을 허용하지 않지만, Map의 Value값은 중복이 가능하다.
쉽게 이해하자면 Map은 Python의 Dictionary와 유사해보인다.  Set의 경우는 집합과 비슷하다 이해하면 편할 것 같다.
기존에 두 구조에 대한 개념적인 이해만 하고있어 코드작성 간 어려움이 다소 있었다.
****
## ● 인상깊은 문제
### 1. 2352. Equal Row and Column Pairs
  STL Map에서 map<KEY, VALUE>의 형식으로 맵이 선언되는데 KEY에 STL vector도 들어 갈 수 있다.
  이를 활용하여 행을 맵에넣어 열과 비교하면 쉽게 해결된다.
