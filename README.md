# github-actions-development-lifecycle-k8s-201

- Make sure to create service accounts for both dev and prod projets (namespaces) on OpenShift
  The service account tokens are then stored on github > secrets

- Create Git Tag from CLI
```
git tag -a v0.2 -m "tag v0.2"
git push origin v0.2

```