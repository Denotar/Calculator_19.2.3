from venv.app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_calc_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_calc_division_calculate_correctly(self):
        assert self.calc.division(self, 6, 2) == 3

    def test_calc_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 2, 2) == 0

    def test_calc_adding_calculate_correctly(self):
        assert self.calc.adding(self, 3, 2) == 5

    def test_calc_multiply_calculation_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_calc_division_calculation_failed(self):
        assert self.calc.division(self, 6, 2) == 1

    def test_calc_substraction_calculation_failed(self):
        assert self.calc.subtraction(self, 2, 2) == 1

    def test_calc_adding_calculation_failed(self):
        assert self.calc.adding(self, 3, 2) == 1