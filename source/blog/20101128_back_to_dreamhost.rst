
.. include:: ../include/glossary.rst

Back to Dreamhost [20101128]
===================================

讨厌在线写东西
---------------

用过 |wordpress|_, 用过Drupal, 用过门户们运营的Blog, 都要在线写东西，这
是我所不能接受的，找过一些离线书写的工具，体验也都很差，俺要找个离线写
的，最好能在俺的 |emacs|_ 里写的(blogger.el等体验也很差...)，没找到趁手
的，干脆自己攒吧，于是现在的站点就来了，用 |emacs|_ 写 |rst|_, 提交到
|kd@github|_, 服务器上用crontab定时pull |kd@github|_ 上的 |rst|_, 之后
再用 |sphinx|_ 把 |rst|_ 编译成html放到webserver的根目录下，就好了，一
个静态的站就攒起来了，每次更新就在 |emacs|_ 里舒舒服服的编辑 |rst|_ 之后
commit/push到 |kd@github|_ 上就可以。这样不仅做到了离线写作，站点的
|rst|_ 代码本地有， |kd@github|_ 上有，server上也有，备份也不用额外做了。

我要动态站
---------------

一个静态的站点，貌似没什么意思... 写的狗屁玩意连评论下都不行，我想要一
些动态功能和朋友交流， 该咋办呢...

还是得自己动手丰衣足食啊，先在某 |rst|_ 文件里写个javascript脚本，操作
dom生成用于提交comment的表单，然后做个动态的(Rest风格?)的服务来接收
用户comment时候发起的请求，在前面提到js里加上页面加载时的从动态的(Rest
风格?)的服务那里获取与当前页面相关的comments，灌到页面里就好了。要做就
做，不到2个小时，做成了，现在想在某页面里开启评论功能只要include写有js
脚本的那个 |rst|_ 文件即可。

顺带说一句，这个动态的评论最初我使用 django_ 做的，后来由于发现
pylons_ 更符合我的胃口，就换到 pylons_ 了。

其他还需要什么动态服务，基本就两个思路:

- 看有现成的第三方的线上服务能直接用不，有的话直接拿来主义。
- 上一条中没有的话就自己整一个，按comment功能的方式加上。

为什么说 "Back to Dreamhost"?
-----------------------------

2007年就买了 |dh|_ 的虚拟主机，那时还用 |wordpress|_, |dh|_ 上也没有
fastcgi支持，基本只能放php程序和静态的东西，后来因为一次服务器数据转移
停了下服务，|dh|_ 为了补偿就给升级成 **存储不限，流量不限** 的账号了，
但是我为了方便自己折腾，忘了去年还是今年初买了个低配的VPS, 在上面跑些
自己的程序以及做一些不能说太细的事情，前面的我所那些工作都是在我用那个
VPS的时候完成的，也是放到那VPS上的。

但是，这个周末，我把这些都搬回DreamHost上了。才发现现在 |dh|_ 的php都
是fastcgi方式在跑了(我土...), 静态页面的迁移体不用说了，在上面用
fastcgi跑 pylons_ 倒是折腾了一番，先是因为我的 '追新强迫症' 让我启用
|dh|_ 自带的 Python 2.5.2 自己装了个 2.7, 之后开始测试fastcgi就开始不
断500了，log里也只说什么 header byte(0) 之类的， 后来在 fastcgi里打印
了下环境变量以及sys.path，发现少了一些egg路径(因为我在.bashrc自己加了
条 PYTHONPATH, easy_install装到这个PYTHONPATH里面了)，然后我有把fcgi改
成让cgi handler处理，发现error.log里有东西了，说paster.deploy找不到...
真相大白了...

说下整个步骤吧:

**安装Python**

我装到了$HOME/local下 (configure的时候指定--prefix=$HOME/local),之后
在.bashrc里写:

.. code-block:: bash

  export PATH=$HOME/local/bin:$HOME/local/script:$PATH
  export PYTHONPATH=$HOME/local/lib/python
  alias python=$HOME/local/bin/python

之所以要 export PYTHONPATH=$HOME/local/lib/python 是因为那些python的本
地library(比如_socket.so)都装在了这里，而这个路径没在sys.path里。

之后安装easy_install(setuptools), 然后用easy_install安装pylons, flup,
sqlalchemy, mysql-python等包，按惯例这些包会被装到
$HOME/local/lib/python2.7/site-packages/下，但是由于前面我 export
PYTHONPATH=$HOME/local/lib/python, 导致这些包都装在了
$HOME/local/lib/python 下面，造成了fastcgi脚本里需要额外
的设置路径。 其实把$HOME/local/lib/python下面的eggs移到
$HOME/local/lib/python2.7/site-packages/下估计也可以。

**dispatch.fcgi**

.. code-block:: python

  #!$HOME/local/bin/python

  import os
  import sys
  import glob
  def add_path_and_eggs(path):
      eggs=glob.glob(path+"/*.egg")
      [sys.path.insert(0,e) for e in eggs]
      sys.path.insert(0,path)

  add_path_and_eggs("$HOME/local/lib/python")
  add_path_and_eggs('$HOME/local/lib/python2.7/site-packages')
  other_path=['',
              '$HOME/local/lib/python27.zip',
              '$HOME/local/lib/python2.7',
              '$HOME/local/lib/python2.7/plat-linux2',
              '$HOME/local/lib/python2.7/lib-tk',
              '$HOME/local/lib/python2.7/lib-old',
              '$HOME/local/lib/python2.7/lib-dynload']
  [sys.path.insert(0,e) for e in other_path]

  import logging
  from paste.deploy import loadapp

  config_file = "$HOME/xxx/pylon-app/production.ini"
  wsgi_app = loadapp('config:'+config_file)

  def serve_with_flup():
      from flup.server.fcgi import WSGIServer
      logging.config.fileConfig(config_file)
      WSGIServer(wsgi_app).run()

  serve_with_flup()


**.htaccess**

.. code-block:: bash

  #AddHandler cgi-script .cgi
  AddHandler fastcgi-script .fcgi
  Options +FollowSymLinks +ExecCGI

  RewriteEngine On
  RewriteRule ^dispatch\.fcgi/ - [L]
  RewriteRule ^(.*)$ dispatch.fcgi [L]

**经验，提示**

- |dh|_ 上fcgi出错时不好找原因，可以把fcgi当cgi跑来看看错误信息

.. include:: ../include/footer.rst
.. include:: ../include/comments.rst