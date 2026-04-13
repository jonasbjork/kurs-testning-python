# Övning 20 - Hypothesis

## Del 1: Sortering

Skriv minst tre property-based-tester för `sorted()`. Kör testerna med `pytest -v`

```python
from hypothesis import given
from hypothesis import strategies as st


@given(st.lists(st.integers()))
def test_sort_preserves_length(xs):
    assert len(sorted(xs)) == len(xs)


@given(st.lists(st.integers()))
def test_sort_is_ordered(xs):
    result = sorted(xs)
    for i in range(len(result) - 1):
        assert result[i] <= result[i + 1]


@given(st.lists(st.integers()))
def test_sort_idempotent(xs):
    assert sorted(sorted(xs)) == sorted(xs)
```

## Del 2: Strängfunktion

```python
def reverse_words(text: str) -> str:
    return ' '.join(text.split()[::-1])
```

Skriv properties:
- Anropa `reverse_words` två gånger, kommer originalet tillbaka?
- Vilka edge cases hittar Hypothesis?

## Del 3: Bonus - Calculator

Testa med matematiska egenskaper:
- `add(a, b) == add(b, a)`
- `add(a, 0) == a`
- `multiply(a, 1) == a`

