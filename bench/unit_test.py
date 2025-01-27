from __future__ import annotations

from unittest import TestCase  # noqa: F401


# 动态创建15000个测试类，每个类中3个测试方法
# setUpClass → 在每个测试类中设置类级别的属性
for i in range(15000):
    exec(
        f"""
class Test{i}(TestCase):
    @classmethod
    def setUpClass(cls): pass
    def test_1(self): pass
    def test_2(self): pass
    def test_3(self): pass
"""
    )
