#!/bin/bash
set -euo pipefail

echo '==> [Lifecycle: postCreateCommand] Starting Dev Container Post-Create Setup...'

# ------------------------------------------------------
# ------------------------------------------------------

echo "[postCreateCommand]:: Installing Powerlevel10k theme..."
P10K_DIR="${HOME}/powerlevel10k"
P10K_VERSION="35833ea15f14b71dbcebc7e54c104d8d56ca5268"

if [ ! -d "${P10K_DIR}" ] || [ -z "$(ls -A "${P10K_DIR}")" ]; then
    mkdir -p "${P10K_DIR}" && cd "${P10K_DIR}" && sudo chown -R ${USER_UID}:${USER_GID} "${P10K_DIR}"
    
    GIT_LOG=$(git init -q && git remote add origin https://github.com/romkatv/powerlevel10k.git && git fetch -q --depth 1 origin "${P10K_VERSION}" && git reset -q --hard FETCH_HEAD 2>&1)
    
    if [ $? -eq 0 ]; then
        rm -rf .git
        echo "[postCreateCommand]:: Powerlevel10k theme successfully installed to ${P10K_DIR}"
    else
        rm -rf .git
        echo "[postCreateCommand]:: Error: Powerlevel10k theme installation failed at ${P10K_DIR}"
        echo "[postCreateCommand]:: Git error details: ${GIT_LOG}"
    fi
    cd - > /dev/null
else
    echo "[postCreateCommand]:: Directory ${P10K_DIR} already exists and is not empty. Skipping installation."
fi

# ------------------------------------------------------
# 2. CLAUDE CODE PLUGIN (magbridge-ai)
# ------------------------------------------------------
echo "[postCreateCommand]:: Setting up magbridge-ai Claude plugin..."
PLUGIN_REMOTE="https://github.com/mag-bros/magbridge-ai"
PLUGIN_PATH=".claude"

if [ -d "${PLUGIN_PATH}/.git" ]; then
    echo "[postCreateCommand]:: magbridge-ai found, syncing to latest..."
    git -C "${PLUGIN_PATH}" pull origin master 2>/dev/null || true
else
    echo "[postCreateCommand]:: Cloning magbridge-ai plugin..."
    git clone "${PLUGIN_REMOTE}" "${PLUGIN_PATH}"
    git -C "${PLUGIN_PATH}" checkout master
fi

PLUGIN_SHA=$(git -C "${PLUGIN_PATH}" rev-parse --short HEAD 2>/dev/null || echo "unknown")
echo "[postCreateCommand]:: magbridge-ai ready @ ${PLUGIN_SHA}."

# ------------------------------------------------------
# 3. GITHUB CLI AUTH
# ------------------------------------------------------
echo "[postCreateCommand]:: Checking GitHub CLI auth..."
gh auth status 2>/dev/null \
    && echo "[postCreateCommand]:: GitHub CLI authenticated." \
    || echo "[postCreateCommand]:: GitHub CLI not authenticated — ensure GH_TOKEN (fine-grained PAT) is set in .env"

echo "[postCreateCommand]:: Exit"
