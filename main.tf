terraform {
  required_providers {
    azurerm = {
        source = "hashicorp/azurerm"
        version = "~> 3.0.2"
    }
  }

  required_version = ">= 1.0.0"
}

provider "azurerm" {
  features {}
  skip_provider_registration = true
}

resource "azurerm_resource_group" "rg-asj" {
  name = "rg-asj"
  location = var.location
}

resource "azurerm_service_plan" "sp-asj" {
  name = "dhbw"
  resource_group_name = azurerm_resource_group.rg-asj.name
  location = azurerm_resource_group.rg-asj.location
  sku_name = "F1"
  os_type = "Linux"
}

resource "azurerm_linux_web_app" "app-asj" {
  name = "saj"
  resource_group_name = azurerm_resource_group.rg-asj.name
  location = azurerm_resource_group.rg-asj.location
  service_plan_id = azurerm_service_plan.sp-asj.id

  site_config {
    always_on = false

    application_stack {
      docker_image = "jannikspringer/devops"
      docker_image_tag = "latest"
    }
  }

  app_settings = {
    "WEBSITES_PORT" = "5000"
  }
}