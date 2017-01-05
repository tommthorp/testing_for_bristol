import numpy as np

def sinc2d(x, y):
    if x == 0.0 and y == 0.0:
        return 1.0
    elif x == 0.0:
        return np.sin(y) / y
    elif y == 0.0:
        return np.sin(x) / x
    else:
        return (np.sin(x) / x) * (np.sin(y) / y)


def test_sinc2d_normal():
        """Testing case x, y non-zero in sinc2d()"""
        expected_value = 0.25*np.sin(2.0)*np.sin(2.0)
        calculated_value = sinc2d(2.0,2.0)
        assert expected_value == calculated_value


def test_y():
        x=1
        expec = np.sin(x) / x
        calc = sinc2d(x,0)
        assert calc == expdef test_y():
        x=1
        expec = np.sin(x) / x
        calc = sinc2d(x,0)
        assert calc == expecec
