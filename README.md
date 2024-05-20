# Virtual Machine Placement in Energy Aware Load Balancer Using Fog Classifier

This repository contains a Python implementation of an algorithm for virtual machine (VM) placement in an energy-aware load balancer, based on the research article "Virtual machine placement in energy aware load balancer using fog classifier" by S. Selvaganapathy and M. Chinnadurai.

## Description

The algorithm aims to balance the load across hosts in a data center by intelligently placing virtual machines (VMs) in a way that minimizes energy consumption while avoiding over-utilization of any host. The key steps involve:

1. Categorizing hosts as under-utilized or over-utilized based on an upper utilization threshold.
2. Calculating the total workload of the data center.
3. Iteratively allocating VMs to hosts, prioritizing those that result in the least increase in power consumption.
4. Generating a migration map showing which VMs are allocated to which hosts.


## Article Information
- Title: Virtual machine placement in energy aware load balancer using fog classifier
- Authors: S. Selvaganapathy, M. Chinnadurai
- DOI: https://doi.org/10.1186/s13677-023-00559-8
License
This project is licensed under the MIT License.

## Acknowledgements
This implementation is based on the research conducted by S. Selvaganapathy and M. Chinnadurai as described in their paper.
