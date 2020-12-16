# Gurobi 与数学建模从入门到放弃

介于毕业论文的需求，迫不得已学习 gurobi 和数学建模。

准备记录从入门到放弃的全过程……

## level 0： 学会安装、配置操作环境

### 直接使用 python 安装

以 macOS 为例

首先去官网下载安装包：➡️ [传送门](https://www.gurobi.com/downloads/)

下载安装好之后，用 python 安装到进 python 的库中

```bash
$ cd /Library/gurobi9xx/mac64/ # 9xx是相应的 gurobi 的版本号
$ bash-3.2$ python setup.py install
```

注意事项：如果使用的是 Pycharm 等存在虚拟环境的 IDE，那么安装时必须要使用虚拟环境中的 python 才能安装成功。

```bash
(venv) bash-3.2$ which python
/Users/username/project/venv/bin/python
(venv) bash-3.2$ cd /Library/gurobi9xx/mac64/ # 9xx是相应的 gurobi 的版本号
(venv) bash-3.2$ python setup.py install
```

命令行有如下提示，则算表明成功了：

```bash
running install
running build
running build_py
creating build
creating build/lib
creating build/lib/gurobipy
copying lib/python3.8/gurobipy/__init__.py -> build/lib/gurobipy
copying lib/python3.8/gurobipy/gurobipy.so -> build/lib/gurobipy
running install_lib
creating /Users/xxxxx/venv/lib/python3.8/site-packages/gurobipy
copying build/lib/gurobipy/gurobipy.so -> /Users/xxxxx/venv/lib/python3.8/site-packages/gurobipy
copying build/lib/gurobipy/__init__.py -> /Users/xxxxx/venv/lib/python3.8/site-packages/gurobipy
byte-compiling /Users/xxxxx/venv/lib/python3.8/site-packages/gurobipy/__init__.py to __init__.cpython-38.pyc
running install_egg_info
Writing /Users/xxxxx/venv/lib/python3.8/site-packages/gurobipy-9.1.0-py3.8.egg-info
removing /Library/gurobi910/mac64/build
```

### 使用 Anaconda 作为环境

添加 Gurobi 安装路径

```bash
conda config --add channels https://conda.anaconda.org/gurobi
```

安装 Gurobi 扩展包

```
conda install gurobi
```

查看已经安装的扩展包

```
conda list
```

以上则是两种 gurobi 的安装方法。安装成功后，就可以使用 gurobipy 导入 gurobi 模块了

```python
from gurobipy import *
```

## 从入门到高阶教程参考 official-examples 目录