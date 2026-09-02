---
name: security-hardening
description: Aplica hardening de segurança em clusters AKS, configura RBAC, network policies, PodSecurityPolicies e integração com Key Vault para proteger ambientes Kubernetes de threats e vulnerabilidades.
version: 1.0.0
tags: [security, aks, rbac, network-policies, key-vault, compliance]
---
# Security Hardening

## Purpose

Aplica hardening de segurança em clusters AKS e ambientes Kubernetes, configurando RBAC, network policies, PodSecurityPolicies, e integração com Key Vault para proteger contra threats e vulnerabilidades.

## When to Use

- Task envelope INPUT contém objective de configuração de segurança em clusters AKS/cKubernetes
- Revisão de segurança pós-deploy requer auditoria de RBAC e rede
- Preparação para certificações (SOC2, ISO27001, PCI-DSS)
- Configuração de secrets management e segredo rotation

## When NOT to Use

- Tarefa envolve apenas deploy de aplicação (usar `agentos-build`)
- Configuração de apenas application-level secrets (usar `resource-provisioning`)
- Otimização de performance (usar `rollout-strategies`)

## Procedure

### 1. RBAC Hardening

```bash
# Verificar RBAC cluster atual
az aks show -n <cluster> -g <rg> --query addons.profile.rbac

# Desativar RBAC legacy se necessário
az aks update -n <cluster> -g <rg> --disable-legacy-rbac

# Aplicar RBAC principles
- Principle of least privilege para service accounts
- Use Azure AD integration ao invés de kubelet credentials
- Review ClusterRoleBinding para concessão excessiva

# Aplicar RBAC via Kubernetes manifests
cat <<EOF | kubectl apply -f -
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: restricted-admin
rules:
- apiGroups: [""]
  resources: ["pods", "services", "configmaps"]
  verbs: ["get", "list", "watch"]
- apiGroups: ["apps"]
  resources: ["deployments", "replicasets"]
  verbs: ["get", "list", "watch"]
EOF
```

### 2. Network Policies

```bash
# Instalar network policies addon
az aks enable-network-policy -n <cluster> -g <rg>

# Aplicar NetworkPolicy para isolamento de workloads
cat <<EOF | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all
spec:
  podSelector: {}
  policyTypes: ["Ingress", "Egress"]
  ingress: []
  egress:
  - to:
    - podSelector: {}
    ports:
    - protocol: TCP
      port: 5978
EOF
```

### 3. Key Vault Integration

```bash
# Criar Key Vault para secrets
az keyvault create -n <kv-name> -g <rg> -l <location>

# Integrar com AKS
az aks enable-secret-rotation -n <cluster> -g <rg> --vault-name <kv-name>

# Acessar secrets via CSI driver
# Secrets ficam disponíveis em /etc/keys/... dentro do pod
```

### 4. Pod Security Standards

```bash
# Aplicar PSP legacy (se ainda for usado)
kubectl apply -f https://raw.githubusercontent.com/divergentist/psp_adapter/master/psp.yaml

# Migration para OPA Gatekeeper
cat <<EOF | kubectl apply -f -
apiVersion: apps.openmcd.io/v1
kind: ConstraintTemplate
metadata:
  name: kubernetes-critical-pods
spec: ...
EOF

# Aplicar constraint
kubectl apply -f -
```

## Validation

- Verificar `kubectl get clusterrolebinding` - todos os bindings têm service accounts associadas
- Confirmar que `networkpolicies` estão ativas: `kubectl get networkpolicies --all-namespaces`
- Validar que `podsecurity` standards são atendidas via `kubectl get pods`
- Cross-check com `memory/knowledge` — promover patterns de security se recorrentes
- Executar `kube-score` ou `kube-linter` para validação automatada

## Failure Modes

- **RBAC misconfiguration**: Service accounts com permissões excessivas; recomenda-se principle of least privilege
- **NetworkPolicy bloqueio**: Workloads não conseguem se comunicar; recomenda-se revisar NetworkPolicy rules
- **Key Vault integration failure**: Secrets não são injetados; recomenda-se verificar CSI driver e permissões
- **PodSecurityPolicy deprecated**: PSP será removido em versões futuras do Kubernetes; migre para OPA Gatekeeper

## Known Limitations

- PSP (Pod Security Policy) está em depreciação nas versões recentes do Kubernetes (1.25+)
- Azure AD integration requer Azure AD Tenant ID configurado corretamente
- Network policies não funcionam no modo Host Network
- Key Vault CSI driver requer versão Kubernetes 1.19+

## Examples

### Exemplo 1: Hardening básico de cluster AKS

```
Input: cluster_name="aks-prod", resource_group="rg-aks-prod"
Output: security_report com RBAC status, NetworkPolicy status, Key Vault integration
```

### Exemplo 2: Migração de PSP para OPA Gatekeeper

```
Input: cluster_name="aks-prod", resource_group="rg-aks-prod"
Output: gatekeeper_constraint aplicado, PSP removido
```

## Improvement Criteria

- **Nova skill proposta**: Quando pattern de security hardening detectado em 4+ tasks
- **Promoção para rule**: Quando configuração de security hardening sistêmica (ex: default RBAC profile)
- **Memory promotion**: Quando aprendizado relevante para arquitetura de segurança

## Changelog

- **1.0.0**: Versão inicial