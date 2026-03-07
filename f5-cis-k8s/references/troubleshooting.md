# CIS Troubleshooting Reference

This document covers common issues and troubleshooting steps for F5 CIS.

---

## Quick Diagnostic Commands

```bash
# Check CIS pod status
kubectl --namespace=kube-system get pods -l app=cis-ctlr-deployment

# Check CIS logs (last 100 lines)
kubectl --namespace=kube-system logs deployment/<cis-deployment> --tail=100

# Follow CIS logs in real-time
kubectl --namespace=kube-system logs -f deployment/<cis-deployment>

# Check CRD objects across all namespaces
kubectl get vs,ts,externaldns -A

# Describe a specific CRD object
kubectl -n <namespace> describe vs <name>

# Check F5 CRDs are installed
kubectl get crd | grep f5

# Check CIS deployment details
kubectl --namespace=kube-system describe deployment <cis-deployment>

# Check events
kubectl --namespace=kube-system get events --sort-by=.lastTimestamp | tail -20
```

---

## Common Issues

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| CIS pod `CrashLoopBackOff` | Wrong BIG-IP credentials or unreachable IP | Check secret values; verify logs for auth errors; confirm BIG-IP IP is reachable from cluster nodes |
| CIS pod running but no VS on BIG-IP | CRD label mismatch | Ensure CR has label `f5cr: "true"`. Check `--custom-resource-mode=true` is set |
| CIS logs: `partition not found` | Partition does not exist on BIG-IP | Create the partition on BIG-IP first, or change `--bigip-partition` |
| VIP not reachable from client | Missing VXLAN tunnel, route, or self-IP on BIG-IP | Verify BIG-IP has: VXLAN tunnel with self-IP in pod CIDR, route to pod CIDR via tunnel |
| Pool members show 0 active | CIS cannot reach pod IPs (Cluster mode) | Check VXLAN tunnel is UP on BIG-IP; verify `--flannel-name` matches the actual tunnel name; check Cilium VTEP config |
| `No resources found` when getting CRDs | CRDs not installed | Install CRDs — see `references/cis-install-steps.md` Step 0 |
| CIS logs: `AS3 response 422` | Invalid AS3 declaration | Enable `--log-as3-response=true` and `--log-level=DEBUG` to see full AS3 error |
| Multiple CIS pods competing | Replicas > 1 | CIS deployment MUST have `replicas: 1` — do NOT increase |
| CIS logs: `connection refused` | BIG-IP management IP unreachable or wrong port | Verify `--bigip-url` value; check network connectivity from cluster to BIG-IP mgmt |
| CIS logs: `x509: certificate signed by unknown authority` | TLS verification failing | Add `--insecure` flag to skip TLS cert verification |
| CRD applied but CIS ignores it | Missing label or wrong namespace | Check `f5cr: "true"` label; check `--namespace` or `--namespace-label` CIS flags |

---

## Troubleshooting Workflow

1. **Check CIS pod status**
   ```bash
   kubectl --namespace=kube-system get pods -l app=cis-ctlr-deployment
   ```
   - `Running` = CIS is up, check logs for errors
   - `CrashLoopBackOff` = startup failure, check logs for root cause
   - `Pending` = scheduling issue, check events and node resources

2. **Check CIS logs for errors**
   ```bash
   kubectl --namespace=kube-system logs deployment/<cis-deployment> --tail=100
   ```
   - Auth errors → fix credentials in secret
   - Connection errors → fix BIG-IP URL
   - Partition errors → create partition on BIG-IP

3. **Verify CRD objects are created correctly**
   ```bash
   kubectl get vs,ts -A
   kubectl -n <namespace> describe vs <name>
   ```
   - Check `f5cr: "true"` label is present
   - Check service names and ports match actual Services

4. **Verify underlying Services and Pods**
   ```bash
   kubectl get pods,svc -n <namespace>
   kubectl get endpoints -n <namespace>
   ```
   - Pods must be Running
   - Endpoints must exist and have addresses

5. **Enable debug logging if needed**
   Edit the CIS deployment to add:
   ```
   --log-level=DEBUG
   --log-as3-response=true
   ```
   Then restart:
   ```bash
   kubectl --namespace=kube-system rollout restart deployment/<cis-deployment>
   ```

6. **Test connectivity**
   ```bash
   curl -vvv http://<VIP>/ -H "Host: <hostname>"
   ```
   If no connectivity from the Agent, show the curl command to the user.
