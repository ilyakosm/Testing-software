import unittest
import main
from numpy import array_equal


class TestCountRisk(unittest.TestCase):
    """ Тестирование подсчета матрицы рисков """

    def test_count_risk_matrix_1(self):
        MatrixStart = [
            [172, 81, 193, 560],
            [114, 160, 108, 325],
            [56, 100, 156, 350]
        ]

        MatrixRisk = [
            [0, 79, 0, 0],
            [58, 0, 85, 235],
            [116, 60, 37, 210]
        ]

        MatrixResult = main.count_risk(MatrixStart)

        assert array_equal(MatrixResult, MatrixRisk) == True

    def test_count_risk_matrix_2(self):
        MatrixStart = [
            [6, 5, 2],
            [8, 4, 3],
            [2, 5, 4]
        ]

        MatrixRisk = [
            [2, 0, 2],
            [0, 1, 1],
            [6, 0, 0]
        ]

        MatrixResult = main.count_risk(MatrixStart)

        assert array_equal(MatrixResult, MatrixRisk) == True


class TestProbability(unittest.TestCase):
    """ Тестирование решения, полученного из критерия, основанного на известных вероятностях условиях """

    def test_with_probaility_1(self):
        MatrixRisk = [
            [0, 79, 0, 0],
            [58, 0, 85, 235],
            [116, 60, 37, 210]
        ]

        right_result_list = [15.8, 125.3, 118.7]

        probability_list = [0.1, 0.2, 0.3, 0.4]

        result_list = main.with_probability(MatrixRisk, probability_list)

        assert array_equal(result_list, right_result_list) == True

    def test_with_probaility_2(self):
        MatrixRisk = [
            [4, 1, 0],
            [6, 0, 1],
            [0, 1, 2]
        ]

        right_result_list = [0.6, 0.9, 0.8]

        probability_list = [0.1, 0.2, 0.3]

        result_list = main.with_probability(MatrixRisk, probability_list)

        assert array_equal(result_list, right_result_list) == True


class TestWald(unittest.TestCase):
    """ Тестирование решения, полученного из критерия Вальда """

    def test_Wald_1(self):
        MatrixPay = [
            [172, 81, 193, 560],
            [114, 160, 108, 325],
            [56, 100, 156, 350]
        ]

        right_result_list = [81, 108, 56]

        result_list = main.Wald(MatrixPay)

        assert array_equal(result_list, right_result_list) == True

    def test_Wald_2(self):
        MatrixPay = [
            [2, 0, 2],
            [0, 1, 1],
            [6, 0, 0]
        ]

        right_result_list = [0, 0, 0]

        result_list = main.Wald(MatrixPay)

        assert array_equal(result_list, right_result_list) == True


class TestSavage(unittest.TestCase):
    """ Тестирование решения, полученного из критерия Сэвиджа """

    def test_Savage_1(self):
        MatrixRisk = [
            [0, 79, 0, 0],
            [58, 0, 85, 235],
            [116, 60, 37, 210]
        ]

        right_result_list = [79, 235, 210]

        result_list = main.Savage(MatrixRisk)

        assert array_equal(result_list, right_result_list) == True

    def test_Savage_2(self):
        MatrixRisk = [
            [4, 1, 0],
            [6, 0, 1],
            [0, 1, 2]
        ]

        right_result_list = [4, 6, 2]

        result_list = main.Savage(MatrixRisk)

        assert array_equal(result_list, right_result_list) == True


class TestHurwitzMatrix(unittest.TestCase):
    """ Тестирование решения, полученного из критерия Гурвица, основанном на выигрыше """

    def test_Hurwitz_matrix_1(self):
        MatrixPay = [
            [172, 81, 193, 560],
            [114, 160, 108, 325],
            [56, 100, 156, 350]
        ]

        right_result_list = [320.5, 216.5, 203]

        result_list = main.Hurwitz_matrix(MatrixPay)

        assert array_equal(result_list, right_result_list) == True

    def test_Hurwitz_matrix_2(self):
        MatrixPay = [
            [2, 0, 2],
            [0, 1, 1],
            [6, 0, 0]
        ]

        right_result_list = [1, 0.5, 3]

        result_list = main.Hurwitz_matrix(MatrixPay)

        assert array_equal(result_list, right_result_list) == True


class TestHurwitzRisk(unittest.TestCase):
    """ Тестирование решения, полученного из критерия Гурвица, основанном на риске """

    def test_Hurwitz_risk_1(self):
        MatrixRisk = [
            [0, 79, 0, 0],
            [58, 0, 85, 235],
            [116, 60, 37, 210]
        ]

        right_result_list = [39.5, 117.5, 123.5]

        result_list = main.Hurwitz_risk(MatrixRisk)

        assert array_equal(result_list, right_result_list) == True

    def test_Hurwitz_risk_2(self):
        MatrixRisk = [
            [4, 1, 0],
            [6, 0, 1],
            [0, 1, 2]
        ]

        right_result_list = [2, 3, 1]

        result_list = main.Hurwitz_risk(MatrixRisk)

        assert array_equal(result_list, right_result_list) == True


if __name__ == "__main__":
    unittest.main()