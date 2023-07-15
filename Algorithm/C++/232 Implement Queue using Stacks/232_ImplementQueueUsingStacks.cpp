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