import pytest
from emp import Employee

# @pytest.fixture
# def obj():
#     print('in fixture')
#     return Employee()


@pytest.fixture
def obj():
    print('in fixture')
    yield Employee()
    print('in teardown')

# @pytest.fixture(scope="class")
# def resource(request):
#     print("setup class")
#     yield
#     print("teardown class")

def test_add_emp(obj):
    # obj=Employee()
    assert obj.add_record(1,'ram')==True
    # assert obj.add_record(1,'ram')==True
    with pytest.raises(ValueError,match='Record is already there in database'):
        obj.add_record(1,'ram')

def test_get_emp(obj):
    assert obj.get_record(1)=='Unknown'