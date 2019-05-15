Tez Client 修改：

* ATSHistoryLoggingService 		Tez中log event 类
* org.apache.hadoop.yarn.client.api.impl.TimelineClient 	yarn中负责http通信和发送消息的服务
* org.apache.tez.client.TezClient 
  * TezConfiguration.TEZ_HISTORY_LOGGING_SERVICE_CLASS  配置ATSHistoryLoggingService 
    private static final String atsHistoryLoggingServiceClassName =
      "org.apache.tez.dag.history.logging.ats.ATSHistoryLoggingService";

	  
* TimelineClientImpl 这个是发送数据的入口
* ApplicationHistoryServer.startWebApp()  -> AHSWebApp -> TimelineWebServices postEntities putDomain 这个方法负责接收数据

Rpc参考编写代码  RPCCallBenchmark



ApplicationHistoryClientService  10200 RPC server .. 



ApplicationHistoryServer -> 
	ApplicationHistoryManager historyManager = createApplicationHistoryManager(conf);
    ApplicationHistoryClientService ahsClientService = createApplicationHistoryClientService(historyManager);
	
	
	
proto rpc:
	yarn_service_protos.proto  -> application_history_client.proto