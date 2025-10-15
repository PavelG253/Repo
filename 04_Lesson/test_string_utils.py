import pytest
from string_utils import StringUtils


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_text, expected_text",
    [
           ("test", "Test"),
           ("work or test", "Work or test"),
           ("TEST", "TEST")
    ]
)
def positive_capitalize_test(input_text, expected_text):
    capitalizer = StringUtils()
    assert capitalizer.capitalize(input_text) == expected_text


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_text, expected_text",
    [
           ("", ""),
           ("   ", "   ")
    ]
)
def negative_capitalize_test(input_text, expected_text):
    capitalizer = StringUtils()
    assert capitalizer.capitalize(input_text) == expected_text


def capitalize_none():
    utils = StringUtils()
    with pytest.raises(AttributeError):
        utils.capitalize(None)


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_text, expected_text",
    [
           ("   type", "type"),
           ("    auto or manual", "auto or manual"),
           ("   TEST", "TEST")
    ]
)
def positive_trim_test(input_text, expected_text):
    trimmer = StringUtils()
    assert trimmer.trim(input_text) == expected_text


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_text, expected_text",
    [
           ("   ", ""),
           ("", "")
    ]
)
def negative_trim_test(input_text, expected_text):
    trimmer = StringUtils()
    assert trimmer.trim(input_text) == expected_text


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_text, expected_text",
    []
)
def negative_empty_trim_test(input_text, expected_text):
    trimmer = StringUtils()
    assert trimmer.trim(input_text) == expected_text


def trim_none():
    utils = StringUtils()
    with pytest.raises(AttributeError):
        utils.trim(None)


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_text, search, expected_text",
    [
           ("test", "s", True),
           ("work or worker", "w", True),
           ("TEST", "T", True)
    ]
)
def positive_container_test(input_text, search, expected_text):
    container = StringUtils()
    res = container.contains(input_text, search)
    assert res == expected_text


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_text, search, expected_text",
    [
           ("", "s", False),
           ("  ", "t", False),
           ("TEST", "s", False)
    ]
)
def negative_container_test(input_text, search, expected_text):
    container = StringUtils()
    res = container.contains(input_text, search)
    assert res == expected_text


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_text, search, expected_text",
    []
)
def negative_empty_container_test(input_text, search, expected_text):
    container = StringUtils()
    res = container.contains(input_text, search)
    assert res == expected_text


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_text, delebol, expected_text",
    [
           ("trest", "r", "test"),
           ("sort or zor", "o", "srt r zr"),
           ("QUESTY", "Y", "QUEST")
    ]
)
def positive_extractor_test(input_text, delebol, expected_text):
    extraction = StringUtils()
    assert extraction.delete_symbol(input_text, delebol) == expected_text


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_text, delebol, expected_text",
    [
           ("Typo", "S", "Typo"),
           ("", "", ""),
           (" ", " ", "")
    ]
)
def negative_extractor_test(input_text, delebol, expected_text):
    extraction = StringUtils()
    assert extraction.delete_symbol(input_text, delebol) == expected_text
