from __future__ import annotations


for i in range(1000):
    # 使用exec动态创建函数
    exec(f"def test_func_{i}(): pass")
