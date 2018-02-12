# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

try:
    import handlers
except ImportError:
    from . import handlers


async def deliveries_get(request):
    """
    Get a list of deliveries
    It is handler for GET /deliveries
    """
    return handlers.deliveries_getHandler(request)


async def deliveries_post(request):
    """
    Create/request a new delivery
    It is handler for POST /deliveries
    """
    return handlers.deliveries_postHandler(request)


async def deliveries_byDeliveryId_get(request, deliveryId):
    """
    Get information on a specific delivery
    It is handler for GET /deliveries/<deliveryId>
    """
    return handlers.deliveries_byDeliveryId_getHandler(request, deliveryId)


async def deliveries_byDeliveryId_patch(request, deliveryId):
    """
    Update the information on a specific delivery
    It is handler for PATCH /deliveries/<deliveryId>
    """
    return handlers.deliveries_byDeliveryId_patchHandler(request, deliveryId)


async def deliveries_byDeliveryId_delete(request, deliveryId):
    """
    Cancel a specific delivery
    It is handler for DELETE /deliveries/<deliveryId>
    """
    return handlers.deliveries_byDeliveryId_deleteHandler(request, deliveryId)
