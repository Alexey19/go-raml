
from .Address import Address
from .City import City
from .api_response import APIResponse
from .unmarshall_error import UnmarshallError

class UsersService:
    def __init__(self, client):
        self.client = client



    async def users_byUserId_address_byAddressId_get(self, addressId, userId, headers=None, query_params=None, content_type="application/json"):
        """
        get address id
        of address
        It is method for GET /users/{userId}/address/{addressId}
        """
        uri = self.client.base_url + "/users/"+userId+"/address/"+addressId
        resp = await self.client.get(uri, None, headers, query_params, content_type)
        try:
        	return Address(await resp.json())
        except ValueError as msg:
        	raise UnmarshallError(resp, msg)
        except:
        	raise UnmarshallError(resp)
        


    async def users_byUserId_delete(self, userId, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for DELETE /users/{userId}
        """
        uri = self.client.base_url + "/users/"+userId
        return await self.client.delete(uri, None, headers, query_params, content_type)


    async def getuserid(self, userId, headers=None, query_params=None, content_type="application/json"):
        """
        get id
        It is method for GET /users/{userId}
        """
        uri = self.client.base_url + "/users/"+userId
        resp = await self.client.get(uri, None, headers, query_params, content_type)
        try:
        	return City(await resp.json())
        except ValueError as msg:
        	raise UnmarshallError(resp, msg)
        except:
        	raise UnmarshallError(resp)
        


    async def users_byUserId_post(self, data, userId, headers=None, query_params=None, content_type="application/json"):
        """
        post without request body
        It is method for POST /users/{userId}
        """
        uri = self.client.base_url + "/users/"+userId
        return await self.client.post(uri, data, headers, query_params, content_type)


    async def users_delete(self, data, headers=None, query_params=None, content_type="application/json"):
        """
        delete with request body
        It is method for DELETE /users
        """
        uri = self.client.base_url + "/users"
        resp = await self.client.delete(uri, data, headers, query_params, content_type)
        try:
        	return City(await resp.json())
        except ValueError as msg:
        	raise UnmarshallError(resp, msg)
        except:
        	raise UnmarshallError(resp)
        


    async def get_users(self, data, headers=None, query_params=None, content_type="application/json"):
        """
        First line of comment.
        Second line of comment
        It is method for GET /users
        """
        uri = self.client.base_url + "/users"
        return await self.client.get(uri, data, headers, query_params, content_type)


    async def option_users(self, headers=None, query_params=None, content_type="application/json"):
        """
        It is method for OPTIONS /users
        """
        uri = self.client.base_url + "/users"
        return await self.client.options(uri, None, headers, query_params, content_type)


    async def create_users(self, data, headers=None, query_params=None, content_type="application/json"):
        """
        create users
        It is method for POST /users
        """
        uri = self.client.base_url + "/users"
        resp = await self.client.post(uri, data, headers, query_params, content_type)
        try:
        	return City(await resp.json())
        except ValueError as msg:
        	raise UnmarshallError(resp, msg)
        except:
        	raise UnmarshallError(resp)
        
