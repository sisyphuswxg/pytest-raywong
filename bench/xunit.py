from __future__ import annotations


# setup_class → xUnit风格的类级别设置方法
for i in range(5000):
    exec(
        f"""
class Test{i}:
    @classmethod
    def setup_class(cls): pass      
    def test_1(self): pass
    def test_2(self): pass
    def test_3(self): pass
"""
    )
