<h1 align="center">Simple Python Scripts</h1>

<p align="center">
  <a href="https://github.com/TheK4n">
    <img src="https://img.shields.io/github/followers/TheK4n?label=Follow&style=social">
  </a>
  <a href="https://github.com/TheK4n/scripts">
    <img src="https://img.shields.io/github/stars/TheK4n/scripts?style=social">
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
[<h2>Dict to Object</h2>](misc/7_dict_to_object/)

Example:
```python
ob = MyObject(a="1", b={"c": 2})
print(ob.b.c)  # 2
```

```python
data = {"a": "1", "b": {"c": 2}}
ob = MyObject()
ob.from_dict(data)
print(ob.b.c)  # 2
```


<a id="chapter-3"></a>
[<h2>Morse</h2>](misc/9_morse/)

Encodes text to and from morse code:\
```--.. -. -.--``` -> ```zny```

**morse_sound.py** creates wav file with morse code from text


<a id="chapter-3"></a>
[<h2>Math</h2>](misc/1_math/coordinates.py)

```python
c = Coordinates(1, -1)
print(c.cartesian())  # Coordinates<(x=1.0, y=-1.0)>  cartesian coordiantes
print(c.polar())  # Coordinates<(r=1.414, phi=-0.785)>  polar coordinates
print("Degrees:", c.polar().phi.degrees)  # Degrees: -44.977  radians to degrees
```


<h1 align="center"><a href="#top">▲</a></h1>
