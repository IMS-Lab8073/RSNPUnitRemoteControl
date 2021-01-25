#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file RSNPUnitConnector.py
 @brief send data to Unit and recieve data from Unit
 @date $Date$


"""
import sys
import time
import json
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

import MQTTClient

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
rsnpunitconnector_spec = ["implementation_id", "RSNPUnitConnector",
		 "type_name",         "RSNPUnitConnector",
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
# @class RSNPUnitConnector
# @brief send data to Unit and recieve data from Unit
#
#
class RSNPUnitConnector(OpenRTM_aist.DataFlowComponentBase):

	##
	# @brief constructor
	# @param manager Maneger Object
	#
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_stringIn = RTC.TimedString(RTC.Time(0,0), "")
		"""
		"""
		self._stringInIn = OpenRTM_aist.InPort("stringIn", self._d_stringIn)
		self._d_robotPose2DIn = RTC.TimedPose2D(RTC.Time(0,0), RTC.Pose2D(RTC.Point2D(0.0,0.0), 0.0))
		"""
		"""
		self._robotPose2DInIn = OpenRTM_aist.InPort("robotPose2DIn", self._d_robotPose2DIn)
		self._d_countIn = RTC.TimedShort(RTC.Time(0,0), 0)
		"""
		"""
		self._countInIn = OpenRTM_aist.InPort("countIn", self._d_countIn)
		self._d_velocityOut = RTC.TimedVelocity2D(RTC.Time(0,0), RTC.Velocity2D(0.0,0.0,0.0))
		"""
		"""
		self._velocityOutOut = OpenRTM_aist.OutPort("velocityOut", self._d_velocityOut)

		self._d_doubleSeqOut = RTC.TimedDoubleSeq(RTC.Time(0,0), [])
		"""
		"""
		self._doubleSeqOutOut = OpenRTM_aist.OutPort("doubleSeqOut", self._d_doubleSeqOut)





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
		self.addInPort("stringIn",self._stringInIn)
		self.addInPort("robotPose2DIn",self._robotPose2DInIn)
		self.addInPort("countIn",self._countInIn)

		# Set OutPort buffers
		self.addOutPort("velocityOut",self._velocityOutOut)
		self.addOutPort("doubleSeqOut",self._doubleSeqOutOut)

		# Set service provider to Ports

		# Set service consumers to Ports

		# Set CORBA Service Ports

		return RTC.RTC_OK

	###
	##
	## The finalize action (on ALIVE->END transition)
	## formaer rtc_exiting_entry()
	##
	## @return RTC::ReturnCode_t
	#
	##
	#def onFinalize(self):
	#
	#	return RTC.RTC_OK

	###
	##
	## The startup action when ExecutionContext startup
	## former rtc_starting_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The shutdown action when ExecutionContext stop
	## former rtc_stopping_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
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
		print("Activate and connect unit")
		self.mqttc = MQTTClient.MyMQTTClass()
		self.mqttc.run(self._UnitHostname[0], "fromServer/Velocity")
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
		print("Deactivate")
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
		# MQTT subscribe data
		# data format : {"robotID":"", "vx":"", "va":"", "option":"", "timestamp":""}
		if self.mqttc.isNew():
			if self.mqttc.recieve_data=="NoData":
				self._d_velocityOut.data.vx = 0
				self._d_velocityOut.data.va = 0
				self._d_velocityOut.data.vy = 0
				self._velocityOutOut.write()
			else:
				print(self.mqttc.recieve_data)
				self.velocity = json.loads(self.mqttc.recieve_data)
				vx = float(self.velocity["vx"]) / 1500
				va = float(self.velocity["va"]) / 1500

				self._d_velocityOut.data.vx = vx
				self._d_velocityOut.data.va = va
				self._d_velocityOut.data.vy = 0
				self._velocityOutOut.write()

				pattern = self.velocity["option"]

				# set list data
				listdata = []
				if pattern=="A":
					listdata = []
				elif pattern=="B":
					listdata = []
				elif pattern=="C":
					listdata = []
				elif pattern=="D":
					listdata = []
				elif pattern=="E":
					listdata = []
				
				# write
				self._doubleSeqOutOut.data = listdata
				self._doubleSeqOutOut.write()

		# MQTT publish data
		send_data_dict = {"data_type":"","data":""}

		if self._stringInIn.isNew():
			self._stringInIn.read()
			send_data_dict["data_type"] = "other"
			send_data_dict["data"]      = self._d_stringIn.data
			send_data_json = json.dumps(send_data_dict)
			self.mqttc.publish_message(self._UnitHostname[0], "toUnit/Robotdata", send_data_json)
		
		if self._robotPose2DInIn.isNew():
			self._robotPose2DInIn.read()
			odometry_x     = self._d_robotPose2DIn.data.position.x
			odometry_y     = self._d_robotPose2DIn.data.position.y
			odometry_h     = self._d_robotPose2DIn.data.heading
			odometry_str   = "x:"+str(odometry_x)+"y:"+str(odometry_y)+"heading:"+str(odometry_h)
			send_data_dict["data_type"] = "odometry"
			send_data_dict["data"]      = odometry_str
			send_data_json = json.dumps(send_data_dict)
			self.mqttc.publish_message(self._UnitHostname[0], "toUnit/Robotdata", send_data_json)
		
		if self._countInIn.isNew():
			self._countInIn.read()
			send_data_dict["data_type"] = "count"
			send_data_dict["data"]      = self._d_countIn.data
			send_data_json = json.dumps(send_data_dict)
			self.mqttc.publish_message(self._UnitHostname[0], "toUnit/Robotdata", send_data_json)
		return RTC.RTC_OK

	###
	##
	## The aborting action when main logic error occurred.
	## former rtc_aborting_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The error action in ERROR state
	## former rtc_error_do()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The reset action that is invoked resetting
	## This is same but different the former rtc_init_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The state update action that is invoked after onExecute() action
	## no corresponding operation exists in OpenRTm-aist-0.2.0
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##

	##
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The action that is invoked when execution context's rate is changed
	## no corresponding operation exists in OpenRTm-aist-0.2.0
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK




def RSNPUnitConnectorInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=rsnpunitconnector_spec)
    manager.registerFactory(profile,
                            RSNPUnitConnector,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    RSNPUnitConnectorInit(manager)

    # Create a component
    comp = manager.createComponent("RSNPUnitConnector")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

