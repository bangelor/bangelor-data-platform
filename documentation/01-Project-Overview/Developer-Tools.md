# Developer Tools

> This page describes the Tools we use for development and their configuration.

##  Visual Studio Code

We use VS Code with the following Extensions:

| Name               | Description                                                     |
|:-------------------|:----------------------------------------------------------------|
| markdownlint       | Ensures consistent styling in md                                |
| Terraform          | Intellisense for Terraform                                      |
| drawio             | Designing Architecture and workflows                            |
| Data Wrangler      | Open and edit .parquet, .csv files through VS Code              |

## Terraform
We use Terraform to deploy Infrastructure as a code, [using this YAML release Pipeline.](https://dev.azure.com/is-prod/isolutions.BI/_build?definitionId=1075)

Every stage contains a resource group and storage account to store our Terraform state, as the following example:

<center>

![image.png](/.attachments/image-0b4ccf74-5e08-4699-8c35-c9e2f0ad41e5.png)

</center>

## drawio
Our architecture diagrams, workflows and drawing are created and maintained through drawio.
    To work, read and edit it, you can use the drawio extension found at Visual Studio Code Extension Manager.
