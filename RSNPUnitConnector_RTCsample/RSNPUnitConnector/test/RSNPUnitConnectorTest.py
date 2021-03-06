﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file RSNPUnitConnectorTest.py
 @brief send data to Unit and recieve data from Unit
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
rsnpunitconnectortest_spec = ["implementation_id", "RSNPUnitConnectorTest", 
		 "type_name",         "RSNPUnitConnectorTest", 
		 "description",       "send data to Unit and recieve data from Unit", 
		 "version",           "1.0.0", 
		 "vendor",            "KoichiroKato", 
		 "category",          "Category", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "1", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 "conf.default.UnitHostname", "rsnpunit",

		 "conf.__widget__.UnitHostname", "text",

         "conf.__type__.UnitHostname", "string",

		 ""]
# </rtc-template>

##
# @class RSNPUnitConnectorTest
# @brief send data to Unit and recieve data from Unit
# 
# 
class RSNPUnitConnectorTest(OpenRTM_aist.DataFlowComponentBase):
	
	##
	# @brief constructor
	# @param manager Maneger Object
	# 
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_velocityOut = OpenRTM_aist.instantiateDataType(RTC.TimedVelocity2D)
		"""
		"""
		self._velocityOutIn = OpenRTM_aist.InPort("velocityOut", self._d_velocityOut)
		self._d_stringIn = OpenRTM_aist.instantiateDataType(RTC.TimedString)
		"""
		"""
		self._stringInOut = OpenRTM_aist.OutPort("stringIn", self._d_stringIn)
		self._d_robotPose2DIn = OpenRTM_aist.instantiateDataType(RTC.TimedPose2D)
		"""
		"""
		self._robotPose2DInOut = OpenRTM_aist.OutPort("robotPose2DIn", self._d_robotPose2DIn)
		self._d_countIn = OpenRTM_aist.instantiateDataType(RTC.TimedShort)
		"""
		"""
		self._countInOut = OpenRTM_aist.OutPort("countIn", self._d_countIn)


		


		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		"""
		
		 - Name:  UnitHostname
		 - DefaultValue: rsnpunit
		"""
		self._UnitHostname = ['rsnpunit']
		
		# </rtc-template>


		 
	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry() 
	# 
	# @return RTC::ReturnCode_t
	# 
	#
	def onInitialize(self):
		# Bind variables and configuration variable
		self.bindParameter("UnitHostname", self._UnitHostname, "rsnpunit")
		
		# Set InPort buffers
		self.addInPort("velocityOut",self._velocityOutIn)
		
		# Set OutPort buffers
		self.addOutPort("stringIn",self._stringInOut)
		self.addOutPort("robotPose2DIn",self._robotPose2DInOut)
		self.addOutPort("countIn",self._countInOut)
		
		# Set service provider to Ports
		
		# Set service consumers to Ports
		
		# Set CORBA Service Ports
		
		return RTC.RTC_OK
	
	#	##
	#	# 
	#	# The finalize action (on ALIVE->END transition)
	#	# formaer rtc_exiting_entry()
	#	# 
	#	# @return RTC::ReturnCode_t
	#
	#	# 
	#def onFinalize(self):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The startup action when ExecutionContext startup
	#	# former rtc_starting_entry()
	#	# 
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The shutdown action when ExecutionContext stop
	#	# former rtc_stopping_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK
	
		##
		#
		# The activated action (Active state entry action)
		# former rtc_active_entry()
		#
		# @param ec_id target ExecutionContext Id
		# 
		# @return RTC::ReturnCode_t
		#
		#
	def onActivated(self, ec_id):
	
		return RTC.RTC_OK
	
		##
		#
		# The deactivated action (Active state exit action)
		# former rtc_active_exit()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onDeactivated(self, ec_id):
	
		return RTC.RTC_OK
	
		##
		#
		# The execution action that is invoked periodically
		# former rtc_active_do()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onExecute(self, ec_id):
	
		return RTC.RTC_OK
	
	#	##
	#	#
	#	# The aborting action when main logic error occurred.
	#	# former rtc_aborting_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The error action in ERROR state
	#	# former rtc_error_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The reset action that is invoked resetting
	#	# This is same but different the former rtc_init_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The state update action that is invoked after onExecute() action
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#

	#	#
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The action that is invoked when execution context's rate is changed
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK
	



def RSNPUnitConnectorTestInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=rsnpunitconnectortest_spec)
    manager.registerFactory(profile,
                            RSNPUnitConnectorTest,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    RSNPUnitConnectorTestInit(manager)

    # Create a component
    comp = manager.createComponent("RSNPUnitConnectorTest")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

