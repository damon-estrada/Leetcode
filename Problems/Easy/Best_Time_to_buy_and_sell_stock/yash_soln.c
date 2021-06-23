int maxProfit(int* prices, int pricesSize){
    unsigned int minPrice = 1U<<31;
    int maxProfit = 0;
    /* basically keep two vars
    find minprice and max profits together, so they're chronological
    */
    
    for (int i = 0; i < pricesSize; i++) {
        if (prices[i] < minPrice)
            minPrice = prices[i];
        
        if (prices[i] - minPrice > maxProfit)
            maxProfit = prices[i] - minPrice;
    }
    return maxProfit;
}