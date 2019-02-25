update:
    brew update
.PHONY: update

linuxbrew:
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"
.PHONY: linuxbrew

linuxbrewalt:
    git clone https://github.com/Homebrew/brew ~/.linuxbrew/Homebrew
    mkdir ~/.linuxbrew/bin
    ln -s ../Homebrew/bin/brew ~/.linuxbrew/bin
    eval $(~/.linuxbrew/bin/brew shellenv)
.PHONY: linuxbrewalt

homebrew:
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
.PHONY: homebrew

homebrewalt:
    mkdir homebrew && curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C homebrew
.PHONY: homebrewalt

tigerbrew:
    ruby -e "$(curl -fsSkL raw.github.com/mistydemeo/tigerbrew/go/install)"
.PHONY: tigerbrew

getcask:
    brew install cask
.PHONY: getcask

doctor:
    brew doctor
.PHONY: doctor

caskdoctor:
    brew cask doctor
.PHONY: caskdoctor

curlrc:
    ls -A ~ | grep .curlrc
.PHONY: curlrc

caskstyle:
    brew cask style --force --verbose --debug
.PHONY: caskstyle

tap:
    brew tap
.PHONY: tap
