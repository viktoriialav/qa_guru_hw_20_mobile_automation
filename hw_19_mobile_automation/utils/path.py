import hw_19_mobile_automation
from pathlib import Path


def relative_from_root(path: str):
    return Path(hw_19_mobile_automation.__file__).parent.parent.joinpath(path).absolute().__str__()
