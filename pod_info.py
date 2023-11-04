# 打印所有的pod信息
# 打印pod的名称， 命名空间，IP地址和运行在哪个节点上

from kubernetes import client, config

def get_pod_info():
    
    config.load_kube_config()

    v1 = client.CoreV1Api()
    
    print("{:<35} {:<15} {:<20} {:<15}".format("NAME", "NAMESPACE", "IP ADDRESS", "NODE"))
    print("--------------------------------------------------------------------------------")
    
    ret = v1.list_pod_for_all_namespaces(watch=False)
    
    for i in ret.items:
        node_name = i.spec.node_name if i.spec.node_name is not None else "N/A"
        pod_ip = i.status.pod_ip if i.status.pod_ip is not None else "None"
        print("{:<35} {:<15} {:<20} {:<15}\n".format(i.metadata.name, i.metadata.namespace, pod_ip, node_name))