import io
import sys
import unittest
from unittest.mock import patch

import calculator
import main


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertAlmostEqual(calculator.add(1.5, 2.5), 4.0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)
        self.assertEqual(calculator.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(4, 3), 12)
        self.assertEqual(calculator.multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertAlmostEqual(calculator.divide(1, 3), 0.333333, places=5)
        with self.assertRaises(ValueError):
            calculator.divide(5, 0)

    def test_percentage_change(self):
        self.assertEqual(calculator.percentage_change(110, 100), 0.1)
        self.assertEqual(calculator.percentage_change(90, 100), -0.1)
        with self.assertRaises(ValueError):
            calculator.percentage_change(10, 0)

    def test_compound_growth(self):
        self.assertAlmostEqual(
            calculator.compound_growth(1000, 0.05, 2), 1102.5, places=2
        )
        self.assertEqual(calculator.compound_growth(100, 0, 5), 100)


class TestMain(unittest.TestCase):

    def test_run_operation_add(self):
        self.assertEqual(main.run_operation("add", [2, 3]), 5)

    def test_run_operation_unknown(self):
        with self.assertRaises(ValueError):
            main.run_operation("power", [2, 3])

    def test_run_operation_wrong_operand_count(self):
        with self.assertRaises(ValueError):
            main.run_operation("add", [1])

    def test_main_success(self):
        with patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            result = main.main(["multiply", "6", "7"])
            self.assertEqual(result, 0)
            self.assertEqual(fake_stdout.getvalue().strip(), "42.0")

    def test_main_division_by_zero(self):
        with patch("sys.stderr", new=io.StringIO()) as fake_stderr:
            result = main.main(["divide", "5", "0"])
            self.assertEqual(result, 1)
            self.assertIn("Cannot divide by zero", fake_stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
