
import os
import unittest


def load_all_test():
    """
    load all testcase
    :return:
    """

    case_path = os.path.join(os.getcwd(), "..\case")
    print(case_path)
    discover = unittest.defaultTestLoader.discover(case_path, pattern="*Case.py", top_level_dir=None)
    print(discover)
    return discover


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(load_all_test())


