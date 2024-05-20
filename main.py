def calculate_total_workload(host_list):
    # Calculate the total workload of the data center
    total_workload = sum(host['utilization'] for host in host_list)
    return total_workload  # Total utilization of all hosts

def sort_hosts_by_utilization(host_list):
    # Sort hosts by utilization in descending order
    return sorted(host_list, key=lambda x: x['utilization'], reverse=True)

def host_load_balancer_with_energy_aware_placement(host_list, vm_list, upper_threshold):
    host_list_under_utilized = []  # List of underutilized hosts
    host_list_over_utilized = []  # List of overutilized hosts

    # Categorize hosts into underutilized and overutilized
    for host in host_list:
        if not host['switched_off']:  # If the host is not switched off
            if host['utilization'] < upper_threshold:
                host_list_under_utilized.append(host)  # Add to underutilized hosts list
            else:
                host_list_over_utilized.append(host)  # Add to overutilized hosts list
    
    total_workload = calculate_total_workload(host_list)  # Calculate the total workload of the data center
    hmax_total = total_workload / upper_threshold  # Calculate the maximum number of hosts

    # Sort overutilized hosts
    host_list_over_utilized = sort_hosts_by_utilization(host_list_over_utilized)

    # Repeat allocation of VMs until hmax_total reaches zero
    while hmax_total > 0:
        for vm in vm_list[:]:  # For each virtual machine
            allocate_host = None
            min_power = float('inf')  # Initial value for minimum power

            # Search for the host with the least power consumption and allocate it
            for host in host_list:
                if host['utilization'] + vm['utilization'] <= upper_threshold:
                    power_consumption = host['utilization'] + vm['utilization']
                    if power_consumption < min_power:
                        min_power = power_consumption
                        allocate_host = host
            
            # If a suitable host is found, perform the allocation
            if allocate_host:
                allocate_host['utilization'] += vm['utilization']  # Update host utilization
                if 'vms' not in allocate_host:
                    allocate_host['vms'] = []
                allocate_host['vms'].append(vm['id'])  # Add the virtual machine to the host
                vm_list.remove(vm)  # Remove the virtual machine from the list

        hmax_total -= 1  # Decrease the maximum number of hosts
    
    # Create a migration map of virtual machines to hosts
    migration_map = {}
    for host in host_list:
        migration_map[host['id']] = host.get('vms', [])

    return migration_map  # Return the migration map

# Example to test the algorithm
hosts = [
    {'id': 1, 'utilization': 70, 'switched_off': False},
    {'id': 2, 'utilization': 20, 'switched_off': False},
    {'id': 3, 'utilization': 90, 'switched_off': True},
    {'id': 4, 'utilization': 30, 'switched_off': False}
]

vms = [
    {'id': 1, 'utilization': 10},
    {'id': 2, 'utilization': 40},
    {'id': 3, 'utilization': 30}
]

upper_threshold = 80  # Upper utilization threshold

# Execute the algorithm
migration_map = host_load_balancer_with_energy_aware_placement(hosts, vms, upper_threshold)

# Print the migration map
print("Migration Map: ")
for host_id, vm_ids in migration_map.items():
    print(f"Host {host_id}: VMs {vm_ids}")
