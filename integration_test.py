import sys
from file_cache import file_cache

# TODO accept a command line argument - on run 1, run function and have its output save. On second, have its output load.

# Track the number of executions. The way this test works is that at the end of run 2, this number should be ZERO.
exec_count = 0


class TestObject:
    """Object that exists only to be saved and loaded. Stores a basic value to make sure that it isn't corrupted."""

    def __init__(self, n):
        self.n = n

    def __eq__(self, other):
        return self.n == other.n

    def __str__(self):
        return str(self.n)

    def __repr__(self):
        return f"{TestObject}({str(self)})"

    def __hash__(self):
        return hash(repr(self))


@file_cache("./cache_dir/test_int_noarg")
def test_int_noarg():
    global exec_count
    exec_count += 1
    return 1


@file_cache("./cache_dir/test_object_noarg")
def test_object_noarg():
    global exec_count
    exec_count += 1
    return 1


@file_cache("./cache_dir/test_int_arg")
def test_int_arg(x):
    global exec_count
    exec_count += 1
    return x


@file_cache("./cache_dir/test_object_arg")
def test_object_arg(o):
    global exec_count
    exec_count += 1
    return o


@file_cache("./cache_dir/test_multi_return")
def test_multi_return():
    global exec_count
    exec_count += 1
    return 1, 2


run_number = int(sys.argv[1])

if run_number == 1:  # First run, execute functions and populate file cache.
    test_int_noarg()
    test_object_noarg()
    test_int_arg(1)
    test_object_arg(TestObject(2))
    test_multi_return()
    assert exec_count == 5
elif run_number == 2:  # Second run, execute functions, check return vals and that there were no executions.
    assert test_int_noarg() == 1
    assert test_object_noarg() == 1
    assert test_int_arg(1) == 1
    assert test_object_arg(TestObject(2)) == TestObject(2)
    a, b = test_multi_return()
    assert a == 1
    assert b == 2
    assert exec_count == 0
