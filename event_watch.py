#获取集群上最近发生的事件

from kubernetes import client, config, watch

def get_event():
    
    config.load_kube_config()

    v1 = client.CoreV1Api()
    #事件选取最近的10个
    count = 10
    w = watch.Watch()
    print("namespace stream:")
    print("--------------------------------------------------------------------------")
    
    #监听事件为4秒
    for event in w.stream(v1.list_namespace, timeout_seconds=4):
        print("Event: %s %s" % (event['type'], event['object'].metadata.name))
        count -= 1
        if not count:
            w.stop()
            
    print("\npod stream:")
    print("--------------------------------------------------------------------------")
    
    for event in w.stream(v1.list_pod_for_all_namespaces, timeout_seconds=10):
        print("Event: %s %s %s" % (
            event['type'],
            event['object'].kind,
            event['object'].metadata.name)
        )
        count -= 1
        if not count:
            w.stop()
            
    print("\n")