from typing import Sequence, Union, Any, Optional

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """abcd efgh ijkl mnop qrst uvw xyz"""
    if lst:
        return lst[0]
    else:
        return None

