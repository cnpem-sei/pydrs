from timeit import timeit

setup = """
import pydrs
drs = pydrs.EthDRS('10.0.6.56', 5000)
drs.slave_addr = 5"""

for i in range(0, 10):
    print(
        timeit("drs.read_vars_fbp(); drs.read_vars_common();", setup=setup, number=100)
    )
