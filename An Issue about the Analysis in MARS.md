# An Issue about the Analysis in MARS

 I export data using a .json file, which creates automatically after I start test. I use the signal in .json file as raw data of my test, including *General_Fz, General_COPx, General_COPy*.

My test is a body sway test, so there are lots of features showed in Analysis part in MARS. These features can also export by that .json file, however, the value of *sway path* in .json file is different from the value I calculate using raw data. I'm really confused.

Here's a question: I think the signal data in .json file is raw data that hasn't been filted, even if I choose "using fileters(smooth filter and lowpass filter)" in MARS. And if I want get the same value in .json file, I have to filter it in my python code. Is that right?

Follows are my python code and the discription of *sway path*:

> Sway path – total [mm]
> The common length of the trajectory of the COP sway calculated as a sum of the point-to-point Euclidian distances.

```py
def swayPath(x, y):
    length=0
    for i in Length:
        length += sqrt((x[i+1] - x[i]) * (x[i+1] - x[i]) + (y[i+1] - y[i]) * (y[i+1] - y[i]))
    
    return length

feature[0] = swayPath(General_COPx, General_COPy)
```

The value of my calculation is nearly 10 times of that in .json file.



Thank you very much!