# ansible-roles
Reusable Ansible roles

[![CI](https://github.com/mucsi96/ansible-roles/actions/workflows/build.yml/badge.svg)](https://github.com/mucsi96/ansible-roles/actions/workflows/build.yml)

## Create box

```bash
vagrant up
```

## Run Ansible playbooks

```bash
ap playbooks/enable_root_login.yaml playbooks/new-ssh-user.yaml playbooks/ssh-hardening.yaml playbooks/update-packages.yaml playbooks/deploy-cluster.yaml
```

## Destroy the box

```bash
vagrant destroy
./clean.sh
```

## Create Cloudflare Tunnel

[More details](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/local/#set-up-a-tunnel-locally-cli-setup)

1. Authenticate cloudflared `ct login`
2. Create a tunnel and give it a name `ct create ansible-roles-demo`
3. Confirm that the tunnel has been successfully `ct list`
4. Reveal credentials `cat ~/.cloudflared/*.json`
5. Add credentials to vault
6. Start routing traffic `ct route dns ansible-roles-demo <hostname>`
7. Test `curl <hostname>`
