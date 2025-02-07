from abc import ABC, abstractmethod

# 基类：所有消息处理类都需要继承这个类并实现 process_message 方法
class BaseMessageHandler(ABC):

    @abstractmethod
    def process_message(self, message: str):
        pass
