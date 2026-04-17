provider "azurerm" {
  version = "=2.31.0"

  features {}

  subscription_id = var.subscription_id
  client_id       = var.client_id
  client_secret   = var.client_secret
  tenant_id       = var.tenant_id
}

terraform {
  backend "azurerm" {
    storage_account_name = "dbasterraformstate"
    container_name       = "terraformstate"
    key                  = "terraformsqlmi.tfstate"
    access_key           = "vd+3dVxTa4SdcV9eWk/qSJoI+DLgPaTVbdqW+Lokr//uebWkx6WBZx+SHS5ngkClrRDQDvkumH708zQQaIn5+A=="
  }
}
