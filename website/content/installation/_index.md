---
title: Installation
weight: 5
---

PymaxMusic contains both a Python package and a Max package, both of which need to be installed. Pymax uses CNMAT’s [osc4py3](https://pypi.org/project/osc4py3/) library, which you need to install before using.  

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

#### To install the Max package:

Download the [pymaxmusic_maxpackage folder](https://github.com/danielims/pymaxmusic/tree/master/maxmsp) and place it in your Max packages folder (probably _Documents/Max (version number)/Packages_). Since each pymax project includes both a Python module and a Max patch, the maxhelp files for each Max object in pymaxmusic also have corresponding Python modules. These are included in the maxpackage folder.

You can also download both the Python and the Max packages from its [source](https://github.com/danielims/pymaxmusic).
