from pathlib import Path
from argparse import ArgumentParser
from find.finder import find_test_files, find_config_files
from test.file import TestFile
from test.config import ConfigFile


class YapProject:

    def __init__(self, args):
        self.args = args
        # self.config = YapConfig.find_config()
        self.configs = self.find_configs()
        self.tests = self.find_tests()
        """
        self.discoverer = TestDiscoverer(
            args.test_paths,
            args.group,
            args.exclude,
            args.include,
            self.config,
        )
        """
        # self.setups = TestSetupFinder().find_setups(args.test_paths)

    def run(self):
        for test in self.tests:
            test.set_configs(self.configs)
            test.run()

    def find_tests(self):
        test_files = [TestFile(tf) for tf in find_test_files(self.args.test_paths)]
        # TODO: Filter Test Files

        all_tests = []
        for tf in test_files:
            all_tests.extend(tf.get_tests())

        # TODO: Filter Tests

        return all_tests

    def find_configs(self):
        all_configs = find_config_files(self.args.test_paths)
        configs = [ConfigFile(cf) for cf in all_configs]
        return configs


def get_parser():
    parser = ArgumentParser(
        prog="Yap Test",
        description="Yaml-based API testing framework",
        epilog="Text at the bottom of help",
    )

    parser.add_argument(
        "test_paths", help="Files/Directories that contains tests", type=Path, nargs="*"
    )
    parser.add_argument(
        "-g",
        "--group",
        action="append",
        required=False,
        help="Specify groups of tests. (Can be used multiple times)",
    )
    parser.add_argument(
        "-x",
        "--exclude",
        action="append",
        required=False,
        help="Test names with matching subsstrings will not be run. (Can be used multiple times)",
    )
    parser.add_argument(
        "-i",
        "--include",
        action="append",
        required=False,
        help="Test names with matching subsstrings will be run. (Can be used multiple times)",
    )
    return parser


if __name__ == "__main__":
    args = get_parser().parse_args()
    project = YapProject(args)
    project.run()
