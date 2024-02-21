import abc
from typing import Any


class _ConverterOperation(abc.ABC):
    def __init__(self, stream, key, *args, **kwargs) -> None:
        self._stream = stream
        self._key = key
        self._args = args
        self._kwargs = kwargs
    
    @property
    def stream(self):
        return self._stream

    def run(self):
        return self._stream.filter(self._key, *self._args, **self._kwargs)
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.run()


class ResolutionConverterOperation(_ConverterOperation):
    def __init__(self, stream, width, height) -> None:
        super().__init__(stream, 'scale', w=width, h=height)