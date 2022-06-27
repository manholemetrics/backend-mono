import datetime
import logging

import asyncio

import aiocoap.resource as resource
import aiocoap
import json
import requests

class Update(resource.Resource):
    
    async def render_get(self, request):
        print(request)
        # TODO design
        # message = json.loads(request.payload)
        return aiocoap.Message(payload='')
    
class Measurements(resource.Resource):
    
    async def render_post(self, request):
        print(request.payload)
        message = json.loads(request.payload)
        print(message)
        # response = requests.post('url', json=message)
        # response = response.text
        response = 'received'
        return aiocoap.Message(payload=response)
        
# logging setup

# logging.basicConfig(level=logging.INFO)
# logging.getLogger("coap-server").setLevel(logging.DEBUG)

async def main():
    # Resource tree creation
    root = resource.Site()
    root.add_resource(['.well-known', 'core'],
            resource.WKCResource(root.get_resources_as_linkheader))
    root.add_resource(['update'], Update())
    root.add_resource(['measurements'], Measurements())

    await aiocoap.Context.create_server_context(root)

    # Run forever
    await asyncio.get_running_loop().create_future()

if __name__ == "__main__":
    asyncio.run(main())
    
    
