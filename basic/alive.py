import threading

# 检查 threading.Thread 是否缺少 isAlive 方法
if not hasattr(threading.Thread, "isAlive"):
    # 给 threading.Thread 添加 isAlive 方法
    threading.Thread.isAlive = threading.Thread.is_alive

# 示例代码
def worker():
    print("Thread is running.")

# 创建并启动线程
t = threading.Thread(target=worker)
t.start()

# 使用 isAlive() （通过补丁兼容）
if t.isAlive():
    print("Thread is alive.")
t.join()
