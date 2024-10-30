# test_count_words.py

from count_words import CountWords

def test_two_words_ending_with_s():
    words = CountWords().count("dogs cats")
    assert words == 2

def test_no_words_at_all():
    words = CountWords().count("dog cat")
    assert words == 0

def test_words_that_end_in_r():
    words = CountWords().count("car bar")
    assert words == 2

def test_mixed_endings():
    words = CountWords().count("car cats")
    assert words == 2

def test_word_ending_with_s_at_end():
    words = CountWords().count("cats")
    assert words == 1

def test_non_alpha_characters():
    words = CountWords().count("dogs, cats.")
    assert words == 2

def test_empty_string():
    words = CountWords().count("")
    assert words == 0

def test_only_non_alpha():
    words = CountWords().count("!!!")
    assert words == 0

def test_non_alpha_after_non_sr_ending_words():
    words = CountWords().count("apple, banana; orange.")
    assert words == 0  # Las palabras no terminan en 's' o 'r', así que el if es siempre falso

def test_case_insensitivity():
    words = CountWords().count("DOGS Cats caR RAT")
    assert words == 3


def test_word_ending_with_r_at_end():
    # Caso extra: una palabra termina en 'r', y el if final se evalúa como True.
    words = CountWords().count("car")
    assert words == 1

def test_sentence_with_mixed_endings():
    # Caso adicional para verificar funcionamiento con mezcla de finales de palabras.
    words = CountWords().count("car star flower")
    assert words == 2

def test_single_word_no_ending_with_s_or_r():
    # Verifica que no cuente ninguna palabra cuando no termina en 's' o 'r'
    words = CountWords().count("flower")
    assert words == 0