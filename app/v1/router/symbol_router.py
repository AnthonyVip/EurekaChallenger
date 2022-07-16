from fastapi import APIRouter, HTTPException
from fastapi import Depends
from fastapi import status
import requests
from app.v1.schema.symbol_schema import SymbolBase, SymbolResponse
from app.v1.service.auth_service import AuthService
from app.v1.schema.user_schema import User
from app.v1.settings.settings import Settings
from app.v1.utils.api_utils import ValidatedFunction, ValidatedOutputsize
from ratelimit import limits


settings_class = Settings()
auth_class = AuthService()
router = APIRouter(prefix="/api/v1")
_limits = settings_class.get_limit_dict


@limits(calls=_limits["max_requests"], period=_limits["seconds"])
def make_request(url):
    _result = requests.get(url)
    return _result.json()


@router.post("/symbol/", tags=["symbols"],
             status_code=status.HTTP_200_OK,
             response_model=SymbolResponse,
             summary="Get Symbol Info")
def get_symbol(symbol: SymbolBase,
               current_user: User = Depends(auth_class.get_current_user)):
    """
    ## Get Symbol Info

    ### Args
    The app can recive next fields into a JSON
    - Symbol: Symbol to get info
    - function: Optional default TIME_SERIES_DAILY
    - outputsize: Optional default compact
    ### Returns
    - user: Symbol info and Data in Json format
    """
    api_cred = settings_class.get_api_dict
    base_url = api_cred['base_url']
    key = api_cred['key']

    if symbol.outputsize and ValidatedOutputsize(symbol.outputsize):
        outputsize = symbol.outputsize
    else:
        outputsize = "compact"

    if symbol.function and ValidatedFunction(symbol.function):
        function = symbol.function
    else:
        function = "TIME_SERIES_DAILY"

    _url = f"{base_url}function={function}"\
           f"&symbol={symbol.symbol}"\
           f"&outputsize={outputsize}&apikey={key}"

    try:
        _result = make_request(_url)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="api limit reached")

    return SymbolResponse(data=_result,
                          symbol=symbol.symbol,
                          function=function,
                          outputsize=outputsize)
