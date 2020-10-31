# 基于贝叶斯优化寻求乙醇在铝表面吸附能最低点

## 计算原理
dft可以优化得到一定区域内的能量最低点，但是得到的能量只能是局部最低点不一定是全局最低点，[BOSS](https://cest-group.gitlab.io/boss/index.html)使用贝叶斯优化算法为目标函数建立N维替代模型，在铝表面的一个周期性区域内进行进行拟合，寻求一个周期内的能量最低点，即全局最低点。


## 代码实现
代码主要由几个部分构成
### `boss.in`
这是boss的输入文件，里面指定了目标函数、目标函数的定义域值域以及优化的条件迭代次数等具体可以下载boss的[帮助文档](https://cest-group.gitlab.io/boss/_downloads/198b6e1dd6c2667838dfd04f0e971413/BOSS_manual.pdf)。
### `user_func`
这是输出目标函数值的python脚本，依赖于python3.8.5
boss将氧原子坐标输入，该脚本将铝原子及乙醇分子的坐标输出交由``calc.sh`脚本，并将返回的能量值输出给boss。
### `cala.sh`
这是将完整的坐标输出给DFT进行优化并求解能量的bash脚本。

## 脚本使用
### 初次使用
初次使用可以直接在根目录下
```
boss o boss.in
```
开始优化，计算完成后在`boss.out`文件最后取得优化得到的最低点。
如果对优化结果不满意，可以修改`boss.rst`文件中`iterpts`的值，并执行
```
boss op boss.rst
```
boss将会基于之前的结果进行更多次的优化。

### 再次使用
boss执行后将会输出很多文件，如果由于某些特殊原因需要重新开始优化，请删除根目录下的`data\`，`calc_folder`,`boss.rst`,`boss.out`并用`i_example.txt`文件替换`i.txt`
在这之后在重新开始优化。




<p align="right">杜淏霖</p>
<p align="right">2020.10.31</p>