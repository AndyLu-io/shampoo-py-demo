
from proxy_fetch import ProxyFetcher

fetcher = ProxyFetcher()
proxies = fetcher.get_proxies(limit=10)
print(proxies)  # 返回代理列表
