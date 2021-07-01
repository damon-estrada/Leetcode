package Easy.Print_in_Order_1114;

class Foo {

    Semaphore lock1, lock2;

    public Foo() {
        lock1 = new Semaphore(0); // zero means no threads can access this lock.
        lock2 = new Semaphore(0);
    }

    public void first(Runnable printFirst) throws InterruptedException {

        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run(); // we autommatically let first() run since it isnt bound by a lock condition.
        lock1.release(); // Now we need to tell the semaphore that we are accepting 1 thread.
    }

    public void second(Runnable printSecond) throws InterruptedException {
        lock1.acquire(); // since we can accept one thread now, we can call second().
        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();
        lock2.release();
    }

    public void third(Runnable printThird) throws InterruptedException {
        lock2.acquire(); // second() will release() lock2 which is what third has been waiting for.
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
        lock2.release();
    }
}