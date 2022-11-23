# ansible-roles
Reusable Ansible roles

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