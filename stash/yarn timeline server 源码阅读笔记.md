Tez Client �޸ģ�

* ATSHistoryLoggingService 		Tez��log event ��
* org.apache.hadoop.yarn.client.api.impl.TimelineClient 	yarn�и���httpͨ�źͷ�����Ϣ�ķ���
* org.apache.tez.client.TezClient 
  * TezConfiguration.TEZ_HISTORY_LOGGING_SERVICE_CLASS  ����ATSHistoryLoggingService 
    private static final String atsHistoryLoggingServiceClassName =
      "org.apache.tez.dag.history.logging.ats.ATSHistoryLoggingService";

	  
* TimelineClientImpl ����Ƿ������ݵ����
* ApplicationHistoryServer.startWebApp()  -> AHSWebApp -> TimelineWebServices postEntities putDomain ������������������

Rpc�ο���д����  RPCCallBenchmark



ApplicationHistoryClientService  10200 RPC server .. 



ApplicationHistoryServer -> 
	ApplicationHistoryManager historyManager = createApplicationHistoryManager(conf);
    ApplicationHistoryClientService ahsClientService = createApplicationHistoryClientService(historyManager);
	
	
	
proto rpc:
	yarn_service_protos.proto  -> application_history_client.proto