FROM docker.io/library/python:3.12-slim-bookworm

ENV USERNAME=vscode_server
ENV USER_UID=6666
ENV USER_GID=6666

USER root

# Setup User and Permissions
RUN groupadd --gid ${USER_GID} ${USERNAME} \
    && useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME}

# Install OS Dependencies (Removed 'sudo' for strict AI Isolation)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    vim \
    curl \
    git \
    libxrender1 \
    libxext6 \
    libsm6 \
    libice6 \
    pulseaudio-utils \
    libfontconfig1 \
    iputils-ping \
    netcat-openbsd && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

ENV PROJECT_DIR=/workspaces/mag-bridge

# Claude persistent isolated auth
RUN mkdir -p /commandhistory /home/${USERNAME}/.claude \
    && chown -R ${USERNAME}:${USER_GID} /commandhistory /home/${USERNAME}/.claude

RUN pip install --no-cache-dir uv

# --- Feature flags (1=install, 0=skip) ---
ARG INSTALL_CBM=1
ARG INSTALL_CHROMIUM=1
ARG INSTALL_GO=1
ARG INSTALL_IRON_PROXY=1
ARG INSTALL_LOKI=1
ARG INSTALL_GRAFANA=1

# codebase-memory-mcp v0.6.1 — built from source with UI assets embedded
# UI variant requires Node.js (for graph-ui frontend build) + zlib (C linker).
# Node.js is installed temporarily and removed after the build; the devcontainer
# Node 22 feature installs its own copy later with no conflict.
# The resulting binary is fully static — no GLIBC constraint.
RUN if [ "$INSTALL_CBM" = "1" ]; then \
    apt-get update && \
    apt-get install -y --no-install-recommends zlib1g-dev && \
    curl -fsSL https://deb.nodesource.com/setup_22.x | bash - && \
    apt-get install -y --no-install-recommends nodejs && \
    git clone --depth=1 --branch v0.6.1 \
        https://github.com/DeusData/codebase-memory-mcp.git /tmp/cbm-src && \
    cd /tmp/cbm-src && bash scripts/build.sh --with-ui && \
    install -m 755 build/c/codebase-memory-mcp /usr/local/bin/codebase-memory-mcp && \
    cd / && rm -rf /tmp/cbm-src && \
    apt-get remove -y nodejs npm && apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/* /root/.npm; \
    fi

# Playwright Chromium OS dependencies — sourced from playwright/nativeDeps.ts debian12-x64.
# Browser binary itself is downloaded in updateContentCommand.sh (version tied to requirements-dev.txt).
RUN if [ "$INSTALL_CHROMIUM" = "1" ]; then \
    apt-get update && apt-get install -y --no-install-recommends \
        libasound2 \
        libatk-bridge2.0-0 \
        libatk1.0-0 \
        libatspi2.0-0 \
        libcairo2 \
        libcups2 \
        libdbus-1-3 \
        libdrm2 \
        libgbm1 \
        libglib2.0-0 \
        libnspr4 \
        libnss3 \
        libpango-1.0-0 \
        libx11-6 \
        libxcb1 \
        libxcomposite1 \
        libxdamage1 \
        libxfixes3 \
        libxkbcommon0 \
        libxrandr2 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*; \
    fi

# GitHub CLI
# Arch-agnostic: $(dpkg --print-architecture) resolves arm64/amd64 at build time.
RUN ARCH=$(dpkg --print-architecture) \
    && curl -fsSL "https://github.com/cli/cli/releases/download/v2.92.0/gh_2.92.0_linux_${ARCH}.deb" \
        -o /tmp/gh.deb \
    && dpkg -i /tmp/gh.deb \
    && rm /tmp/gh.deb

# Go toolchain (feature flag)
ARG GO_VERSION=1.24.4
RUN if [ "$INSTALL_GO" = "1" ]; then \
    ARCH=$(dpkg --print-architecture) \
    && curl -fsSL "https://go.dev/dl/go${GO_VERSION}.linux-${ARCH}.tar.gz" -o /tmp/go.tar.gz \
    && tar -C /usr/local -xzf /tmp/go.tar.gz \
    && rm /tmp/go.tar.gz; \
    fi

ENV PATH="/usr/local/go/bin:${PATH}"

# iron-proxy (issue #9) — feature flag; requires INSTALL_GO=1. Build from source, pinned tag.
# v0.41.0 = latest STABLE (validated; spike autoresearch/debug-260603-2125). Latest tag incl.
# prereleases is v0.42.0-rc.7 — bump IRON_PROXY_REF. Arch-native build (macOS-arm64 + WSL2-amd64).
# INERT: binary + CA installed, proxy NOT started, no proxy-env set => a rebuild does not change
# egress. Wiring it on is the human Phase-1 step (.claude/context/iron-proxy-setup.md).
ARG IRON_PROXY_REF=v0.41.0
RUN if [ "$INSTALL_IRON_PROXY" = "1" ]; then \
    git clone --depth 1 --branch "${IRON_PROXY_REF}" https://github.com/ironsh/iron-proxy.git /tmp/iron-proxy-src \
    && cd /tmp/iron-proxy-src \
    && CGO_ENABLED=0 go build -trimpath \
        -ldflags "-s -w -X github.com/ironsh/iron-proxy/internal/version.Version=${IRON_PROXY_REF}" \
        -o /usr/local/bin/iron-proxy ./cmd/iron-proxy \
    && /usr/local/bin/iron-proxy generate-ca -outdir /etc/iron-proxy \
    && chmod 644 /etc/iron-proxy/ca.crt && chmod 600 /etc/iron-proxy/ca.key \
    && chown -R ${USERNAME}:${USER_GID} /etc/iron-proxy \
    && cd / && rm -rf /tmp/iron-proxy-src /root/.cache/go-build; \
    fi

# Loki — feature flag; single static binary from GitHub releases.
ARG LOKI_VERSION=3.7.2
RUN if [ "$INSTALL_LOKI" = "1" ]; then \
    ARCH=$(dpkg --print-architecture) \
    && curl -fsSL "https://github.com/grafana/loki/releases/download/v${LOKI_VERSION}/loki-linux-${ARCH}.zip" \
        -o /tmp/loki.zip \
    && python3 -c "import zipfile; z=zipfile.ZipFile('/tmp/loki.zip'); z.extract('loki-linux-${ARCH}', '/tmp'); z.close()" \
    && install -m 755 "/tmp/loki-linux-${ARCH}" /usr/local/bin/loki \
    && rm /tmp/loki.zip "/tmp/loki-linux-${ARCH}"; \
    fi

# Grafana — feature flag; tarball from dl.grafana.com CDN (no GitHub release assets).
# +security-NN suffix is part of the version string and appears verbatim in the tarball name.
ARG GRAFANA_VERSION=13.0.1+security-01
RUN if [ "$INSTALL_GRAFANA" = "1" ]; then \
    ARCH=$(dpkg --print-architecture) \
    && curl -fsSL "https://dl.grafana.com/oss/release/grafana-${GRAFANA_VERSION}.linux-${ARCH}.tar.gz" \
        -o /tmp/grafana.tar.gz \
    && tar -xzf /tmp/grafana.tar.gz -C /usr/local/ \
    && mv "/usr/local/grafana-${GRAFANA_VERSION}" /usr/local/grafana \
    && rm /tmp/grafana.tar.gz; \
    fi

ENV DEVCONTAINER_DIR="${PROJECT_DIR}/.devcontainer"
ENV SERVICES_DIR="${DEVCONTAINER_DIR}/services"

USER ${USERNAME}