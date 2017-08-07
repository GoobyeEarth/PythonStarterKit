# PythonStarterKit
## TODO
- packaging c.f. http://qiita.com/Kensuke-Mitsuzawa/items/7717f823df5a30c27077
- http://blog-ja.sideci.com/entry/python-lint-pickup-5tools

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
$ pip list --format columns
```
