import commands

def get_node_num():
    namespace = []
    pod_namespaces = []
    status, output = commands.getstatusoutput("kubectl get namespace")
    if status == 0:
        for line in output.split("\n"):
            if line.startswith("NAME"):
                continue
            namespace.append(line.split()[0])
    else:
        print("get namespace error")
        return None
    
    sts, out = commands.getstatusoutput("kubectl get pods --all-namespaces")
    if sts == 0:
        for line in out.split("\n"):
            if line.startswith("NAMESPACE"):
                continue
            pod_namespaces.append(line.split()[0])
    else:
        print("get pod error")
        return None
    
def get_pod_num():
    nodes = []
    node_pod = []
    status, output = commands.getstatusoutput("kubectl get nodes")
    if status == 0:
        for line in output.split("\n"):
            if line.startswith("NAME"):
                continue
            nodes.append(line.split()[0])
    else:
        print("get nodes error")
        return None
    
    sts,outp = commands.getstatusoutput("kubectl get pod -A -o wide")
    if sts == 0:
        for line in outp.split("\n"):
            if line.startswith("NAMESPACE"):
                continue
            node_pod.append(line.split()[7])
    else:
        print("get pod error")
        return None