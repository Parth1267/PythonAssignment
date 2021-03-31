# Demonstrate how to customize logging output

import logging

# TODO: add another function to log from
extraData = {'user': 'user@gmail.com'}


def anotherFuc():
    logging.debug("This is a debug-level log message ", extra=extraData)


def main():

    # set the output file and debug level, and
    # TODO: use a custom formatting specification
    fmtstr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d User:%(user)s %(message)s"
    datestr = "%m/%d/%Y %I:%M:%S %p"

    logging.basicConfig(filename="output1.log",
                        level=logging.DEBUG,
                        format=fmtstr,
                        datefmt=datestr)

    logging.info("This is an info-level log message", extra=extraData)
    logging.warning("This is a warning-level message", extra=extraData)
    anotherFuc()


if __name__ == "__main__":
    main()
