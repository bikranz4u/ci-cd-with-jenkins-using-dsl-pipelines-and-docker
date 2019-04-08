FROM ubuntu:18.04
ARG USERNAME=jenkins

RUN useradd -ms /bin/bash ${USERNAME} && usermod -aG sudo ${USERNAME} \
    && echo '${USERNAME} ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers \
    usermod -aG docker ${USERNAME}

RUN apt-get update && \
    apt-get install openssh* nginx nodejs npm apt-utils -y && \
    /lib/systemd/systemd-sysv-install enable nginx && \
    /etc/init.d/nginx start

# Define default command.
#CMD ["nginx"]

# Expose ports.
EXPOSE 80
EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]
#ADD index.html /var/www.html/custom-index.html
# https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-18-04
