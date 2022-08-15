# 1. 导入模板
from redis import Redis

# 2. 创建redis-cli的类实例
# redis cli = Redis()
redis_cli = Redis(host='localhost',
                  port=6379,
                  db=0)

# 3. 按照上午的指令调用
redis_cli.set('mingzi', 'itheima')
# 获取数据
name = redis_cli.get('mingzi')
print(name)

redis_cli.delete('name')