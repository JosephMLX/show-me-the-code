# written by Joseph Meng 2018
# mlx7.xyz

from generate import generate_promotion_code
import redis

code_list = generate_promotion_code(200)
# Create a redis client
redisClient = redis.Redis(host='localhost', port=6379, db=0)

for code in code_list:
    redisClient.lpush('promotion_code', code)

