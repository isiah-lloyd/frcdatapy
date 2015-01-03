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

