# hps-behave
[![CircleCI](https://circleci.com/gh/hiptest/hps-behave.svg?style=svg)](https://circleci.com/gh/hiptest/hps-behave)
[![Build Status](https://travis-ci.org/damianlacomba/hps-behave.svg?branch=master)](https://travis-ci.org/damianlacomba/ahorcado2020))

Hiptest publisher samples with Behave

In this repository you'll find tests generated in Behave format from [Hiptest](https://hiptest.com), using [Hiptest publisher](https://github.com/hiptest/hiptest-publisher).

The goals are:

 * to show how tests are exported in Behave.
 * to check exports work out of the box (well, with implemented actionwords)

System under test
------------------

The SUT is a (not that much) simple coffee machine. You start it, you ask for a coffee and you get it, sometimes. But most of times you have to add water or beans, empty the grounds. You have an automatic expresso machine at work or at home? So you know how it goes :-)

Update tests
-------------


To update the tests:

    hiptest-publisher -c behave.conf --only=features,step_definitions

The tests are generated in the [``features``](https://github.com/hiptest/hps-behave/tree/master/features) directory.

Run tests
---------


To build the project and run the tests, use the following command:

    behave --junit --junit-directory results

The SUT implementation can be seen in [``src/coffee_machine.py``](https://github.com/hiptest/hps-behave/blob/master/src/coffee_machine.py)

The test report is generated in ```results/```
