from Calculator import Calculator


def test_calculator_init():
    instruction = "add 2\napply 2"
    calculator = Calculator(instruction)
    assert calculator is not None


def test_compute_add():
    instruction = "add 2\napply 0"
    calculator = Calculator(instruction)
    assert calculator.Compute() == 2


def test_compute_subtract():
    instruction = "subtract 2\napply 4"
    calculator = Calculator(instruction)
    assert calculator.Compute() == 2


def test_compute_multiply():
    instruction = "multiply 2\napply 1"
    calculator = Calculator(instruction)
    assert calculator.Compute() == 2


def test_compute_divide():
    instruction = "divide 2\napply 4"
    calculator = Calculator(instruction)
    assert calculator.Compute() == 2


def test_compute_apply():
    instruction = "apply 1"
    calculator = Calculator(instruction)
    assert calculator.Compute() == 1


def test_compute_0():
    instruction = "add 2\nmultiply 3\napply 10"
    calculator = Calculator(instruction)
    assert calculator.Compute() == 36


def test_compute_1():
    instruction = "multiply 3\nadd 2\napply 10"
    calculator = Calculator(instruction)
    assert calculator.Compute() == 32


