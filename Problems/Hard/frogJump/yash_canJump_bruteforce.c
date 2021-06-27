#include <stdio.h>
#include <stdlib.h>

// int ** memoization = NULL;
bool newOne(int * stones,int stonesSize, int lastJump, int curr, int next)
{
    bool answer = false;
    
    if (curr == stonesSize -1 && next == stonesSize) {
        // printf("here true");
        return true;
    }
    if (next >= stonesSize) {
        // printf("here false");
        return false;
    }
    
    if (stones[next] > stones[curr] + lastJump + 1)
        return false;
    
    if (stones[curr] + lastJump + 1 == stones[next]) {
        // printf("third stones[curr] = %d, lastJump = %d, stones[next] = %d answer = %d\n", stones[curr], lastJump+1, stones[next], answer);
        answer = newOne(stones, stonesSize, lastJump + 1, next, next + 1);
    }
        
    if (stones[curr] + lastJump - 1 == stones[next]) {
        // printf("second stones[curr] = %d, lastJump = %d, stones[next] = %d answer = %d\n", stones[curr], lastJump-1, stones[next], answer);
        answer = answer || newOne(stones, stonesSize, lastJump -1 , next, next + 1);
    }
    
    if (stones[curr] + lastJump == stones[next]) {
        /* if stones[curr] + lastJump == stones[next] then this is it.
        Now change curr to next and next to next + 1, see if lastJump-1, lastJump, lastJump +1 yields to any positive outcome.
        */
        // printf("first stones[curr] = %d, lastJump = %d, stones[next] = %d answer = %d \n", stones[curr], lastJump, stones[next], answer);
        answer = answer || newOne(stones, stonesSize, lastJump, next, next + 1);
    } 
        
    if (stones[next] < stones[curr] + lastJump + 1)
        answer = answer || newOne(stones, stonesSize, lastJump, curr, next + 1);

    // printf("%d \n", answer);
    return answer;
}

bool canCross(int* stones, int stonesSize) {
    if (stones[1] - stones[0] != 1) // first jump must be 1
        return false;    
    return newOne(stones, stonesSize, 1, 0, 1);
}
