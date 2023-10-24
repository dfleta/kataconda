from src.loose_change import loose_change

def test_cambio_cero():
    assert loose_change(0) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}

def test_cambio_entero_decenas_positivo():
    assert loose_change(56) == {'Nickels': 1, 'Pennies': 1, 'Dimes': 0, 'Quarters': 2}

def test_cambio_negativo():
    assert loose_change(-435) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}

def test_cambio_decimal_positivo_redondeado():
    assert loose_change(4.935) == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(100.25) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 4}
    assert loose_change(0.213) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}

def test_cambio_solo_nickels():
    assert loose_change(5) == {'Nickels': 1, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}

def test_cambio_solo_pennies():
    assert loose_change(3) == {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}
