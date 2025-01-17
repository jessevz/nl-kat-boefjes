from enum import Enum
from typing import Union, Dict, Tuple

from boefjes.job_models import BoefjeMeta, NormalizerMeta, NormalizerOutput


class Handler:
    def handle(self, item: Union[BoefjeMeta, NormalizerMeta]):
        raise NotImplementedError()


class BoefjeJobRunner:
    def run(self, boefje_meta: BoefjeMeta, environment: Dict[str, str]) -> Tuple[BoefjeMeta, Union[str, bytes]]:
        raise NotImplementedError()


class NormalizerJobRunner:
    def run(self, normalizer_meta, raw) -> NormalizerOutput:
        raise NotImplementedError()


class RuntimeManager:
    class Queue(Enum):
        BOEFJES = "boefje"
        NORMALIZERS = "normalizer"

    def run(self, queue: Queue) -> None:
        raise NotImplementedError()


class StopWorking(Exception):
    """Exception to tell workers in the runtime to stop working"""
