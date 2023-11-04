# 获取集群的所有节点
# 打印每个节点的标签

from kubernetes import client, config


def get_node_labels():
    
    config.load_kube_config()

    api_instance = client.CoreV1Api()

    # Listing the cluster nodes
    node_list = api_instance.list_node()

    print("{:<40} {}".format("NAME", "LABELS"))
    print("--------------------------------------------------------------------------")
    # 打印每个node的标签
    for node in node_list.items:
        #可能没有某些特定的标签
        labels = node.metadata.labels or {}
        print(f"{node.metadata.name:<40}")
        for key, value in labels.items():
            print(f"{'':<40}{key}: {value}")
        print("--------------------------------------------------------------------------")
