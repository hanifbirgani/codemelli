#!/usr/bin/env python

"""Tests for `codemelli` package."""
import pytest

from re import search
from codemelli import codemelli


def test_city_codes_data_returns_dict_type():
    assert isinstance(codemelli.city_codes_data(), dict)


def test_validator_valid_input_is_true():
    assert codemelli.validator(1493933957) is True


def test_validator_invalid_input_is_false():
    assert codemelli.validator(1493933958) is False


def test_validator_raises_valueerror_on_bool_input():
    with pytest.raises(ValueError):
        codemelli.validator(True)


def test_validator_raises_valueerror_on_dict_input():
    with pytest.raises(ValueError):
        codemelli.validator({'test_key': 'test_value'})


def test_validator_raises_valueerror_on_list_input():
    with pytest.raises(ValueError):
        codemelli.validator([1, 2, 3])


def test_validator_raises_valueerror_on_tuple_input():
    with pytest.raises(ValueError):
        codemelli.validator((1, 2))


def test_validator_raises_valueerror_on_string_input():
    with pytest.raises(ValueError):
        codemelli.validator('abcde')


def test_validator_raises_valueerror_on_less_than_10_number_string_input():
    with pytest.raises(ValueError):
        codemelli.validator('12345678')


def test_validator_raises_valueerror_on_less_than_10_integer_input():
    with pytest.raises(ValueError):
        codemelli.validator(1234567)


def test_validator_raises_valueerror_on_less_more_10_integer_input():
    with pytest.raises(ValueError):
        codemelli.validator(12345671234565)


def test_validator_strict_raises_valueerror_on_invalid_city_code_input():
    with pytest.raises(ValueError):
        codemelli.validator(9995872448, strict=True)


def test_get_remainder_raises_typeerror_on_string_input():
    with pytest.raises(TypeError):
        codemelli._get_remainder('string')


def test_get_remainder_raises_typeerror_on_tuple_input():
    with pytest.raises(TypeError):
        codemelli._get_remainder((1, 2))


def test_get_remainder_does_not_raise_typeerror_on_int_input():
    try:
        codemelli._get_remainder(1234567890)
    except Exception:
        assert False


def test_get_remainder_does_not_raise_typeerror_on_list_input():
    try:
        codemelli._get_remainder([1, 2, 3])
    except Exception:
        assert False


def test_generator_raises_a_valueerror_on_input_integer_less_than_3():
    with pytest.raises(ValueError):
        codemelli.generator(12)


def test_generator_raises_a_valueerror_on_input_integer_more_than_3():
    with pytest.raises(ValueError):
        codemelli.generator(1234)


def test_generator_raises_a_valueerror_on_input_string():
    with pytest.raises(ValueError):
        codemelli.generator('abc')


def test_generator_returns_a_10_character_string():
    assert search(r'^\d{10}$', codemelli.generator())


def test_generator_returns_a_10_character_string_with_city_code_input():
    assert search(r'^\d{10}$', codemelli.generator('123'))


def test_lookup_returns_dict_on_valid_input():
    assert isinstance(codemelli.lookup('123'), dict)


def test_lookup_returns_none_on_notfound_key():
    assert codemelli.lookup('999') is None
