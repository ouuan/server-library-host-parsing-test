FROM archlinux

RUN echo 'Server = https://mirrors.tuna.tsinghua.edu.cn/archlinux/$repo/os/$arch' > /etc/pacman.d/mirrorlist
RUN pacman -Syu --noconfirm
RUN pacman -S --noconfirm pm2 nodejs python python-django rust go ruby php
RUN gem install sinatra webrick

COPY servers servers
RUN servers/start.sh

COPY test.py .
CMD ["bash", "-c", "pm2 resurrect && sleep 5 && servers/versions.sh > /results/server-versions.txt && python test.py > /results/test-servers-result.txt"]
