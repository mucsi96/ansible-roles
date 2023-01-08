# See here for image contents: https://github.com/microsoft/vscode-dev-containers/blob/v0.202.3/containers/python-3/.devcontainer/base.Dockerfile
# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
ARG VARIANT=3-bullseye
FROM mcr.microsoft.com/devcontainers/python:0-${VARIANT}

ARG USERNAME=vscode
ARG USER_HOME=/home/${USERNAME}
ARG WORKSPACE_HOME=/workspaces/ansible-roles

# [Optional] Allow the vscode user to pip install globally w/o sudo
ENV PIP_TARGET=/usr/local/pip-global
ENV PYTHONPATH=${PIP_TARGET}:${PYTHONPATH}
ENV PATH=${PIP_TARGET}/bin:${PATH}
RUN if ! cat /etc/group | grep -e "^pip-global:" > /dev/null 2>&1; then groupadd -r pip-global; fi \
    && usermod -a -G pip-global vscode \
    && umask 0002 && mkdir -p ${PIP_TARGET} \
    && chown :pip-global ${PIP_TARGET} \
    && ( [ ! -f "/etc/profile.d/00-restore-env.sh" ] || sed -i -e "s/export PATH=/export PATH=\/usr\/local\/pip-global:/" /etc/profile.d/00-restore-env.sh )

COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends sshpass

# Apt cleanup
RUN apt-get autoremove -y; \
    apt-get clean -y; \
    rm -rf /var/lib/apt/lists/*

# Install kubectl
RUN curl -sSL -o /usr/local/bin/kubectl https://dl.k8s.io/release/v1.25.3/bin/linux/amd64/kubectl \
    && chmod 0755 /usr/local/bin/kubectl

# Install Helm
RUN curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 \
    && chmod 700 get_helm.sh \
    && ./get_helm.sh --version v3.10.3

# Install cloudflared
RUN wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb && dpkg -i cloudflared-linux-amd64.deb

# Install Java
ARG JAVA_VERSION=11.0.17-tem
RUN su ${USERNAME} --command \
    'curl -s "https://get.sdkman.io" | bash \
    && source "${HOME}/.sdkman/bin/sdkman-init.sh" \
    && sdk install java "${JAVA_VERSION}" \
    && sdk flush archives \
    && sdk flush temp'

ENV ANSIBLE_CONFIG=${WORKSPACE_HOME}/ansible.cfg
ENV KUBECONFIG=${WORKSPACE_HOME}/.kube/config
COPY .bashrc ${USER_HOME}