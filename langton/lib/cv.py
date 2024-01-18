from cv2 import VideoWriter  # pylint: disable=no-name-in-module, # noqa: F401
from cv2 import VideoWriter_fourcc  # pylint: disable=no-name-in-module, # noqa: F401


def codec_from_code(code: str) -> int:
    return VideoWriter_fourcc(*code)
