#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#import requests

import urllib,urllib2
import re,os
import time
class RestTest(object):
    def __init__(self):
        '''
        python的魔术方法，类似java的构造函数，该类在实例化的时候会调用这个函数
        '''
        self.__ResPath__='/Users/niuhanyang/Desktop/TestRes/'#测试结果路径
    def Rest(self,method,url,restName,**param):
        '''
        :param method: 请求方法，GET/POST，入参类型是str
        :param url: 请求url地址，入参类型是str
        :param restName: 接口名称，入参，类型是str
        :param param: 请求参数是一个可选参数，例如oper_id=11,会把传入的值都放到一个dict中，如{'oper_id':11}
        :return:如果是登录接口的话，会返回jessionid
        '''
        jsessionStr=r'"jsessionid":"(.*?)"'#正则表达式，抓出jsessionid
        new_jsessionStr = re.compile(jsessionStr)#编译正则
        if method=='GET':
            data = self.UrlParam(param)
            new_url=url+'?'+data#生成新的url
            result = urllib.urlopen(new_url).read()#保存返回结果
            print  restName+'\n'+result
            self.WriteRes(result,restName)#保存测试结果和返回报文
            return ''.join(new_jsessionStr.findall(result))
        if method=='POST':
            data = self.UrlParam(param)#参数转换
            req = urllib2.Request(url,data)#生成一个request对象
            response = urllib2.urlopen(req)#发送request请求
            result = response.read()#保存结果
            print  restName+'\n'+result
            self.WriteRes(result,restName)#保存测试结果和返回报文
            return ''.join(new_jsessionStr.findall(result))#把jsessionid转化成字符串返回，findall方法的返回值是一个list
    def UrlParam(self,param):
        '''
        参数转换，入参是一个dict，把这个list变为xx=xx这样
        示例：
        入参：{'oper_id':11}
        出参：oper_id=11
        '''
        return urllib.urlencode(param)
    def WriteRes(self,result,restName):
        '''
        :param result: 返回报文
        :param restName: 接口名，用来做报文结果的文件名
        :return: 无返回值
        '''
        res= result.find('success')#返回结果是否成功
        fw_flag = open('%sTestRes.txt'%self.__ResPath__,'a')#追加方式打开测试结果文件
        if res>0:
           fw_flag.write('%s : pass\n'%restName)#写入测试结果
        else:
            fw_flag.write('%s : fail\n'%restName)#写入测试结果
        fw_flag.close()
        fw_response = open('%s%s.txt'%(self.__ResPath__,restName),'w')#打开返回报文文件，前面一个%s是路径，后面的%s是以接口名命名的文件名
        fw_response.write(result)#写入返回报文
        fw_response.close()
    def BakRes(self):
        '''
        该函数的作用是用来备份测试结果
        '''
        now_time= time.strftime("%m-%d_%H:%M", time.localtime())
        os.system('cd %s&&mkdir %s&&mv *.txt ./%s'%(self.__ResPath__,now_time,now_time))
    def RmRes(self):
        '''
        清空测试目录下的所有测试结果
        '''
        os.system('cd %s&&rm -rf *'%self.__ResPath__)
if __name__ == '__main__':
    Test = RestTest()#创建一个实例
    session_id = Test.Rest('POST','http://127.0.0.1:8080/nn_web/rest/oper/login','login',login_flag=0,oper_no='HEHH',oper_pwd=1)#调用Rest方法测试登录接口，获取session_id
    Test.Rest('POST','http://127.0.0.1:8080/nn_web/rest/oper/getOperInfo','getOperInfo',jsessionid=session_id)#调用获取工号信息接口，传入登录获取到的seession_id

    getHistoryList = {"page":1,"page_size":15}

re = requests.post("http://api.thecover.cn/getHistoryList?client=iOS&vno=2.0.0.1&deviceid=123&timestamp=123&sign=C271EDBEDB5E77A4597DDC63547CDD1A&data=",data=getHistoryList)

print re.text