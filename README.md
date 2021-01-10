# PiCollision

Simulation where **pi** is computed from the collision between two cubes of different masses.

Inspired by this 3Blue1Brown video: <a href=https://www.youtube.com/watch?v=jsYwFizhncE&vl=zh-CN> Why do colliding blocks compute pi? </a>

All collisions are perfectly elastic. The math is as follows:
The blocks will have mass **1kg** and **(10)^n kg**, then the total number of collisions will be **floor(10^(n+1) * pi)**, which is **pi** to **(n+1)** decimal places.

</br>

</br>

Here are some examples.

Block A = **1kg** | Block B = **(100)^1**
<img src="https://media.discordapp.net/attachments/795803904075366400/797605381483266052/unknown.png?width=1153&height=676"
     alt=""
     style="float: left; margin-right: 10px;" />


</br>

Block A = **1kg** | Block B = **(100)^3**
<img src="https://media.discordapp.net/attachments/795803904075366400/797603774004068424/unknown.png?width=1153&height=676"
     alt=""
     style="float: left; margin-right: 10px;" />
