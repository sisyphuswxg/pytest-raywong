from __future__ import annotations

import pytest


# 创建一个模块级别的fixture，带有966个参数
@pytest.fixture(scope="module", params=range(966))
def foo(request):
    return request.param


# 两个使用该fixture的测试函数
# - 每个测试函数会被执行966次（即一共966x2=1932个测试用例），每次执行使用不同的参数值，
def test_it(foo):
    pass


def test_it2(foo):
    pass
