# SimpleVersionBumper
Given a version and possible option, increase a portion of the version by one and set lower portions to zero.

## NAME
    bumpversion - Given a version, such as 1.23.45, various portions of it can be increased.

## DESCRIPTION
    By default the least significant portion of the version is increased by one.

    The -m option will increase the middle portion.

    The -M option will increase the most significant portion.


    Examples:

    python bumpversion.py 1.23.45
    1.23.46

    python bumpversion.py -m 1.23.45
    1.24.0

    python bumpversion.py -M 1.23.45
    2.0.0


    Versions can also be piped into the tool and output to stdout:

    echo 1.23.45 | python bumpversion.py
    1.23.46

    echo 1.23.45 | python bumpversion.py -m
    1.24.0

    echo 1.23.45 | python bumpversion.py -M
    2.0.0

## FUNCTIONS
    main(args)

## FILE
    SimpleVersionBumper/bumpversion.py

