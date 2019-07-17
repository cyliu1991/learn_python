import pytest
import os
import pytest_mock
from learn_mock.module import Count


def rm(filename):
    os.remove(filename)


def test_rm(mocker):
    filename = 'file'
    mock_function = mocker.patch('os.remove')
    rm(filename)
    mock_function.assert_called_once_with(filename)


def test_count(mocker):
    count = Count
    mock_method = mocker.patch.object(count, 'add')
    count.add(3, 4)
    assert mock_method.called

def test_function(mocker):
    mock_function = mocker.patch('learn_mock.function.multiply')




