import pytest


def test_concate_positive_nums(client):
    """Валидация метода GET /concate/{num1}/{num2}.
    num1, num2 - целые положительные числа.
    Ожидаемый результат согласно документации в Swagger - сумма num1+num2."""
    response = client.get('/concate/12/22')
    assert response.data == 34


def test_concate_negative_nums(client):
    """Валидация метода GET /concate/{num1}/{num2}.
    num1, num2 - целые отрицательные числа.
    Ожидаемый результат - сумма num1+num2."""
    response = client.get('/concate/-12/-22')
    assert response.data == -34


def test_concate_float_nums(client):
    """Валидация метода GET /concate/{num1}/{num2}.
    num1, num2 - дробные числа.
    Ожидаемый результат - TypeError."""
    with pytest.raises(TypeError):
        response = client.get('/concate/12.0/22.0')


def test_subtract_positive_nums(client):
    """Валидация метода GET /subtract/{num1}/{num2}.
    num1, num2 - целые положительные числа.
    Ожидаемый результат согласно документации в Swagger - разность num1-num2."""
    response = client.get('/subtract/6/3')
    assert response.data == 3


def test_subtract_negative_nums(client):
    """Валидация метода GET /subtract/{num1}/{num2}.
    num1, num2 - целые отрицательные числа.
    Ожидаемый результат - разность num1-num2."""
    response = client.get('/subtract/-6/-3')
    assert response.data == -3


def test_subtract_float_nums(client):
    """Валидация метода GET /subtract/{num1}/{num2}.
    num1, num2 - дробные числа.
    Ожидаемый результат - TypeError."""
    with pytest.raises(TypeError):
        response = client.get('/subtract/6.0/3.0')


def test_multiple_positive_nums(client):
    """Валидация метода GET /multiple/{num1}/{num2}.
    num1, num2 - целые положительные числа.
    Ожидаемый результат согласно документации в Swagger - произведение num1*num2."""
    response = client.get('/multiple/4/3')
    assert response.data == 12


def test_multiple_negative_nums(client):
    """Валидация метода GET /multiple/{num1}/{num2}.
    num1, num2 - целые отрицательные числа.
    Ожидаемый результат - произведение num1*num2."""
    response = client.get('/multiple/-4/-3')
    assert response.data == 12


def test_multiple_res_negative(client):
    """Валидация метода GET /multiple/{num1}/{num2}.
    num1, num2 - целые числа. Результат вычисления - отрицательное число.
    Ожидаемый результат - произведение num1*num2."""
    response = client.get('/multiple/-4/3')
    assert response.data == -12


def test_multiple_float_nums(client):
    """Валидация метода GET /multiple/{num1}/{num2}.
    num1, num2 - дробные числа.
    Ожидаемый результат - TypeError."""
    with pytest.raises(TypeError):
        response = client.get('/multiple/4.0/3.0')


def test_division_positive_nums(client):
    """Валидация метода GET /division/{num1}/{num2}.
    num1, num2 - целые числа.
    Ожидаемый результат согласно документации в Swagger - num1//num2."""
    response = client.get('/division/12/2')
    assert response.data == 6


def test_division_negative_nums(client):
    """Валидация метода GET /division/{num1}/{num2}.
    num1, num2 - целые отрицательные числа.
    Ожидаемый результат - num1//num2."""
    response = client.get('/division/-12/-2')
    assert response.data == 6


def test_division_res_negative(client):
    """Валидация метода GET /division/{num1}/{num2}.
    num1, num2 - целые числа. Результат вычисления - отрицательное число.
    Ожидаемый результат - num1//num2."""
    response = client.get('/division/-12/2')
    assert response.data == -6


def test_zero_division(client):
    """Валидация метода GET /division/{num1}/{num2}.
    num1, num2 - целые числа. num2 = 0.
    Ожидаемый результат - ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        response = client.get('/division/12/0')


def test_division_float_nums(client):
    """Валидация метода GET /division/{num1}/{num2}.
    num1, num2 - дробные числа.
    Ожидаемый результат - TypeError."""
    with pytest.raises(TypeError):
        response = client.get('/division/12.0/2.0')


def test_exponent_positive(client):
    """Валидация метода GET /exponent/{num1}/{num2}.
    num1, num2 - целые положительные числа.
    Ожидаемый результат - num1**num2."""
    response = client.get('/exponent/4/2')
    assert response.data == 16


def test_exponent_negative(client):
    """Валидация метода GET /exponent/{num1}/{num2}.
    num1, num2 - целые числа. num1 - отрицательное число.
    Ожидаемый результат - num1**num2."""
    response = client.get('/exponent/-4/2')
    assert response.data == 16


def test_exponent_res_negative(client):
    """Валидация метода GET /exponent/{num1}/{num2}.
    num1, num2 - целые числа. Результат вычисления - отрицательное число.
    Ожидаемый результат - num1**num2."""
    response = client.get('/exponent/-4/3')
    assert response.data == -64


def test_exponent_base_negative(client):
    """Валидация метода GET /exponent/{num1}/{num2}.
    num1, num2 - целые числа. num2 - отрицательное число.
    Ожидаемый результат - num1**num2."""
    response = client.get('/exponent/4/-2')
    assert response.data == 0.0625


def test_exponent_float_nums(client):
    """Валидация метода GET /exponent/{num1}/{num2}.
    num1, num2 - дробные числа.
    Ожидаемый результат - TypeError."""
    with pytest.raises(TypeError):
        response = client.get('/exponent/4.0/2.0')
