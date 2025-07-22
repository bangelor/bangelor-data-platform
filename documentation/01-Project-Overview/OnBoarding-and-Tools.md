# OnBoarding

> This page described the onboarding of new team members.

##  Step 1 - NDA

Every Team member who works with the internal data platform has to sign the isolutions NDA.

The NDA is Managed by HR. If a new member is joining, should be contacted in order to request a NDA to be signed.

## Step 2 - Access Rights and Roles

| Name                  | Description                     | Link                                                                 |
|:----------------------|:--------------------------------|:---------------------------------------------------------------------|
| Azure DevOps          | Code Repository| [Project isolutions.BI](https://dev.azure.com/is-prod/isolutions.BI) |
| Power BI              | Reporting| Pending Workspace |
| Power BI (Fabric Administrator)                         | Reporting Adm.| Pending Workspace|
| Azure Resource Group | Access to **d**,**t**, and **p** resources |  [Resource groups under "rg-bi"](https://portal.azure.com/#browse/resourcegroups)


### Step 3 - Azure DevOps

Every [DevTeam member](https://dev.azure.com/is-prod/isolutions.BI/_git/isolutions.BI?path=/documentation/01%20Project%20Overview/Team.md&version=GBmain&_a=preview&anchor=dev-team) should be **project administrator**.

| Name                  | Role                  |
|:----------------------|:----------------------|
| C      | Project Administrator |
| G    | Project Administrator | 
| G        | Project Administrator | 
| T         | Project Administrator | 

The right can be set [here](https://dev.azure.com/is-prod/isolutions.BI/_settings/projectOverview)

![image.png](/.attachments/image-2a8f5edb-ede6-483f-9a12-45ca78f2be2f.png)

### Step 4 - Azure Entra ID Groups and Resource Groups
The whole solution is deployed within Azure, in 8 different resource groups (2 for each stage), eg:
| Name                  | Description                       | Link                                                                 |
|:----------------------|:----------------------------------|:---------------------------------------------------------------------|
|isol-d1-rg-bi-main     | Resource Group that hosts and stores the development environment              | [Resource Group](https://portal.azure.com/#@isolutionsch.onmicrosoft.com/resource/subscriptions/68bb1548-aae7-430e-89be-635eb8d3ae2c/resourceGroups/isol-d1-rg-bi-main/overview) |
|isol-d1-rg-bi-iac | Resource Group that stores the Terraform state for our development environment| [Resource Group](https) |
| ra-businessintelligence-d1-admin| Contributor Role| [Request the following role through ticket](https://7): 
| rg-powerbi-downloadreports | Engineer Role| [Request the following role through ticket](https://is)


### _Step 5 - Current Platform_
As we are currently migrating from the current data platform, to this project, we would need the following accesses and rights to work during the migration phase:
| Name / Acc. Info.               | Description                       | Link                                                                 |
|:----------------------|:----------------------------------|:---------------------------------------------------------------------|
|[isol-d1-rg-businessintelligence-core](https://portal.azure.com)  | Resource Group that hosts and stores the current development environment              | [Request the following access through ticket](http7)|
| ra-businessintelligence-d1-admin | Member | [Request the following role through ticket](https:/): 
| sa-datagateway@isolutions.ch| Service Account | [Request the following account access through ticket](https:/): 
| Fabric Tenant Admin Acc. Creation| Service Account | [Request to be created through ticket](https:): 
| [Service Now](https:/)| Service Now Access| [Request the following access through ticket](https:7): 
| [iSolutions Bi Reporting Sharepoint Folder](https:/): 

