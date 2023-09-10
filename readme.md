# MOUSE DANCE
> **author** kim, youngseop <br>
> **email address** kim.youngseop.developer@gmail.com

hello, visitor! <br>
we totally understand what you need. <br>
sometimes you juse want to have a great show by the famous mouse dancer. <br>
how about a cup of coffee during the show? :) <br>

![example](https://github.com/kim-youngseop-developer/mousedance/blob/master/example/example.png)

## **INSTALL**

before the installation, <br>

the script `mousedance` is written on the below environment. <br>
as only tested on the environment, we cannot guarantee the execution on other environment. <br>

- **os** `Microsoft Windows 11 Home, 10.0.22621 N/A Build 22621`
- **git** `Git, 2.36.0.windows.1`
- **python** `Python, 3.11.0`
- **pip** `PIP, 22.3 (python 3.11)`

and for the comfortable installation, <br>
we recommend to use `git` to clone the repository. <br>

```batch
:: move to directory where to clone.
cd <path\to\clone>

:: clone the repository.
git clone https://github.com/kim-youngseop-developer/mousedance.git

:: move to the cloned directory "mousedance".
cd mousedance

:: pip install via "requirements.txt".
pip install -r requirements.txt

:: execute batch file.
mousedance
```

the default configuration for the `repeat` is 10 times. <br>
if you want to the never ending show, <br>
please edit the key with following information.

```yaml
# .\configuration.yaml
# for never ending show, set `0` on the key `draw.repeat`.

draw:
  repeat: 0 
```

<br>

---

<br>

## **BATCH FILE**

```batch
python mousedance\__main__.py -p "configuration.yaml"
```

## **CONFIGURATION FILE**

```yaml
# WARNING!
# before editing the configuration file,
# you should be aware of that
# only the keys which is not made use of arguments for constructing an instance
# use the case style `kebab-case`, 
# and others use `snake_case` instead of `kebab-case`.
#
# for example, 
# the key `figure-factories` uses `kebab-case`,
# but the key `another_point` which is a part of arguments to
# construct an instance of the class `Straight` uses `snake_case`.

# ABOUT FACTORY,
# the key `*-factory` which represents the class `Factory` 
# requires a common argument to construct an instance via factory.
# 
# a common argument `name` represents that
# a inherited type name from `<type>-factory`.
#   - expression: a string (e.g., straight)
---

# ABOUT MOVEMENT FACTORY,
# to create an instance inheriting the class `Movement`,
# the class `MovementFactory` represented by the key `movement-factory`
# requires common arguments to construct an instace via factory.
#
# a common argument `time` represents that
# how much time (second) to reach at destination.
#   - expression: an integer or a float (e.g., 0 ~ INF)
#   - minimum: too small value requires an attention for an unexpected situation.
#   - maximum: the value is not limited.
#
# a common argument `steps` represents that
# how many steps to update mouse position.
#   - expression: an integer (e.g., 1 ~ INF)
#   - minimum: too small value requires an attention for an unexpected situation.
#   - maximum: the value is not limited.
movement-factory:
  name: regular
  time: 0.01
  steps: 100

# the key `figure-factories` is a container
# to contain a sequence consisted of a number of the key `figure-factory`.
figure-factories:

  # ABOUT FIGURE FACTORY,
  # to create an instance inheriting the class `Figure`,
  # the class `FigureFactory` represented by the key `figure-factory`
  # requires common arguments to construct an instace via factory.
  #
  # a common argument `point` represents that
  # a point where to place the mouse when each draw starts.
  #   - expression: null or an integer array. (e.g., null or [0, 0])
  #   - 1st index: 0 ~ the screen resolution width.
  #   - 2nd index: 0 ~ the screen resolution height.
  #
  # a common argument `position` represents that 
  # a position where to place the mouse when each draw is over.
  #   - expression: a string (e.g., POINT_CENTER)
  #   - a value `POINT_CENTER`: the center point of the screen resolution.
  #   - a value `POINT_CURRENT`: the current mouse point.
  #   - a value `POINT_CONSTRUCTED`: the point which was provided on a constructor.
  - figure-factory:
      name: straight
      point: null
      position: POINT_CENTER
      another_point: null

  - figure-factory:
      name: straightpatrol
      point: null
      position: POINT_CENTER
      another_point: null

  - figure-factory:
      name: circle
      point: null
      position: POINT_CENTER
      radius: 100

# the key `draw` handles drawing figures 
# which are defined on the key `figure-factories`.
# the arguments `figures_duration`, `repeat`, and `repeat_duration` can be configured.
draw:

  # an argument `figures_duration` represents that
  # a duration time (second) to sleep the thread when drawing each figure is over.
  # the argument can be provided within the below values.
  #   - expression: an integer (e.g., 0 ~ INF)
  #   - minimum: zero requires an attention for an unexpected situation.
  #   - maximum: the value is not limited.
  figures_duration: 3

  # an argument `repeat` represents that
  # how many times to repeat the drawing figures.
  # if the argument is provided as zero,
  # the drawing figures never reach to the end until the keyboard interruption.
  #   - expression: an integer (e.g., 0 ~ INF)
  #   - minimum: zero means that never reach to the end.
  #   - maximum: the value is not limited.
  repeat: 10
    
  # an argument `repeat_duration` represents that
  # a duration time (second) to sleep the thread when each repeat (`figure-factories`) is over.
  # the argument can be provided within the below values.
  #   - expression: an integer (e.g., 3 ~ INF)
  #   - minimum: zero requires an attention for an unexpected situation.
  #   - maximum: the value is not limited.
  repeat_duration: 10
```
