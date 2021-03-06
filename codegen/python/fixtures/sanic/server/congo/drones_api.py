# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

import handlers


async def drones_get(request):
    """
    Get a list of drones
    It is handler for GET /drones
    """
    return handlers.drones_getHandler(request)


async def drones_post(request):
    """
    Add a new drone to the fleet
    It is handler for POST /drones
    """
    return handlers.drones_postHandler(request)


async def drones_byDroneId_get(request, droneId):
    """
    Get information on a specific drone
    It is handler for GET /drones/<droneId>
    """
    return handlers.drones_byDroneId_getHandler(request, droneId)


async def drones_byDroneId_patch(request, droneId):
    """
    Update the information on a specific drone
    It is handler for PATCH /drones/<droneId>
    """
    return handlers.drones_byDroneId_patchHandler(request, droneId)


async def drones_byDroneId_delete(request, droneId):
    """
    Remove a drone from the fleet
    It is handler for DELETE /drones/<droneId>
    """
    return handlers.drones_byDroneId_deleteHandler(request, droneId)


async def drones_byDroneId_deliveries_get(request, droneId):
    """
    The deliveries scheduled for the current drone
    It is handler for GET /drones/<droneId>/deliveries
    """
    return handlers.drones_byDroneId_deliveries_getHandler(request, droneId)
