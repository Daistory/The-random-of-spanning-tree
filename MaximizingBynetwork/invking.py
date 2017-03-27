# --*coding:utf-8*--
import copy

import gc

import method


def getResultByAllWay(graph, amt_vaccination, relative_path, total):
    """
    :param graph: 无向图
    :param amt_vaccination: 需要隔离点的总数
    :param relative_path: 需要存储的相对位置
    :param total: 原来网络的大小
    :return: none
    """
    try:
        new_graph = copy.deepcopy(graph)
        vaccination_list = method.getDegreePoint(new_graph, amt_vaccination)
        method.saveData(vaccination_list, relative_path + "degreePoint" + ".txt")
        method.saveData(method.getInfluence(new_graph, vaccination_list), relative_path + "degreePriority" + ".txt")
        del new_graph
        gc.collect()
    except Exception, e:
        print "error in the way named getDegree"
        print Exception, ":", e

    try:
        new_graph = copy.deepcopy(graph)
        vaccination_list = method.getCenPoint(new_graph, amt_vaccination)
        method.saveData(vaccination_list, relative_path + "centralityPoint" + ".txt")
        method.saveData(method.getInfluence(new_graph, vaccination_list), relative_path + "centralityPriority" + ".txt")
        del new_graph
        gc.collect()
    except Exception, e:
        print "error in the way named getCentrality"
        print Exception, ":", e

    try:
        new_graph = copy.deepcopy(graph)
        vaccination_list = method.getRandNeiPoint(new_graph, amt_vaccination, total)
        method.saveData(vaccination_list, relative_path + "randNeiPoint" + "txt")
        method.saveData(method.getInfluence(new_graph, vaccination_list), relative_path + "randNeiPriority" + ".txt")
        del new_graph
        gc.collect()
    except Exception, e:
        print "error in the way named getRandNei"
        print Exception, ":", e

    try:
        new_graph = copy.deepcopy(graph)
        vaccination_list = method.randWalk(new_graph, amt_vaccination, total)
        method.saveData(vaccination_list, relative_path + "randWalkPoint" + ".txt")
        method.saveData(method.getInfluence(new_graph, vaccination_list), relative_path + "randWalkPriority" + ".txt")
        del new_graph
        gc.collect()
    except Exception, e:
        print "error in the way named getRandWalk"
        print Exception, ":", e

    try:
        new_graph = copy.deepcopy(graph)
        vaccination_list = method.getRandSpanTree(new_graph, amt_vaccination, total, 1, 1)
        method.saveData(vaccination_list, relative_path + "similarAntPoint11" + ".txt")
        method.saveData(method.getInfluence(new_graph, vaccination_list),
                        relative_path + "similarAntPriority11" + ".txt")
        del new_graph
        gc.collect()
    except Exception, e:
        print "error in the way named getSimilarAnt"
        print Exception, ":", e

    try:
        new_graph = copy.deepcopy(graph)
        vaccination_list = method.getRandSpanTree(new_graph, amt_vaccination, total, 0, 1)
        method.saveData(vaccination_list, relative_path + "similarAntPoint01" + ".txt")
        method.saveData(method.getInfluence(new_graph, vaccination_list),
                        relative_path + "similarAntPriority01" + ".txt")
        del new_graph
        gc.collect()
    except Exception, e:
        print "error in the way named getSimilarAnt"
        print Exception, ":", e

    try:
        new_graph = copy.deepcopy(graph)
        vaccination_list = method.getPath(relative_path + "similarAntPoint.txt")
        method.saveData(method.getInfo(new_graph, vaccination_list), relative_path + "info.txt")
        del vaccination_list
        gc.collect()
    except Exception, e:
        print "error in the way named getInfo"
        print Exception, ":", e
    del graph, amt_vaccination,
    gc.collect()
