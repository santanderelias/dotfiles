#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '
alias ct="toolbox enter container-one"
alias gpush='git add . && git commit -m "small tweaks" && git push'
alias tm="tmux attach || tmux new"
export PATH="$HOME/.local/bin:$PATH"

# >>> grok installer >>>
export PATH="$HOME/.grok/bin:$PATH"
[[ -r "$HOME/.grok/completions/bash/grok.bash" ]] && source "$HOME/.grok/completions/bash/grok.bash"
# <<< grok installer <<<
export PATH=~/.npm-global/bin:$PATH


# Added by Antigravity CLI installer
export PATH="/home/okarun/.local/bin:$PATH"
