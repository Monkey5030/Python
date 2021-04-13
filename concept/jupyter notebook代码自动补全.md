jupyter notebook 中一些实际的技巧。  
* 针对 jupyter notebook 中的 Markdown 文件自动生成目录  
* 自动补全代码  
上述两个功能，都是由 python 的一个 jupyter 扩展插件 Nbextensions 库来实现。安装该库的命令如下：  
`python -m pip install jupyter_contrib_nbextensions`  
然后执行：  
`jupyter contrib nbextension install --user --skip-running-check`  
安装完成后，勾选 Table of Contents 以及 Hinterland。其中 Hinterland 是用来自动补全代码的。  
