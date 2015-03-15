####frcdatapy: A Python API wrapper for the [official FRC (FIRST Robotics Competition) API](http://docs.frceventsprelim.apiary.io/) 
====

Simplifies calls to the FRC API by not having to mess with the requests and just get the data you want. Automatically converts the json responses to python dictionaries. This module is in beta and things may not work. If something doesn't work the way you expected then please create an issue.

####Installation:
---
~~#####Using Pip:~~

~~`pip install frcdatapy`~~

 -- Currently not on PyPi; will be once stable
#####From source:

```
git clone https://github.com/isiah-lloyd/frcdatapy.git
cd frcdatapy
sudo python setup.py install
```

####Quickstart:
---
Before using the API, you must set it up in your project. 
```
import frcdatapy
frcdatapy.setUp('http://example.com/api/', username="exampleUsername", authToken="00000000-0000-0000-0000-000000000000")
```
Replace "http://example.com/api/" to the base URL used to connect to the API. This can either be the Apiary mock server, or the production server.

If you wish to just use the Apiary test server, that's all you need. If you want to use the production server continue:

Replace "exapmleUsername" with the username you got from FIRST

Fill the authToken with the token you are supplied with from FIRST. 

After this, you can pretty much follow the [API docs](http://docs.frcevents.apiary.io/) to use this module. All API calls are prepended with "get_"; for example if you want to get an event schedule the method to call it would become `frcdatapy.get_event_schedule(2015, "PAPI", top=8)`. All required parameter go in the method call in order as shown on the API docs. All optional parameters are named parameters, for example the `top=8` in the example above.


####Contributing:
---
frcdatapy is under the [MIT License](http://en.wikipedia.org/wiki/MIT_License), so feel free to fork and use as you please, as long as you source back to here. We would also love that if you make any improvements (whatever code or documentation) that you submit a pull request and get it into the main project. If you are looking to contribute, have a look at the issues and choose something that interests you. Then you should comment stating that you are starting work on it, to make sure everything goes smoothly. 
