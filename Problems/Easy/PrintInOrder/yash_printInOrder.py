class Foo:
    def __init__(self):
        self.tmp = 0 
        # Kinda using a variable to lock and release.


    def first(self, printFirst: 'Callable[[], None]') -> None:
        while(self.tmp != 0):
            continue
            
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.tmp = self.tmp | 1


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while (self.tmp != 1):
            continue
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.tmp = self.tmp | 11


    def third(self, printThird: 'Callable[[], None]') -> None:
        while (self.tmp != 11):
            continue
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.tmp = self.tmp | 111