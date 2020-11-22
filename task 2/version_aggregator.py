from functools import total_ordering


@total_ordering
class Version:
    PRERELEASE = {"a": -3, "alpha": -3,
                     "b": -2, "beta": -2,
                     "r": -1, "rc": -1
                     }

    def __init__(self, version: str):
        self.version, self.prerelease = self.parse_values(version)

    def __lt__(self, other):
        if self.version < other.version:
            return True
        elif other.version < self.version:
            return False
        elif len(self.prerelease) == 0 and len(other.prerelease) != 0:
            return False
        elif len(self.prerelease) != 0 and len(other.prerelease) == 0:
            return True
        elif self.prerelease < other.prerelease:
            return True
        elif other.prerelease < self.prerelease:
            return False

    def __eq__(self, other):
        if self.version == other.version and self.prerelease == other.prerelease:
            return True
        else:
            return False

    def parse_values(self, version):
        standart_version = version.replace('-', '')
        for index, item in enumerate(standart_version):
            if item.isalpha():
                return self.convert_digits(standart_version[:index]), self.convert_letters(standart_version[index:])
        return self.convert_digits(standart_version), []

    def convert_digits(self, lst):
        digits_list = lst.split('.')
        return [int(i) for i in digits_list]

    def convert_letters(self, lst):
        letters_list = lst.split('.')
        for index, item in enumerate(letters_list):
            if item in self.PRERELEASE:
                letters_list[index] = self.PRERELEASE[item]
            else:
                letters_list[index] = int(item)
        return letters_list


def main():
    to_test = [
        ("1.0.0", "2.0.0"),
        ("1.0.0", "1.42.0"),
        ("1.2.0", "1.2.42"),
        ("1.1.0-alpha", "1.2.0-alpha.1"),
        ("1.0.1b", "1.0.10-alpha.beta"),
        ("1.0.0-rc.1", "1.0.0"),
    ]

    for version_1, version_2 in to_test:
        v1, v2 = Version(version_1), Version(version_2)
        assert v1 < v2, "le failed"
        assert v2 > v1, "ge failed"
        assert v1 != v2, "neq failed"


if __name__ == "__main__":
    main()
