from fastapi import APIRouter


router = APIRouter(
    prefix='/api/v1/cars',
    tags=['cars'],
)

@router.get('/')
def list_cars():
    return {
        'cars': [
            {'id': 1, 'modelo': 'Mobi'},
            {'id': 2, 'modelo': 'Onix'},
            {'id': 3, 'modelo': 'Kwid'},
        ]
    }
