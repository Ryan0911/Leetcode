# **232. Implement Queue using Stacks (Easy)**

## **LeetCode URL:**

> https://leetcode.com/problems/implement-queue-using-stacks/

## **Solution Date:**

> 2023/7/11

## **Problem Description:**

> 主要就是使用兩個 Stack 來完成 Queue 的結構，主要有幾個 function 要完成，分別是:
>
> > void push(int x): 將 x push 到 queue 中  
> > int pop(): 回傳最先進 queue 的資料，並將他移除
> > int peak(): 回傳最先進 queue 的資料
> > boolean empty(): 回傳 queue 是否是空的

## **Example:**

    Input
    ["MyQueue", "push", "push", "peek", "pop", "empty"]
    [[], [1], [2], [], [], []]
    Output
    [null, null, null, 1, 1, false]

    Explanation
    MyQueue myQueue = new MyQueue();
    myQueue.push(1); // queue is: [1]
    myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
    myQueue.peek(); // return 1
    myQueue.pop(); // return 1, queue is [2]
    myQueue.empty(); // return false

## **Approach:**

> 解題關鍵已在題目中，可注意了解兩個資料結構的差異點:
>
> > Stack: 先進後出，如疊盤子，後進來的先出去
> > Queue: 先進先出，如排隊，先進來的先出去
> > 可以注意到兩個資料結構的差別，出去的順序顛倒了，所以用兩個 Stack 即可模擬 Queue，兩個 stack 分別命名為 pushStorage & queue，主要的做法大概就是  
> > push => 直接堆到 pushStorage 中
> > pop => 探測是否為空，是空的就將 pushStorage 中的資料全數倒進 queue 中，反之不動，此時在將 queue 進行回傳與移除
> > peak => 同 pop, 但不需移除
> > empty => 檢查 pushStorage & queue 是否為空即可

## **Code**

    class MyQueue
    {
    private:
        stack<int> pushStorage; // 全塞到這
        stack<int> queue;       // queue主要操作的stack
    public:
        MyQueue()
        {
        }

        void push(int x)
        {
            pushStorage.push(x);
        }

        int pop()
        {
            if (queue.empty())
            {
                while (!pushStorage.empty())
                {
                    queue.push(pushStorage.top());
                    pushStorage.pop();
                }
            }
            int top = queue.top();
            queue.pop();
            return top;
        }

        int peek()
        {
            if (queue.empty())
            {
                while (!pushStorage.empty())
                {
                    queue.push(pushStorage.top());
                    pushStorage.pop();
                }
            }
            return queue.top();
        }

        bool empty()
        {
            return (pushStorage.empty() && queue.empty());
        }
    };
