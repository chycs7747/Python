기준을 피봇이라고 해요.

피봇 값을 아무거나 값을 하나 잡고, 얘를 기준으로 두 부분으로 나누는 거에요

그리고 나누어진 두 부분에서 왼쪽을 피봇보다 작은 수, 오른쪽을 피봇보다 큰 수로 옮기고 각각을 정렬해요. 그러면 최종적으로 합치면 모두 정렬된 상태겟죠. (예시에서 어떻게 피봇기준으로 작은값을 왼쪽, 큰값을 오른쪽으로 옮기는지 보여드릴 겁니다.)



그 다음에는 아무곳이나 다시 잡고 위 행동을 반복해요.



평균시간: O(n logn) 최악: O(n^2)

평균시간이유: n만큼 파티션을 나누는데, 정렬할 데이터가 절반식 줄으므로



참고)  가운데를 피봇으로 잡아야 시간을 더 크게 줄일 수 있음. 그 이유는 예시 2개를 보며 천천히 생각해봅시다.

예시)

1. 가운데를 피봇으로 잡아도 효과를 보기 힘든 경우 (여기서 주의할 점은 pivot을 기준으로 왼쪽 오른쪽 정렬하는 것은 고려하지 않았습니다.)

[ 7, 5, 1, 2, 3 ]

가운데 값인 pivot=1, 로 두고 첫번째 정렬을 완료하면, 1이 가장 작은 수이기 때문에 1과 7을 바꿔줍니다.

[ 1, 5, 7, 2, 3 ]

pivot=7로 두고 두번째 정렬을 하면, 7이 가장 큰 수이므로, 3과 바꾸어줍니다. 그러면,



[ 1, 5, 3, 2, 7 ] 이 됩니다. 이런식으로 선택한  pivot값이 계속 가장 큰 값, 가장 작은 큰 값으로 설정된다면, 시간복잡도는 최악인 O(n^2)이 됩니다.



2. 일반적인 quicksort

[3,9,4,7,'5',0,1,6,8,2]

pivot=5, start=3, end=2

pivot=5 로 두고, 배열의 양 끝 값인 시작점을 3, 종료점을 2로 둔다. 그러면 위에처럼 초기설정이 되겠죠. 이제 우리는 pivot보다 왼쪽에 있는 값들 중 pivot 미만의 값을 왼쪽, 초과의 값을 오른쪽에 배치할 것입니다.

3은 5보다 작으므로 건너뛰고, 9는 5보다 크므로 start를 9로 바꿔줍니다.

start=3 -> 5 이상태로 start를 묶어두고 이번엔 end값을 봅니다. 맨 처음 2를 보는데, pivot값인 5보다작습니다. 자 이제 묶여있는 start값과 end값을 교환해줍니다.

그러면 [3,2,4,7,'5',0,1,6,8,9] 가 됩니다.

이제 start포인트와 end포인트를 각각 한개씩 이동시켜 줍니다.

pivot=5, start=4, end=8이 되겠죠

start가 5보다 작으니 건너 뛰고, 7은 5보다 크니 start=5->7로 바꾸어줍니다. 그리고 묶어둡니다. 이제 end로 넘어가서 8을 보면 pivot값인 5보다 큽니다. 다음으로 6도 마찬가지로 pivot값보다 크므로 건너뜁니다. 그 다음 1은 pivot값보다 작네요. 이제 묶여있던 start값인 7과 1을 바꾸어줍니다.



정리하면, [3,2,4,1,'5',0,7,6,8,9]가 됩니다.

start와 end 포인트를 한칸씩 옮기면,

pivot=5, start=5, end=0이 됩니다. 

같은 원리로, start값인5는 pivot이하의 값(즉, 작지 않은 값)이므로 start로 묶어둡니다. 그리고 0을 보니 5보다 작으므로, start와 end를 교환해줍니다. 

[3,2,4,1,0,'5',7,6,8,9]

그리고 start값과 end값을 한칸씩 옮기면, start 포인트가 end포인트보다  커져버리게 됩니다. 그러면 start 포인트 반환 후 종료.

그 값을 mid라는 변수에 저장한다면,

이제부터는 mid-1를 끝으로하는 좌측배열을 이용해서 위 행동을 재귀, 재귀가 끝나면 역으로 mid점를 시작으로 하는 우측배열도 마찬가지로 재귀를 실행 시키도록 한다.

재귀의 종료 조건은 sort의 시작점이 끝점과 같아질 때이다.



[0,1,2,9,7,5,4]일 때를 생각해보자.