---
title: Installation
weight: 5
---

PymaxMusic contains both a Python package and a Max package, both of which need to be installed. Pymax uses CNMAT’s osc4py3 library, which you need to install before using. (https://pypi.org/project/osc4py3/)

#### To install the Python package:

Install osc4py3:

{{< tabs >}}
{{% tab name="Windows" %}}
```Bash
py -m pip install osc4py3
```
{{% /tab %}}

{{% tab name="Mac or Linux" %}}
```Bash
python3 -m pip install osc4py3
```
{{% /tab %}}
{{< /tabs >}}

Install pymaxmusic:

{{< tabs >}}
{{% tab name="Windows" %}}
```Bash
py -m pip install pymaxmusic
```
{{% /tab %}}

{{% tab name="Mac or Linux" %}}
```Bash
python3 -m pip install pymaxmusic
```
{{% /tab %}}
{{< /tabs >}}


Conversely, you can install pymaxmusic from its source at github/ims/pymaxmusic.

#### To install the Max package:

From github/ims/pymaxmusic/Max, download the “pymaxmusic_maxpackage” folder and place it in your Max packages folder (probably Documents/Max/Packages).