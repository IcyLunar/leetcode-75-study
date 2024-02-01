Array / String
==
### 챕터 이름에서 알 수 있듯 직관적으로 배열과 문자열에 관련된 챕터이다.  
특징으로, 알고리즘적인 개념보다는 언어에서 지원하는 배열과 문자열에 관련된 함수의 개념이해가 더 중요했다.  
해당 챕터에 있는 문제를 풀며 C++에 있는 STL vector/string의 자주 안 쓰던 멤버함수에 대해 알 수 있었다.  
심화적인 개념은 없었기에 문제를 풀며 자주쓰이던 혹은 편리했던 멤버함수에 대해 정리 해볼까 한다. 
****
## ● STL String
### 1. str.length()  
   NULL문자를 제외한 문자열의 길이를 반환한다.
### 2. str.size()
   해당 컨테이너의 크기를 반환한다.
### 3. str1.swap(str2)
   두 문자열을 교환한다.
### 4. str+='a'
   string 형식의 변수에 +연산자가 사용이 가능하다.(연산자를 통해 문자열 뒤에 추가로 문자를 붙일 수 있다.)
## ● STL Vector
### 1. vector<int> v(int size, int num)
   벡터를 num으로 size만큼 초기화한다.
## ● STL Algorithm
### 1. sort(iterator begin, iterator end, compare comp)
   begin에서 end까지 정렬을 한다. comp에 따라 오름차순 내림차순을 정할 수 있다.
### 1. max_element(iterator begin, iterator end), min_element(iterator begin, iterator end)
   begin부터 end까지 원소 중 최대/최소 원소를 구한다.
****
## ● 인상깊은 문제
### 1. 443. String Compression
   주어진 string에서 연속되는 원소를 aa의 경우 a2로 하는 듯 교체하면 되는 간단한 문제이다.  
   다만 교체 과정에서 숫자가 10이상일 경우 아스키코드 변환 과정에서 +'0'을 사용하면 오류가 일어나므로  
   to_string을 이용하여 해결하였다.
