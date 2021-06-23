int hammingWeight(uint32_t n) {
    
    unsigned char ans = 0;
    while (n) {
/* 
This is a trick I used in 221 btw. 
Counting and 

*/

        n &= (n-1); 
        ans++;
    }
    return (int) ans;
}