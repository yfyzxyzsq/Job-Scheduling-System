# 打印集群的所有节点
# 每个节点显示其名称，状态，版本，IP地址和所占用的内存

from kubernetes import config, dynamic
from kubernetes.client import api_client


def get_node_info():
    
    # 创建一个动态客户端
    client = dynamic.DynamicClient(
        api_client.ApiClient(configuration=config.load_kube_config())
    )

    # 获取节点对应的api
    api = client.resources.get(api_version="v1", kind="Node")

    # 显示节点的信息

    print("%s\t\t%s\t\t%s\t\t%s\t\t%s" % ("NAME", "STATUS", "VERSION", "IP ADDRESS", "MEMORY"))
    print("--------------------------------------------------------------------------------")
    for item in api.get().items:
        node = api.get(name=item.metadata.name)
        print(
            "%s\t\t%s\t\t%s\t\t%s\t\t%.2fGB\n"
            % (
                node.metadata.name,
                node.status.conditions[3]["type"],
                node.status.nodeInfo.kubeProxyVersion,
                node.status.addresses[0]["address"],
                float(node.status.capacity["memory"].replace("Ki", ""))/1024/1024,
            )
        )
def main():
    get_node_info()
    
if __name__ == "__main__":
    main()