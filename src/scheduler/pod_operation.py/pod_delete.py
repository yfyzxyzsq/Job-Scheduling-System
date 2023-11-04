#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 参数说明：
# config_path：k8s集群token文件路径
# namespace：k8s namespace
# name：pod名称
# grace_period_seconds：优雅退出时间，0s就是立即删除
def delete_pod(config_path, namespace, name, grace_period_seconds=None):
    # load k8s集群token信息
    config.load_kube_config(config_path)
    v1 = client.CoreV1Api()

    # 删除pod
    ret = v1.delete_namespaced_pod(namespace=namespace, name=pod_name,
                                    grace_period_seconds=grace_period_seconds)
    return
