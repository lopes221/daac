from diagrams import Diagram
from diagrams.azure.network import VirtualNetworks
from diagrams.azure.compute import KubernetesServices, ContainerRegistries

with Diagram("Diagram as a Code", show=True):
    aks_lz = KubernetesServices("AKS Platform")
    aks_cr_lz = ContainerRegistries("Container Registry")
    vnet_hub = VirtualNetworks("vnet-hub")
    lz_spoke01 = VirtualNetworks("vnet-spoke-01")
    lz_spoke02 = VirtualNetworks("vnet-spoke-02")
    lz_spoke03 = VirtualNetworks("vnet-spoke-03")
    lz_spoke04 = VirtualNetworks("vnet-spoke-04")
    lz_spoke05 = VirtualNetworks("vnet-spoke-05")
    lz_spoke01 - vnet_hub
    lz_spoke02 - vnet_hub
    lz_spoke03 - vnet_hub
    lz_spoke04 - vnet_hub
    lz_spoke05 - vnet_hub
    aks_lz - vnet_hub
    aks_lz - aks_cr_lz
    aks_cr_lz - aks_lz



