"""An Azure Python Pulumi program"""

import pulumi
from pulumi_azure import core, storage

# Create an Azure Resource Group
resource_group = core.ResourceGroup(
    'rg',
    name='{}-{}-rg'.format(pulumi.get_project(), pulumi.get_stack()),
    location='westeurope'
)

# Create an Azure resource (Storage Account)
storage_account = storage.Account(
    'sa',
    resource_group_name=resource_group.name,
    name='{}{}sa01'.format(pulumi.get_project(), pulumi.get_stack()),
    account_tier='Standard',
    account_replication_type='LRS',
    tags={"Environment": "Dev"}
)

# Export the connection string for the storage account
pulumi.export('connection_string', storage_account.primary_connection_string)
