from fastapi import HTTPException

HTTP_CODE = 500

def raise_http_exception(message: str):
    raise HTTPException(status_code=HTTP_CODE, detail=message)