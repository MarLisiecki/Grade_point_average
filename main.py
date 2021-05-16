## Project for calc your average ##
## Author: Marcin Lisiecki       ##

from helpers_func import Operation
from initial_values import InitialValues


def test_calculate_average():
    init_val = InitialValues()
    content = Operation.open_file(init_val.name_of_file)
    tuple_with_grades_and_points = Operation.extract_data(content, init_val.choice, init_val.sum_of_grades,
                                                          init_val.sum_of_points, init_val.semester, init_val.grades,
                                                          init_val.points, init_val.index)
    assert Operation.calculate_average(tuple_with_grades_and_points) == 4.583


if __name__ == '__main__':
    pass
