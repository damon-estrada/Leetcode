
double exponentFunction(double x, unsigned int n) {
    double answer = 1;
    double tmp = x;
    
    if (x == 1.0)
        return 1.0;
    if (x == 0.0)
        return 0.0;
    
    
    
     while (n) {
            if (n % 2) { // if exponent not divisible by 2, then multiply with base and subtract 1 from exponent
                answer = answer * tmp;
                n = n - 1;
            }else { // if exponent divisible by 2, then square it
                tmp = tmp * tmp;
                n /= 2;
            }
        }
    return answer;
}

double myPow(double x, int n){
    if (n > 0) {
       return exponentFunction(x, n);
    } else {
        if (n == 0)
            return 1.0;
        else {
            /* Boundary condition -> that's why I used -(n + 1) + 1 */
            return 1/exponentFunction(x, (unsigned int) -(n + 1) + 1);        
    }
}
}


