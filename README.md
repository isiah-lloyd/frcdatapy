####frcdatapy: A Python API wrapper for the [official FRC (FIRST Robotics Competition) API](http://docs.frceventsprelim.apiary.io/) 
====

Simplifies calls to the FRC API by not having to mess with the requests and just get the data you want. Automatically converts the json responses to python dictionaries.

**IMPORTANT: THE API IS CURRENTLY IN BETA,THINGS COULD CHANGE WITHOUT NOTICE. USE AT YOUR OWN RISK.**
####Installation:
---
#####Using Pip:

`pip install frcdatapy`

#####From source:

```
git clone https://github.com/isiah-lloyd/frcdatapy.git
cd frcdatapy
sudo python setup.py install
```

####Quickstart:
---
Before using the API, you must set it up in your project. 

`frcdatapy.setUp('Token sampleToken','http://example.com/api/')`

Replace "Token sampleToken" with the token you are supplied with from FIRST. 

Replace "http://example.com/api/" to the base URL used to connect to the API. This can either be the Apiary mock server, or the production server.


####Contributing:
---
frcdatapy is under the [MIT License](http://en.wikipedia.org/wiki/MIT_License), so feel free to fork and use as you please, as long as you source back to here. We would also love that if you make any improvements (whatever code or documentation) that you submit a pull request and get it into the main project. If you are looking to contribute, have a look at the issues and choose something that interests you. Then you should comment stating that you are starting work on it, to make sure everything goes smoothly. 

