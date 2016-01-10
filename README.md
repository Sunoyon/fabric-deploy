# fabric-deploy

This is a simple framework to provision remote host and deploy services in both dev and prod environment using fabric.
 
Environment can be set by `fab devhost` for development host OR `fab prodhost` for production host. Therefore anyone can write a fabric command (e.g, `def deploy()`) and run it in prod host by calling `fab prodhost deploy` or in dev host by calling `fab devhost deploy`.

 
## How to use


*   Configure host information of dev and prod in `host_config.yaml`
*	Provision host: `fab devhost provision_machine` OR `fab prodhost provision_machine` [code has to be written accordingly]
*	Deploy services: `fab devhost deploy` OR `fab prodhost deploy` [code has to be written accordingly]
*	New command can be written and run in both hosts. 