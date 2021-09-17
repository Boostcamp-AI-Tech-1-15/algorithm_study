#include <unistd.h>
#include <stdio.h>

void put_character(char c)
{
    write(1, &c, 1);
}

void print_queens(int arr[10])
{
    int i;

    i = 0;
    while (i < 10)
    {
        put_character(arr[i] + '0');
        i++;
    }
    put_character('\n');
}

int is_valid(int arr[10], int row, int col)
{
    int i;

    i = 0;
    while (i < row)
    {
        if (arr[i] == col || arr[i] + i == row + col ||
            i - arr[i] == row - col)
            return (0);
        i++;
    }
    return (1);
}

void backtrack(int arr[10], int *count, int row)
{
    int col;

    col = 0;
    if (row == 10)
    {
        *count += 1;
        print_queens(arr);
        return;
    }
    while (col < 10)
    {
        if (is_valid(arr, row, col))
        {
            arr[row] = col;
            backtrack(arr, count, row + 1);
        }
        col++;
    }
}

int solve_ten_queens(void)
{
    int arr[10];
    int i;
    int count;

    i = 0;
    count = 0;
    while (i < 10)
    {
        arr[i] = -1;
        i++;
    }
    backtrack(arr, &count, 0);
    return (count);
}

int main()
{
    int answer;

    answer = solve_ten_queens();
    printf("%d\n", answer);
}