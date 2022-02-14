# github-actions-development-lifecycle-k8s-201

### Prerequisites

- Login to OpenShift Console and grab the login credentials to login from CLI
- Login from CLI and create 2 namespaces/projects
  - `ksingh-dev`
  - `ksingh-prod`
- Navigate to Github > Repository > Settings > Secrets > Actions
- Set the values for the following GitHub Secrets
```
OPENSHIFT_SERVER_URL = https://api.s690b6hi.centralindia.aroapp.io:6443

OPENSHIFT_DEV_NAMESPACE = ksingh-dev
OPENSHIFT-DEV_TOKEN = sha256~_x1dCr4kLg5PGIHbG7WyUPM4OgpiogsEXXXXXcxxxxx

OPENSHIFT_PROD_NAMESPACE = ksingh-prod
OPENSHIFT_PROD_TOKEN = sha256~_x1dCr4kLg5PGIHbG7WyUPM4OgpiogsEXXXXXcxxxxx

DOCKER_USERNAME = username
DOCKER_PASSWORD = password

QUAY_PULL_SECRET = pull_secret
```

> Note: You can also create service accounts for both dev and prod projets (namespaces) on OpenShift, and store the secrets in github > secrets

### Triggering the build and deployment using GHA

#### 1. Trigger GHA when PR is created
- Make changes to the app as you like
- git commit and push
```
git add .
git commit -am "updates to the app"
git push origin development
```
- Create a PR
- Navigate to Actions and monitor the build/deploy

#### 2. Trigger GHA when PR is merged
- Merge the PR
- Navigate to Actions and monitor the build/deploy

#### 3. Trigger GA when TAG is created

- Create Git Tag from CLI
```
git tag -a v0.2 -m "tag v0.2"
git push origin v0.2

```

#### 4. Trigger GHA when Release is created
- Navigate to GitHub Repository
- Click on the created TAG
- Click on Actions > Create Release
- Navigate to Actions and monitor the build/deploy