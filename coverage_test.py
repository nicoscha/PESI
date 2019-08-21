from unittest import main

import coverage

if __name__ == '__main__':
    C = coverage.Coverage()
    C.start()
    main(module='tests.test_main', exit=False)
    C.stop()
    C.report()
    C.save()
    C.html_report()