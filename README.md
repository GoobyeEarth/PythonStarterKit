# PythonStarterKit

## What is this?
This is a starter kit of python project to try libraries I frequently use.

You can try these libraries
- click (command line parser) https://github.com/pallets/click
- hacking (flake8 plugins) https://github.com/openstack-dev/hacking
- unittest (auto test tools) https://docs.python.org/3/library/unittest.html

## Make Environment (macOS Sierra version 10.12.6)
```
# install anyenv
$ git clone https://github.com/riywo/anyenv ~/.anyenv

$ vim ~/.bash_profile
#####################################
if [ -d $HOME/.anyenv ] ; then
    export PATH="$HOME/.anyenv/bin:$PATH"
    eval "$(anyenv init -)"
    # tmux対応
    for D in `\ls $HOME/.anyenv/envs`
    do
        export PATH="$HOME/.anyenv/envs/$D/shims:$PATH"
    done
fi
#####################################
$ source ~/.bash_profile
# make update **env easily
$ mkdir -p $(anyenv root)/plugins
$ git clone https://github.com/znz/anyenv-update.git $(anyenv root)/plugins/anyenv-update

# install pyenv
$ anyenv install pyenv

$ pyenv install 3.6.2
$ git clone https://github.com/yyuu/pyenv-virtualenv ~/.anyenv/envs/pyenv/plugins/pyenv-virtualenv
$ vim ~/.bash_profile
#####################################
eval "$(pyenv virtualenv-init -)"
#####################################
$ pyenv virtualenv 3.6.2 python-starter-kit

# install libraries
$ pip install -r requirements.txt
```
