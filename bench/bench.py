from __future__ import annotations

import sys


if __name__ == "__main__":
    import cProfile
    import pstats

    """
    noqa 是 no quality assurance 的缩写
    F401 是一个特定的错误代码，表示 module imported but unused（模块已导入但未使用）
    这个注释是给代码检查工具（如 flake8）看的，告诉它忽略 "未使用的导入" 警告

    - 为什么需要这个注释？
    在这个文件中，pytest 看起来像是未被直接使用（只在字符串中通过 pytest.cmdline.main 引用）
    但实际上这个导入是必需的，因为 cProfile.run() 在执行时需要能够访问到 pytest 模块
    为了防止代码检查工具报错，我们使用 # noqa: F401 显式地告诉它这个导入是有意为之的

    → 导入 pytest，即使看起来没有直接使用它，这也是必需的，请代码检查工具不要报警告
    """
    import pytest  # noqa: F401

    script = sys.argv[1:] if len(sys.argv) > 1 else ["empty.py"]

    # prof: 性能分析数据的输出文件名，cProfile会将所有的性能数据分析（如函数调用次数、执行时间等）都保存到这个文件中
    # prof文件是临时的，主要用于在性能分析过程中存储和读取数据。运行完成后，你可以删除这个文件，因为它只是中间产物
    cProfile.run(f"pytest.cmdline.main({script!r})", "prof")

    # 从prof文件读取性能统计数据
    p = pstats.Stats("prof")
    # 从文件路径中移除目录名
    p.strip_dirs()
    # 按累积时间排序（降序），对应的是cumtime字段 
    # cumtime → 整体耗时最多的函数（包括它调用的所有子函数的时间），可以看到程序中的主要性能瓶颈
    p.sort_stats("cumulative")
    # 打印前500行统计数据
    # print(p.print_stats(500))
    print(p.print_stats(10))    # 修改为10，测试用 - raywong

