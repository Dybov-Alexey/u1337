from car import Car, MonsterTruck

def _q_01():
    """
    ============================================================================
    Часть 1
    ----------------------------------------------------------------------------
    >>> apalkoff_car = Car('Tesla', 'Model S')                  # doctest: +SKIP
    >>> apalkoff_car.color                                      # doctest: +SKIP
    ______

    >>> apalkoff_car.paint('чёрный')                            # doctest: +SKIP
    ______

    >>> apalkoff_car.color                                      # doctest: +SKIP
    ______

    ============================================================================
    Часть 2
    ----------------------------------------------------------------------------
    >>> apalkoff_car = Car('Tesla', 'Model S')                  # doctest: +SKIP
    >>> apalkoff_car.model                                      # doctest: +SKIP
    ______

    >>> apalkoff_car.gas = 10                                   # doctest: +SKIP
    >>> apalkoff_car.drive()                                    # doctest: +SKIP
    ______

    >>> apalkoff_car.drive()                                    # doctest: +SKIP
    ______

    >>> apalkoff_car.fill_gas()                                 # doctest: +SKIP
    ______

    >>> apalkoff_car.gas                                        # doctest: +SKIP
    ______

    >>> Car.gas                                                 # doctest: +SKIP
    ______

    ============================================================================
    Часть 3
    ----------------------------------------------------------------------------
    >>> Car.headlights                                          # doctest: +SKIP
    ______

    >>> apalkoff_car.headlights                                 # doctest: +SKIP
    ______

    >>> Car.headlights = 3                                      # doctest: +SKIP
    >>> apalkoff_car.headlights                                 # doctest: +SKIP
    ______

    >>> apalkoff_car.headlights = 2                             # doctest: +SKIP
    >>> Car.headlights                                          # doctest: +SKIP
    ______

    ============================================================================
    Часть 4
    ----------------------------------------------------------------------------
    >>> apalkoff_car.wheels = 2                                 # doctest: +SKIP
    >>> apalkoff_car.wheels                                     # doctest: +SKIP
    ______

    >>> Car.num_wheels                                          # doctest: +SKIP
    ______

    >>> apalkoff_car.drive()                                    # doctest: +SKIP
    ______

    >>> Car.drive()                                             # doctest: +SKIP
    ______

    >>> Car.drive(apalkoff_car)                                 # doctest: +SKIP
    ______

    ============================================================================
    Часть 5
    ----------------------------------------------------------------------------
    >>> apalkoff_car = MonsterTruck('Монстр', 'Бэтмобиль')      # doctest: +SKIP
    >>> apalkoff_car.drive()                                    # doctest: +SKIP
    ______

    >>> Car.drive(apalkoff_car)                                 # doctest: +SKIP
    ______

    >>> MonsterTruck.drive(apalkoff_car)                        # doctest: +SKIP
    ______

    >>> Car.rev(apalkoff_car)                                   # doctest: +SKIP
    ______
    """
    return 0

# Ниже этого места трогать ничего не нужно.

if __name__ == '__main__':
    import doctest, sys
    finder = doctest.DocTestFinder()
    runner = doctest.DocTestRunner(doctest.OutputChecker(), optionflags=doctest.FAIL_FAST)
    doctest.OutputChecker.output_difference = lambda a, b, c, d: ""
    m = sys.modules.get('__main__')
    for test in finder.find(m, m.__name__):
        if test.name == '__main__': continue
        if test.name.split('.')[1][:2] != '_q': continue
        for example in test.examples: example.options[doctest.SKIP] = False
        if  runner.run(test).failed != 0: break