#!/bin/bash
rm -rf .ssh .vagrant .kube
rm -rf /home/vscode/.ssh/
cloudflared tunnel delete -f ansible-roles