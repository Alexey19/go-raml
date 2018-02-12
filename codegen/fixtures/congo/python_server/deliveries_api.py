# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

from flask import Blueprint
try:
    import handlers
except ImportError:
    from . import handlers


deliveries_api = Blueprint('deliveries_api', __name__)


@deliveries_api.route('/deliveries', methods=['GET'])
def deliveries_get():
    """
    Get a list of deliveries
    It is handler for GET /deliveries
    """
    return handlers.deliveries_getHandler()


@deliveries_api.route('/deliveries', methods=['POST'])
def deliveries_post():
    """
    Create/request a new delivery
    It is handler for POST /deliveries
    """
    return handlers.deliveries_postHandler()


@deliveries_api.route('/deliveries/<deliveryId>', methods=['GET'])
def deliveries_byDeliveryId_get(deliveryId):
    """
    Get information on a specific delivery
    It is handler for GET /deliveries/<deliveryId>
    """
    return handlers.deliveries_byDeliveryId_getHandler(deliveryId)


@deliveries_api.route('/deliveries/<deliveryId>', methods=['PATCH'])
def deliveries_byDeliveryId_patch(deliveryId):
    """
    Update the information on a specific delivery
    It is handler for PATCH /deliveries/<deliveryId>
    """
    return handlers.deliveries_byDeliveryId_patchHandler(deliveryId)


@deliveries_api.route('/deliveries/<deliveryId>', methods=['DELETE'])
def deliveries_byDeliveryId_delete(deliveryId):
    """
    Cancel a specific delivery
    It is handler for DELETE /deliveries/<deliveryId>
    """
    return handlers.deliveries_byDeliveryId_deleteHandler(deliveryId)
