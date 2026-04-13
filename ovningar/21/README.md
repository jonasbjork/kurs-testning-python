# Övning 21 - Mutationstestning

Använd Calculator-projektet från vecka 1. Du behöver ha både `calculator.py` och `test_calculator.py` filerna. Kopiera in dem i den här katalogen.

För att mutmut skall fungera behöver vi skapa en `pyproject.toml`-fil i katalogen:

```toml
[tool.mutmut]
paths_to_mutate = [ "calculator.py" ]
```

Nu kan du köra `mutmut`:

```sh
mutmut run
```

Kontrollera resultaten med:

```sh
mutmut results
    calculator.xǁCalculatorǁsubtract__mutmut_1: no tests
    calculator.xǁCalculatorǁmultiply__mutmut_1: no tests
    calculator.xǁCalculatorǁdivide__mutmut_6: survived
    calculator.xǁCalculatorǁpower__mutmut_1: no tests
    calculator.xǁCalculatorǁsqrt__mutmut_1: survived
    calculator.xǁCalculatorǁsqrt__mutmut_2: survived
    calculator.xǁCalculatorǁsqrt__mutmut_6: survived
    calculator.xǁCalculatorǁsqrt__mutmut_7: survived
    calculator.xǁCalculatorǁmodulo__mutmut_1: survived
```

Undersök varje överlevande mutant:

```sh
mutmut show calculator.xǁCalculatorǁdivide__mutmut_6
```

Skriv nya tester för de mutanter som har `no tests` och de tester där mutanterna överlever (`survived`).

Kör `mutmut` igen och kontrollera att ditt mutation score ökar.

## Reflektera

1. Vad hittade `mutmut` som coverage-rapporten inte visar?
2. Vilka mutanter är ekvivalenta?
3. Hur ändrade det här ditt sätt att tänka kring tester?

