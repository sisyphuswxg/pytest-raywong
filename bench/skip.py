from __future__ import annotations

import pytest


# 定义一个布尔变量，用于控制是否跳过测试
SKIP = True


# 使用pytest.mark.parametrize装饰器，为test_foo函数创建5000个参数 → 5000个测试用例
@pytest.mark.parametrize("x", range(5000))
def test_foo(x):
    if SKIP:
        pytest.skip("heh")
