typedef struct {
    // User defined data may be declared here.
    unsigned char tmp;
} Foo;

Foo* fooCreate() {
    Foo* obj = (Foo*) malloc(sizeof(Foo));
    obj -> tmp = 0;
    // Initialize user defined data here.
    
    return obj;
}

void first(Foo* obj) {
    while (obj -> tmp != 0)
        continue;
    // printFirst() outputs "first". Do not change or remove this line.
    printFirst();
    obj -> tmp |= 0b1;
}

void second(Foo* obj) {
    while (obj -> tmp != 1)
        continue;
    // printSecond() outputs "second". Do not change or remove this line.
    printSecond();
    obj -> tmp |= 0b11;
}

void third(Foo* obj) {
    while (obj -> tmp != 0b11)
        continue;
    // printThird() outputs "third". Do not change or remove this line.
    printThird();
    
}

void fooFree(Foo* obj) {
    // User defined data may be cleaned up here.
    free(obj);
}