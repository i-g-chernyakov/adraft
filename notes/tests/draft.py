# import pytest
#
#
# def setup():
#     print("basic setup into module")
#
#
# def teardown():
#     print("basic teardown into module")
#
#
# def setup_module(module):
#     print("module setup")
#
#
# def teardown_module(module):
#     print("module teardown")
#
#
# def setup_function(function):
#     print("function setup")
#
#
# def teardown_function(function):
#     print("function teardown")
#
#
# def test_numbers_3_4():
#     print
#     "test 3*4"
#     assert 3 * 4 == 12
#
#
# def test_strings_a_3():
#     print
#     "test a*3"
#     assert 'a' * 3 == 'aaa'
#
#
# class TestUM:
#     def setup(self):
#         print("basic setup into class")
#
#     def teardown(self):
#         print("basic teardown into class")
#
#     def setup_class(cls):
#         print("class setup")
#
#     def teardown_class(cls):
#         print("class teardown")
#
#     def setup_method(self, method):
#         print("method setup")
#
#     def teardown_method(self, method):
#         print("method teardown")
#
#     def test_numbers_5_6(self):
#         print
#         "test 5*6"
#         assert 5 * 6 == 30
#
#     def test_strings_b_2(self):
#         print
#         "test b*2"
#         assert 'b' * 2 == 'bb'



# Test exception
# def f():
#     print(1/0)
#
# def test_exception():
#     with pytest.raises(ZeroDivisionError):
#         f()


#  Test fixture
# @pytest.fixture()
# def resource_setup(request):
#     print("resource_setup")
#
#     def resource_teardown():
#         print("resource_teardown")
#
#     request.addfinalizer(resource_teardown)
#
#
# def test_1_that_needs_resource(resource_setup):
#     print("test_1_that_needs_resource")
#
#
# def test_2_that_does_not():
#     print("test_2_that_does_not")
#
#
# def test_3_that_does_again(resource_setup):
#     print("test_3_that_does_again")



# Test parametrize
# def strange_string_func(str):
#     if len(str) > 5:
#         return str + "?"
#     elif len(str) < 5:
#         return str + "!"
#     else:
#         return str + "."
#
#
# @pytest.fixture(scope="function", params=[
#     ("abcdefg", "abcdefg?"),
#     ("abc", "abc!"),
#     ("abcde", "abcde.")],
#     ids=["len>5","len<5","len==5"]
#     )
# def param_test(request):
#     return request.param
#
#
# def test_strange_string_func(param_test):
#     (input, expected_output) = param_test
#     result = strange_string_func(input)
#     assert result == expected_output

# def idfn_x(val):
#     return "x=({0})".format(str(val))
#
#
# def idfn_y(val):
#     return "y=({0})".format(str(val))
#
#
# @pytest.mark.parametrize("x", [-1, 2], ids=idfn_x)
# @pytest.mark.parametrize("y", [-10, 11], ids=idfn_y)
# def test_cross_params(x, y):
#     assert True
#
#
# @pytest.mark.parametrize("x", [-1, 2], ids=["negative x", "positive y"])
# @pytest.mark.parametrize("y", [-10, 11], ids=["negative y", "positive y"])
# def test_cross_params_2(x, y):
#     assert True


