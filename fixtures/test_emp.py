import pytest
from emp import Employee

def test_add_emp():
    emp1=Employee()
    assert emp1.add_record(1,'ram')==True
    # assert emp1.add_record(1,'ram')==True
    with pytest.raises(ValueError,match='Record is already there in database'):
        emp1.add_record(1,'ram')