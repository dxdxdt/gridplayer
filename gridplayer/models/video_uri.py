from typing import Union

from pydantic import AnyUrl, ValidationError

from gridplayer.params.extensions import SUPPORTED_MEDIA_EXT


class VideoURL(AnyUrl):
    max_length = 2083


class PathNotAbsoluteError(ValidationError):
    code = "path.not_absolute"
    msg_template = 'path "{path}" is not absolute'


class PathExtensionNotSupportedError(ValidationError):
    code = "path.ext_not_supported"
    msg_template = 'path extension "{path}" is not supported'


VideoURI = Union[VideoURL]
