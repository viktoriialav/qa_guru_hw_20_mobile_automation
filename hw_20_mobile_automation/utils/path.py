from pathlib import Path

import hw_20_mobile_automation


def abs_path_from_root(path: str):
    return Path(hw_20_mobile_automation.__file__).parent.parent.joinpath(path).absolute().__str__()
