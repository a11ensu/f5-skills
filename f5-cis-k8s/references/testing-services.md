# Testing Services Reference

This document covers creating, modifying, and deleting test pods and services
for use with F5 CIS.

---

## Available Templates

| Template | Description |
|----------|-------------|
| `templates/10-svc/ns-example.yaml` | Example namespace with `type: crd` label |
| `templates/10-svc/cafe-svc-cluster.yaml` | Cafe demo app (coffee + tea) with ClusterIP services |
| `templates/10-svc/httpbin-svc.yaml` | httpbin HTTP request/response testing service |

---

## Create a Namespace

```bash
kubectl apply -f templates/10-svc/ns-example.yaml
```

Or create a custom namespace:

```bash
kubectl create namespace <namespace>
kubectl label namespace <namespace> type=crd   # optional: for --namespace-label filtering
```

---

## Deploy Test Applications

### Cafe App (coffee + tea)

Deploys two services for testing L7 path-based routing:
- `coffee-svc` (port 80 -> 8080, 2 replicas)
- `tea-svc` (port 80 -> 8080, 1 replica)

```bash
kubectl apply -f templates/10-svc/cafe-svc-cluster.yaml -n <namespace>
```

Verify:

```bash
kubectl get pods,svc -n <namespace>
```

### httpbin

Deploys an HTTP request/response testing service:
- `httpbin` (port 80, 1 replica)

```bash
kubectl apply -f templates/10-svc/httpbin-svc.yaml -n <namespace>
```

---

## Creating Custom Test Services

When the user needs a service not covered by templates, create a Deployment + Service:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: <app-name>
spec:
  replicas: <replica-count>
  selector:
    matchLabels:
      app: <app-name>
  template:
    metadata:
      labels:
        app: <app-name>
    spec:
      containers:
        - name: <app-name>
          image: <image>
          ports:
            - containerPort: <port>
---
apiVersion: v1
kind: Service
metadata:
  name: <app-name>-svc
spec:
  ports:
    - name: http
      port: 80
      targetPort: <port>
  selector:
    app: <app-name>
  type: ClusterIP    # Use ClusterIP for Cluster mode, NodePort for NodePort mode
```

---

## Modifying Existing Services

Common modifications:

```bash
# Scale replicas
kubectl scale deployment <name> --replicas=<count> -n <namespace>

# Change image
kubectl set image deployment/<name> <container>=<new-image> -n <namespace>

# Edit service (change port, type, etc.)
kubectl edit svc <name> -n <namespace>
```

---

## Deleting Test Services

```bash
# Delete specific resources
kubectl delete -f templates/10-svc/cafe-svc-cluster.yaml -n <namespace>
kubectl delete -f templates/10-svc/httpbin-svc.yaml -n <namespace>

# Delete all resources in a namespace
kubectl delete all --all -n <namespace>

# Delete the namespace entirely
kubectl delete namespace <namespace>
```

---

## Testing Connectivity

After a CRD (VirtualServer/TransportServer) is applied, test with `curl`:

```bash
# L7 HTTP test (VirtualServer)
curl http://<VIP>/<path> -H "Host: <hostname>"

# L4 TCP test (TransportServer)
curl -v telnet://<VIP>:<port>

# With verbose output
curl -vvv http://<VIP>/ -H "Host: <hostname>"

# Check HTTP status only
curl -s -o /dev/null -w "%{http_code}" http://<VIP>/ -H "Host: <hostname>"
```

> **Note:** If the Agent has no connectivity to the VIP, show the user the
> curl command to run from a machine that does have connectivity.
