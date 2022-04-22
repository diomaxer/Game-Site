from fastapi import APIRouter

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


@router.get('/')
async def all_games():
    return games


@router.get('/{game_id}')
async def all_games(game_id: int):
    return games[game_id - 1]
