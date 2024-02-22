def test_one():
    expect = 1
    actual = 1
    assert expect == actual

def test_two():
    expect = 2
    actual = 2
    assert expect == actual

# setup/teardown
# 模块级别 setup_module/teardown_module 开始于模块始末，生效一次
# 函数级别 setup_function/teardown_function 对每条函数用例生效（不在类中）
# 类级 setup_class/teardown_class 只在类中前后运行一次（在类中）
# 方法级别 setup_method/teardown_method 开始于方法始末（在类中）
