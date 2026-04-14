---
title: Python Async Programming Summary / Python 异步编程总结
tags: [python, async, asyncio, programming, concurrency]
date: 2026-04-14
---

# Python Async Programming Summary / Python 异步编程总结

## 1. Core Concepts / 核心概念

### Event Loop / 事件循环

The event loop is the core of asyncio. It runs and manages the execution of coroutines.
事件循环是 asyncio 的核心。它运行和管理协程的执行。

```python
import asyncio

async def main():
    print("Event loop is running")
    await asyncio.sleep(1)
    print("Done")

# Run the event loop
asyncio.run(main())
```

### Coroutine / 协程

A coroutine is a special function that can pause and resume execution. Defined with `async def`.
协程是一种可以暂停和恢复执行的特殊函数。使用 `async def` 定义。

```python
import asyncio

async def fetch_data(url: str, delay: float = 1.0) -> str:
    """Simulate fetching data from a URL"""
    print(f"Fetching {url}...")
    await asyncio.sleep(delay)  # Non-blocking wait
    print(f"Completed {url}")
    return f"Data from {url}"

async def main():
    result = await fetch_data("https://api.example.com")
    print(result)

asyncio.run(main())
```

### Task / 任务

Tasks are used to schedule coroutines concurrently. They wrap coroutines for parallel execution.
任务用于并发调度协程。它们包装协程以进行并行执行。

```python
import asyncio

async def worker(name: str, delay: float):
    for i in range(3):
        print(f"{name} working {i}")
        await asyncio.sleep(delay)
    return f"{name} finished"

async def main():
    # Create tasks for concurrent execution
    task1 = asyncio.create_task(worker("Task-A", 0.5))
    task2 = asyncio.create_task(worker("Task-B", 0.7))
    
    # Wait for both to complete
    results = await asyncio.gather(task1, task2)
    print(results)

asyncio.run(main())
```

### Future / 未来对象

A Future is a low-level awaitable object representing a result that will be available later.
Future 是一个低级可等待对象，表示将来可用的结果。

```python
import asyncio

async def set_result(future: asyncio.Future, value: str):
    await asyncio.sleep(1)
    future.set_result(value)

async def main():
    loop = asyncio.get_event_loop()
    future = loop.create_future()
    
    # Schedule setting the result
    asyncio.create_task(set_result(future, "Hello Future!"))
    
    # Wait for result
    result = await future
    print(result)

asyncio.run(main())
```

## 2. Async/Await Syntax Key Points / async/await 语法要点

### Key Rules / 关键规则

| Rule / 规则 | Description / 描述 |
|------------|-------------------|
| `async def` | Defines a coroutine function / 定义协程函数 |
| `await` | Pauses coroutine until awaitable completes / 暂停协程直到可等待对象完成 |
| `asyncio.run()` | Entry point for async programs / 异步程序入口点 |
| `asyncio.create_task()` | Schedules coroutine concurrently / 并发调度协程 |
| `asyncio.gather()` | Runs multiple coroutines concurrently / 并发运行多个协程 |

### Important Notes / 重要注意事项

1. **await can only be used inside async functions** / await 只能在 async 函数内使用
2. **Blocking calls freeze the event loop** / 阻塞调用会冻结事件循环
3. **Use asyncio.to_thread() for CPU-bound tasks** / 使用 asyncio.to_thread() 处理 CPU 密集型任务

```python
import asyncio
import time

async def blocking_example():
    # WRONG: This blocks the event loop
    # time.sleep(1)
    
    # CORRECT: Non-blocking wait
    await asyncio.sleep(1)

async def main():
    await blocking_example()

asyncio.run(main())
```

## 3. Common Use Cases / 常见用例

### I/O Bound Operations / I/O 密集型操作

- Network requests (HTTP, WebSocket, database) / 网络请求
- File operations / 文件操作
- API calls / API 调用

```python
import asyncio
import aiohttp

async def fetch_url(session: aiohttp.ClientSession, url: str) -> str:
    async with session.get(url) as response:
        return await response.text()

async def fetch_all(urls: list[str]) -> list[str]:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        return await asyncio.gather(*tasks)

# Usage (requires aiohttp: pip install aiohttp)
# urls = ["https://api.github.com", "https://httpbin.org"]
# results = asyncio.run(fetch_all(urls))
```

### Concurrent Task Execution / 并发任务执行

```python
import asyncio

async def process_item(item_id: int, delay: float = 0.5):
    await asyncio.sleep(delay)
    return f"Processed item {item_id}"

async def process_batch(items: list[int], max_concurrent: int = 5):
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def limited_process(item_id):
        async with semaphore:
            return await process_item(item_id)
    
    tasks = [limited_process(item_id) for item_id in items]
    return await asyncio.gather(*tasks)

async def main():
    items = list(range(10))
    results = await process_batch(items)
    print(results)

asyncio.run(main())
```

### Timeout Handling / 超时处理

```python
import asyncio

async def slow_operation():
    await asyncio.sleep(5)
    return "Completed"

async def main():
    try:
        # Wait max 2 seconds
        result = await asyncio.wait_for(slow_operation(), timeout=2.0)
        print(result)
    except asyncio.TimeoutError:
        print("Operation timed out!")

asyncio.run(main())
```

## 4. Best Practices / 最佳实践

1. **Use asyncio.run() as the main entry point** / 使用 asyncio.run() 作为主入口
2. **Avoid blocking calls in async code** / 避免在异步代码中使用阻塞调用
3. **Use asyncio.gather() for concurrent execution** / 使用 asyncio.gather() 进行并发执行
4. **Handle exceptions properly with try/except** / 使用 try/except 正确处理异常
5. **Use context managers for resources** / 对资源使用上下文管理器

## 5. Quick Reference / 快速参考

```python
import asyncio

# Basic pattern / 基本模式
async def main():
    await some_async_function()

asyncio.run(main())

# Concurrent execution / 并发执行
async def main():
    results = await asyncio.gather(
        task1(),
        task2(),
        task3()
    )

# With timeout / 带超时
async def main():
    try:
        result = await asyncio.wait_for(task(), timeout=5.0)
    except asyncio.TimeoutError:
        pass

# Create background task / 创建后台任务
async def main():
    task = asyncio.create_task(background_work())
    # Do other work...
    await task  # Wait for completion
```

---

*Generated: 2026-04-14*
*For LLM Wiki Project*
