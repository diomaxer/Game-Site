from typing import List

from fastapi import APIRouter
from starlette import status

from backend.models.games_model import Game

router = APIRouter()

games = [{
    'id': 1,
    'name': 'Inspector Insector',
    'cool': 10000
}, {
    'id': 2,
    'name': 'Couple Finder 1942',
    'cool': 3000
}]


@router.get(
    path="/",
    description="Get all products",
    status_code=status.HTTP_200_OK,
    tags=['games'],
    response_model=List[Game],
)
async def all_games():
    return games


@router.get(
    path='/{game_id}',
    description="Get all products",
    status_code=status.HTTP_200_OK,
    tags=['games'],
    response_model=Game,
)
async def all_games(game_id: int):
    return games[game_id - 1]
