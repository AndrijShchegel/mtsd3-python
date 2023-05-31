import numpy
from fastapi import APIRouter

router = APIRouter()


@router.get('/matrix')
def matrix() -> dict:
    first = numpy.random.random_integers(0, 9, (10, 10))
    second = numpy.random.random_integers(0, 9, (10, 10))
    combine = numpy.dot(first, second)
    return {
        'first matrix': first.tolist(),
        'second matrix': second.tolist(),
        'combine matrix': combine.tolist()
    }

