# ansible-roles
Reusable Ansible roles

[![CI](https://github.com/mucsi96/ansible-roles/actions/workflows/build.yml/badge.svg)](https://github.com/mucsi96/ansible-roles/actions/workflows/build.yml)

## Create box

```bash
vagrant up
```

## Run Ansible playbooks

```bash
ap playbooks/enable_root_login.yaml playbooks/new_ssh_user.yaml playbooks/ssh_hardening.yaml playbooks/update_packages.yaml playbooks/install_kubernetes.yaml playbooks/deploy_kubernetes_demo.yaml playbooks/deploy_cloudflare_tunnel.yaml
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

## Firewall

Check status
```bash
sudo firewall-cmd --state
```

Start
```bash
sudo systemctl start firewalld
```

Firewalld enable logging

Find and list the actual LogDenie settings
```bash
sudo firewall-cmd --get-log-denied
```

Change the actual LogDenie settings
```bash
sudo firewall-cmd --set-log-denied=all
```

Verify it:
```bash
sudo firewall-cmd --get-log-denied
```

Log all dropped packets
```bash
sudo nano /etc/rsyslog.d/firewalld-droppd.conf
```

Append the following configuration
```bash
:msg,contains,"_DROP" /var/log/firewalld-droppd.log
:msg,contains,"_REJECT" /var/log/firewalld-droppd.log
& stop
```

```bash
sudo systemctl restart rsyslog.service
```

Watch log
```bash
sudo tail -f /var/log/firewalld-droppd.log
```