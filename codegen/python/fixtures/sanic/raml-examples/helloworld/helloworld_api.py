# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

try:
    import handlers
except ImportError:
    from . import handlers


async def helloworld_get(request):
    """
    It is handler for GET /helloworld
    """
    return handlers.helloworld_getHandler(request)
