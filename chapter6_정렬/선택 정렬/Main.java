/*
    Date : 2022년 9월 17일
    Author : 이푸름
    Description: 이것이 코딩 테스트다 선택 정렬 예제
 */
public class Main{
    public static void main(String[] args) {
        int n = 10;
        int [] arr = {7, 4, 8, 0, 3, 9, 1, 6, 5, 2};

        for(int i = 0; i < n; i++)
        {
            int min_index = i;
            for (int j = i + 1; j < n; j++)
            {
                if (arr[min_index] > arr[j])
                {
                    min_index = j;
                }
            }
            int temp = arr[i];
            arr[i] = arr[min_index];
            arr[min_index] = temp;
        }

        for(int i = 0; i < n; i++)
        {
            System.out.print(arr[i] + " ");
        }
    }
}
