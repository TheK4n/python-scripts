<h1 align="center">Simple Python Scripts</h1>

<p align="center">
  <a href="https://github.com/TheK4n">
    <img src="https://img.shields.io/github/followers/TheK4n?label=Follow&style=social">
  </a>
  <a href="https://github.com/TheK4n/scripts">
    <img src="https://img.shields.io/github/stars/TheK4n/python-scripts?style=social">
  </a>
</p>

* [Project description](#chapter-0)
* [RoadMap](#chapter-1)
* [Dict to Object](#chapter-2)
* [Morse](#chapter-3)
* [OOP Patterns](patterns)


<a id="chapter-0"></a>
## Project description 

Simple Python scripts by kan.


<a id="chapter-1"></a>
## RoadMap

1. Script Decodes morse sound signals 


<a id="chapter-2"></a>
[<h2>Dict to Object</h2>](misc/07_dict_to_object/)

Example:
```python
data = {"a": "1", "b": {"c": 2}}
ob = MyObject()
ob.set(data)
print(ob.b.c)  # 2
```


<a id="chapter-3"></a>
[<h2>Morse</h2>](misc/09_morse/)

Encodes text to and from morse code:\
```--.. -. -.--``` -> ```zny```

**morse_sound.py** creates wav file with morse code from text


<a id="chapter-3"></a>
[<h2>Math</h2>](misc/01_math/coordinates/coordinate_system.py)

```python
c = Cartesian(2, 3).create_polar()
print("Radius:", c.rho)
print("Degrees:", c.phi.degrees)
```


<h1 align="center"><a href="#top">▲</a></h1>
