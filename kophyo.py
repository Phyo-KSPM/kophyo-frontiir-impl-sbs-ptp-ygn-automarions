import sys
import os
import time
import paramiko
import subprocess

def Descriptions():
	main = """
 /////////////////////////////////////////////////////////////////////////////
 //                                                                         //
 //                        Network Automation System                        //
 //                                                                         //
 //                            [KO PHYO PTP-Team]                           //
 //                                                                         //
 /////////////////////////////////////////////////////////////////////////////



  [1] for Channel 149                      [2] for Channel 153

  [3] for Channel 157                      [4] for Channel 161

  [5] for Channel 165                      [6] for Channel 169

  [7] for Channel 173                      [help] 



 """
	print(main)

def down():
	host = raw_input(" Enter Device ip address: ")
	parallel = (" -i1 -t100 -P8")
	os.system ('iperf3 -c '+host+parallel)
	print ('*******************************************************************************')
	print ('*                                                                             *')
	print ('*                          PTP-Team Yangon (Ko Phyo)                          *')
	print ('*                                                                             *')
	print ('*******************************************************************************')
	print ('')
	print ('')
	print (' Program Finished !!!')
	print ('')
	print (' Press Enter to continues')
	os.system('read answer')

def up():
	host = raw_input(" Enter Device ip address: ")
	parallel = (" -i1 -t100 -P8 -R")
	os.system ('iperf3 -c '+host+parallel)
	print ('*******************************************************************************')
	print ('*                                                                             *')
	print ('*                          PTP-Team Yangon (Ko Phyo)                          *')
	print ('*                                                                             *')
	print ('*******************************************************************************')
	print ('')
	print ('')
	print (' Program Finished !!!')
	print ('')
	print (' Press Enter to continues')
	os.system('read answer')

def downt():
	host = raw_input(" Enter Device ip address: ")
	parallel = (" -i1 -t100 -P8 |grep SUM")
	os.system ('iperf3 -c '+host+parallel)
	print ('*******************************************************************************')
	print ('*                                                                             *')
	print ('*                          PTP-Team Yangon (Ko Phyo)                          *')
	print ('*                                                                             *')
	print ('*******************************************************************************')
	print ('')
	print ('')
	print (' Program Finished !!!')
	print ('')
	print (' Press Enter to continues')
	os.system('read answer')

def upt():
	host = raw_input(" Enter Device ip address: ")
	parallel = (" -i1 -t100 -P8 -R |grep SUM")
	os.system ('iperf3 -c '+host+parallel)
	print ('*******************************************************************************')
	print ('*                                                                             *')
	print ('*                          PTP-Team Yangon (Ko Phyo)                          *')
	print ('*                                                                             *')
	print ('*******************************************************************************')
	print ('')
	print ('')
	print (' Program Finished !!!')
	print ('')
	print (' Press Enter to continues')
	os.system('read answer')

def check_description():
	finished = "  Complete   "
	ani_list = ['[          ]','[*         ]','[**        ]','[***       ]','[****      ]','[*****     ]','[******    ]','[*******   ]','[********  ]','[********* ]','[**********]']
	for i in ani_list:
		i = i[0:]
		time.sleep(0.1)
		os.system('clear')
		print '  Checking ', i
	print(finished)

def config_description():
	finished = "  Complete   "
	ani_list = ['[          ]','[*         ]','[**        ]','[***       ]','[****      ]','[*****     ]','[******    ]','[*******   ]','[********  ]','[********* ]','[**********]']
	for i in ani_list:
		i = i[0:]
		time.sleep(3.5)
		os.system('clear')
		print '  Configurations process start ', i
	print(finished)

def check_int_description():
	finished = "  Complete   "
	ani_list = ['[          ]','[*         ]','[**        ]','[***       ]','[****      ]','[*****     ]','[******    ]','[*******   ]','[********  ]','[********* ]','[**********]']
	for i in ani_list:
		i = i[0:]
		time.sleep(1.1)
		os.system('clear')
		print '  Scanning interference ', i
	print(finished)

def oub():
	print(' Press Enter to continues')
	os.system('read answer')

def ptool():
	host = raw_input(" Enter address: ")
	os.system ('ping -c 5 '+host)
	oub()

def check_duplex():
	host = raw_input(" Enter ip address :")
	port = 22
	username = "root"
	password = "Fr0nt!!r"
	skill = " |grep 'Speed\|Duplex'"
	Zero = "echo -------- Eth0"
	One = "echo -------- Eth1"
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=host,username=username,password=password)
	print " Successful connection....", host
	time.sleep (0.5)
	os.system('clear')
	remote_connection = ssh_client.invoke_shell()
	remote_connection.send ('echo ------ [ Eth0 ]'+' && ethtool eth0'+skill + ' && echo ------ [ Eth1 ]'+' && ethtool eth1'+skill+'\n')
	"""remote_connection.send ('cd scripts/bin\n')
	remote_connection.send ('./apget pub_sssid_enable\n')"""
	check_description()
	output = remote_connection.recv(65535)
	type(output)
	print ''.join (output)
	print ("")
	oub()

def TWO_2G_Check():
	host = raw_input(" Enter ip address :")
	port = 22
	username = "root"
	password = "Fr0nt!!r"
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=host,username=username,password=password)
	print " Successful connection....", host
	time.sleep (0.5)
	os.system('clear')
	remote_connection = ssh_client.invoke_shell()
	remote_connection.send ('cd scripts/bin\n')
	remote_connection.send ('./apget pub_sssid_enable\n')
	check_description()
	output = remote_connection.recv(65535)
	type(output)
	print ''.join (output)
	print ("")
	oub()

def rssi():
	host = raw_input(" Enter ip address :")
	port = 22
	username = "admin"
	password = "Fr0nt!!r"
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=host,username=username,password=password)
	print " Successful connection....", host
	time.sleep (0.5)
	os.system('clear')
	remote_connection = ssh_client.invoke_shell()
	remote_connection.send ('show rssi\n')
	check_description()
	output = remote_connection.recv(65535)
	type(output)
	print ''.join (output)
	print ("")
	oub()

def show_sw_mac():
	host = raw_input(" Enter ip address :")
	port = 22
	username = "operations"
	password = "Fr0nt!!r"
	skill = " |grep 'br0\|HWaddr'"
	skill2 = " |head -n1"
	skill3 = " |awk '{print $5}'"
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=host,username=username,password=password)
	print " Successful connection....", host
	time.sleep (0.5)
	os.system('clear')
	remote_connection = ssh_client.invoke_shell()
	remote_connection.send ('ifconfig'+skill+skill2+skill3+'\n')
	time.sleep(0.1)
	check_description()
	output = remote_connection.recv(65535)
	type(output)
	print ''.join (output)
	print ("")
	oub()

def minipc_mac():
	host = raw_input(" Enter ip address :")
	port = 22
	username = "operations"
	password = "Fr0nt!!r"
	skill = "|grep ether "
	skill2 = "|head -n1 "
	skill3 = "|awk '{print $2}'"
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=host,username=username,password=password)
	print " Successful connection....", host
	time.sleep (0.5)
	os.system('clear')
	remote_connection = ssh_client.invoke_shell()
	time.sleep(0.5)
	remote_connection.send ('clear \n')
	time.sleep(0.5)
	remote_connection.send ('ifconfig '+skill+skill2+skill3+'\n')
	check_description()
	output = remote_connection.recv(65535)
	type(output)
	print ''.join (output)
	print ("")
	oub()

def minipc_model():
	host = raw_input(" Enter ip address :")
	port = 22
	username = "operations"
	password = "Fr0nt!!r"
	skill = "|grep Ethernet "
	#skill2 = "|head -n1 "
	skill3 = "|awk '{print $7, $8, $9, $10, $11, $12}'"
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=host,username=username,password=password)
	print " Successful connection....", host
	time.sleep (0.5)
	os.system('clear')
	remote_connection = ssh_client.invoke_shell()
	time.sleep(0.5)
	remote_connection.send ('clear \n')
	time.sleep(0.5)
	remote_connection.send ('lspci '+skill+skill3+'\n')
	check_description()
	output = remote_connection.recv(65535)
	type(output)
	print ''.join (output)
	print ("")
	oub()

def sw_M_M():
	host = raw_input(" Enter ip address :")
	port = 22
	username = "operations"
	password = "Fr0nt!!r"
	command = "clear && echo 'Switch Information' && echo '==================' && cat board.info |grep board.name= |tail -n1 |cut -c 7-26 && ifconfig |grep 'br0\|HWaddr' |head -n1 |awk '{print $5}'"
	command2 = " && cat /tmp/running.cfg |grep switch.port.1.name |cut -c 8-40 && cat /tmp/running.cfg |grep switch.port.2.name |cut -c 8-40 && cat /tmp/running.cfg |grep switch.port.3.name |cut -c 8-40 && cat /tmp/running.cfg |grep switch.port.4.name |cut -c 8-40 && cat /tmp/running.cfg |grep switch.port.5.name |cut -c 8-40 && cat /tmp/running.cfg |grep switch.port.6.name |cut -c 8-40 && cat /tmp/running.cfg |grep switch.port.7.name |cut -c 8-40 && cat /tmp/running.cfg |grep switch.port.8.name |cut -c 8-40"
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=host,username=username,password=password)
	print " Successful connection....", host
	time.sleep (0.5)
	os.system('clear')
	remote_connection = ssh_client.invoke_shell()
	remote_connection.send ('cd / \n')
	remote_connection.send ('cd /etc \n')
	remote_connection.send (command+'\n')
	check_description()
	time.sleep(1)
	output = remote_connection.recv(65535)
	type(output)
	print ''.join (output)
	print ("")
	oub()

def show_sw_port():
	host = raw_input(" Enter ip address :")
	port = 22
	username = "operations"
	password = "Fr0nt!!r"
	command2 = "clear && cat /tmp/running.cfg |grep switch.port.1.name |cut -c 8-40 && cat /tmp/running.cfg |grep switch.port.2.name |cut -c 8-40 && cat /tmp/running.cfg |grep switch.port.3.name |cut -c 8-40 && cat /tmp/running.cfg |grep switch.port.4.name |cut -c 8-40 && cat /tmp/running.cfg |grep switch.port.5.name |cut -c 8-40 && cat /tmp/running.cfg |grep switch.port.6.name |cut -c 8-40 && cat /tmp/running.cfg |grep switch.port.7.name |cut -c 8-40 && cat /tmp/running.cfg |grep switch.port.8.name |cut -c 8-40"
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=host,username=username,password=password)
	print " Successful connection....", host
	time.sleep (0.5)
	os.system('clear')
	remote_connection = ssh_client.invoke_shell()
	remote_connection.send ('cd / \n')
	remote_connection.send ('cd /etc \n')
	remote_connection.send (command+'\n')
	check_description()
	time.sleep(1)
	output = remote_connection.recv(65535)
	type(output)
	print ''.join (output)
	print ("")
	oub()

def vxlan_check():
	host = raw_input(" Enter ip address :")
	port = 22
	username = "operations"
	password = "Fr0nt!!r"
	skill = "|grep ether "
	skill2 = "|head -n1 "
	skill3 = "|awk '{print $2}'"
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=host,username=username,password=password)
	print " Successful connection....", host
	time.sleep (0.5)
	os.system('clear')
	remote_connection = ssh_client.invoke_shell()
	time.sleep(0.5)
	remote_connection.send ('clear \n')
	time.sleep(0.5)
	remote_connection.send ('cd / \n')
	remote_connection.send ('cd etc \n')
	remote_connection.send ('cd vxconfig \n')
	remote_connection.send ('cat fwconfig.cfg \n')
	check_description()
	output = remote_connection.recv(65535)
	type(output)
	print ''.join (output)
	print ("")
	oub()

def poe_on():
	host = raw_input(" Enter ip address :")
	port = 22
	username = "root"
	password = "Fr0nt!!r"
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=host,username=username,password=password)
	print " Successful connection....", host
	time.sleep (0.5)
	os.system('clear')
	remote_connection = ssh_client.invoke_shell()
	remote_connection.send ('cd scripts/bin\n')
	remote_connection.send ('./apset eth1_poeout 1\n')
	remote_connection.send ('./apcommit\n')
	config_description()
	os.system ('clear')
	remote_connection.send ('./apget eth1_poeout \n')
	time.sleep(1)
	output = remote_connection.recv(65535)
	type(output)
	print ''.join (output)
	print ("")
	oub()

def poe_off():
	host = raw_input(" Enter ip address :")
	port = 22
	username = "root"
	password = "Fr0nt!!r"
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=host,username=username,password=password)
	print " Successful connection....", host
	time.sleep (0.5)
	os.system('clear')
	remote_connection = ssh_client.invoke_shell()
	remote_connection.send ('cd scripts/bin\n')
	remote_connection.send ('./apset eth1_poeout 0\n')
	remote_connection.send ('./apcommit\n')
	config_description()
	os.system ('clear')
	remote_connection.send ('./apget eth1_poeout \n')
	time.sleep(1)
	output = remote_connection.recv(65535)
	type(output)
	print ''.join (output)
	print ("")
	oub()

def TWO_2G_Append():
	host = raw_input(" Enter ip address :")
	port = 22
	username = "root"
	password = "Fr0nt!!r"
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=host,username=username,password=password)
	print " Successful connection....", host
	time.sleep (0.5)
	os.system('clear')
	remote_connection = ssh_client.invoke_shell()
	remote_connection.send ('cd scripts/bin\n')
	remote_connection.send ('./apset pub_sssid_enable 1\n')
	remote_connection.send ('./apcommit\n')
	config_description()
	output = remote_connection.recv(65535)
	type(output)
	print ''.join (output)
	print ("")
	oub()

def channel_check():
	host = raw_input(" Enter ip address :")
	port = 22
	username = "root"
	password = "Fr0nt!!r"
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=host,username=username,password=password)
	print " Successful connection....", host
	time.sleep (0.5)
	os.system('clear')
	remote_connection = ssh_client.invoke_shell()
	remote_connection.send ('cd scripts/bin\n')
	remote_connection.send ('./apget lan5g_channel && ./apget lan5g_txpwratten && ./apget lan_channel && ./apget eth1_poeout && ./apget pub_sssid_wan_enable && ./apget pub_sssid_enable && ./apget lan4_enable\n')
	check_description()
	output = remote_connection.recv(65535)
	type(output)
	print ''.join (output)
	print ("")
	oub()

def interference():
	host = raw_input(" Enter ip address :")
	port = 22
	username = "root"
	password = "Fr0nt!!r"
	skill = "|grep 'Address\|ESSID\|Frequency\|Quality'"
	skill2 = " |awk '{print $2}'"
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=host,username=username,password=password)
	print " Successful connection....", host
	time.sleep (0.5)
	os.system('clear')
	remote_connection = ssh_client.invoke_shell()
	remote_connection.send ('cd /scripts/bin\n')
	remote_connection.send ('iwlist ath11 scanning '+skill+ '\n')
	check_int_description()
	output = remote_connection.recv(65535)
	type(output)
	print ''.join (output)
	print ("")
	oub()

def model():
	host = raw_input(" Enter ip address :")
	port = 22
	username = "root"
	password = "Fr0nt!!r"
	power = "| awk '{print $3}'"
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=host,username=username,password=password)
	print " Successful connection....", host
	time.sleep (0.5)
	os.system('clear')
	remote_connection = ssh_client.invoke_shell()
	remote_connection.send ('cd /\n')
	remote_connection.send ('cd tmp/sysinfo\n')
	remote_connection.send ('clear && cat frontiir_model '+power+ '\n')
	time.sleep(0.5)
	output = remote_connection.recv(65535)
	type(output)
	print ("")
	print ''.join (output)
	print ("")
	oub()

def ping_multi_ip():
	os.system('clear')
	main = """
 /////////////////////////////////////////////////////////////////////////////
 //                                                                         //
 //                   Network Automation System [Site_Check]                //
 //                                                                         //
 //                            [KO PHYO PTP-Team]                           //
 //                                                                         //
 /////////////////////////////////////////////////////////////////////////////



  [1] Switch                        | Edge Switch

  [2] Access Point                  | Ruckus // Frontiir Device [ LAP/LAQ ]

  [3] Point to Point Devices        | Mimosa // ISO Station // Cambium

  [4] All Devices                   | All Devices [Onsite]

  [5] Exit

 """
 	num = 1
	while (num ==1):
		print (main)
		result_multi = raw_input("Choose number >>> ")
		if result_multi == '1':
			os.system('./switch')
			print (' Press Enter to continues')
			os.system('read answer')
			os.system('clear')
		elif result_multi == '2':
			os.system('./ap')
			print (' Press Enter to continues')
			os.system('read answer')
			os.system('clear')
		elif result_multi == '3':
			os.system('./ptp')
			print (' Press Enter to continues')
			os.system('read answer')
			os.system('clear')
		elif result_multi == '4':
			os.system('./all')
			print (' Press Enter to continues')
			os.system('read answer')
			os.system('clear')
		elif result_multi == 'exit':
			break
		elif result_multi == '5':
			break
		elif result_multi == 'Exit':
			break
		else:
			print('Input Error')
			os.system('read answer')
			os.system('clear')


def channel_149():
	host = raw_input(" Enter ip address :")
	port = 22
	username = "root"
	password = "Fr0nt!!r"
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=host,username=username,password=password)
	print " Successful connection....", host
	time.sleep (0.5)
	os.system('clear')
	remote_connection = ssh_client.invoke_shell()
	remote_connection.send ('cd scripts/bin/\n')
	remote_connection.send ('./apset lan5g_channel 149\n')
	remote_connection.send ('./apset lan5g_txpwratten 15\n')
	remote_connection.send ('./apset lan_channel 0\n')
	remote_connection.send ('./apset eth1_poeout 0\n')
	remote_connection.send ('./apset pub_sssid_wan_enable 1\n')
	remote_connection.send ('./apset pub_sssid_enable 1\n')
	remote_connection.send ('./apset lan4_enable 1\n')
	remote_connection.send ('./apcommit\n')
	config_description()
	remote_connection.send ('./apget lan5g_channel && ./apget lan5g_txpwratten && ./apget lan_channel && ./apget eth1_poeout && ./apget pub_sssid_wan_enable && ./apget pub_sssid_enable && ./apget lan4_enable\n')
	time.sleep(3)
	output = remote_connection.recv(65535)
	type(output)
	print ''.join (output)
	print ("")
	oub()

def channel_153():
	host = raw_input(" Enter ip address :")
	port = 22
	username = "root"
	password = "Fr0nt!!r"
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=host,username=username,password=password)
	print " Successful connection....", host
	time.sleep (0.5)
	os.system('clear')
	remote_connection = ssh_client.invoke_shell()
	remote_connection.send ('cd scripts/bin/\n')
	remote_connection.send ('./apset lan5g_channel 153\n')
	remote_connection.send ('./apset lan5g_txpwratten 15\n')
	remote_connection.send ('./apset lan_channel 0\n')
	remote_connection.send ('./apset eth1_poeout 0\n')
	remote_connection.send ('./apset pub_sssid_wan_enable 1\n')
	remote_connection.send ('./apset pub_sssid_enable 1\n')
	remote_connection.send ('./apset lan4_enable 1\n')
	remote_connection.send ('./apcommit\n')
	config_description()
	remote_connection.send ('./apget lan5g_channel && ./apget lan5g_txpwratten && ./apget lan_channel && ./apget eth1_poeout && ./apget pub_sssid_wan_enable && ./apget pub_sssid_enable && ./apget lan4_enable\n')
	time.sleep(3)
	output = remote_connection.recv(65535)
	type(output)
	print ''.join (output)
	print ("")
	oub()

def channel_157():
	host = raw_input(" Enter ip address :")
	port = 22
	username = "root"
	password = "Fr0nt!!r"
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=host,username=username,password=password)
	print " Successful connection....", host
	time.sleep (0.5)
	os.system('clear')
	remote_connection = ssh_client.invoke_shell()
	remote_connection.send ('cd scripts/bin/\n')
	remote_connection.send ('./apset lan5g_channel 157\n')
	remote_connection.send ('./apset lan5g_txpwratten 15\n')
	remote_connection.send ('./apset lan_channel 0\n')
	remote_connection.send ('./apset eth1_poeout 0\n')
	remote_connection.send ('./apset pub_sssid_wan_enable 1\n')
	remote_connection.send ('./apset pub_sssid_enable 1\n')
	remote_connection.send ('./apset lan4_enable 1\n')
	remote_connection.send ('./apcommit\n')
	config_description()
	remote_connection.send ('./apget lan5g_channel && ./apget lan5g_txpwratten && ./apget lan_channel && ./apget eth1_poeout && ./apget pub_sssid_wan_enable && ./apget pub_sssid_enable && ./apget lan4_enable\n')
	time.sleep(3)
	output = remote_connection.recv(65535)
	type(output)
	print ''.join (output)
	print ("")
	oub()

def channel_161():
	host = raw_input(" Enter ip address :")
	port = 22
	username = "root"
	password = "Fr0nt!!r"
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=host,username=username,password=password)
	print " Successful connection....", host
	time.sleep (0.5)
	os.system('clear')
	remote_connection = ssh_client.invoke_shell()
	remote_connection.send ('cd scripts/bin/\n')
	remote_connection.send ('./apset lan5g_channel 161\n')
	remote_connection.send ('./apset lan5g_txpwratten 15\n')
	remote_connection.send ('./apset lan_channel 0\n')
	remote_connection.send ('./apset eth1_poeout 0\n')
	remote_connection.send ('./apset pub_sssid_wan_enable 1\n')
	remote_connection.send ('./apset pub_sssid_enable 1\n')
	remote_connection.send ('./apset lan4_enable 1\n')
	remote_connection.send ('./apcommit\n')
	config_description()
	remote_connection.send ('./apget lan5g_channel && ./apget lan5g_txpwratten && ./apget lan_channel && ./apget eth1_poeout && ./apget pub_sssid_wan_enable && ./apget pub_sssid_enable && ./apget lan4_enable\n')
	time.sleep(3)
	output = remote_connection.recv(65535)
	type(output)
	print ''.join (output)
	print ("")
	oub()

def channel_165():
	host = raw_input(" Enter ip address :")
	port = 22
	username = "root"
	password = "Fr0nt!!r"
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=host,username=username,password=password)
	print " Successful connection....", host
	time.sleep (0.5)
	os.system('clear')
	remote_connection = ssh_client.invoke_shell()
	remote_connection.send ('cd scripts/bin/\n')
	remote_connection.send ('./apset lan5g_channel 165\n')
	remote_connection.send ('./apset lan5g_txpwratten 15\n')
	remote_connection.send ('./apset lan_channel 0\n')
	remote_connection.send ('./apset eth1_poeout 0\n')
	remote_connection.send ('./apset pub_sssid_wan_enable 1\n')
	remote_connection.send ('./apset pub_sssid_enable 1\n')
	remote_connection.send ('./apset lan4_enable 1\n')
	remote_connection.send ('./apcommit\n')
	config_description()
	remote_connection.send ('./apget lan5g_channel && ./apget lan5g_txpwratten && ./apget lan_channel && ./apget eth1_poeout && ./apget pub_sssid_wan_enable && ./apget pub_sssid_enable && ./apget lan4_enable\n')
	time.sleep(3)
	output = remote_connection.recv(65535)
	type(output)
	print ''.join (output)
	print ("")
	oub()

def channel_169():
	host = raw_input(" Enter ip address :")
	port = 22
	username = "root"
	password = "Fr0nt!!r"
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=host,username=username,password=password)
	print " Successful connection....", host
	time.sleep (0.5)
	os.system('clear')
	remote_connection = ssh_client.invoke_shell()
	remote_connection.send ('cd scripts/bin/\n')
	remote_connection.send ('./apset lan5g_channel 169\n')
	remote_connection.send ('./apset lan5g_txpwratten 15\n')
	remote_connection.send ('./apset lan_channel 0\n')
	remote_connection.send ('./apset eth1_poeout 0\n')
	remote_connection.send ('./apset pub_sssid_wan_enable 1\n')
	remote_connection.send ('./apset pub_sssid_enable 1\n')
	remote_connection.send ('./apset lan4_enable 1\n')
	remote_connection.send ('./apcommit\n')
	config_description()
	remote_connection.send ('./apget lan5g_channel && ./apget lan5g_txpwratten && ./apget lan_channel && ./apget eth1_poeout && ./apget pub_sssid_wan_enable && ./apget pub_sssid_enable && ./apget lan4_enable\n')
	time.sleep(3)
	output = remote_connection.recv(65535)
	type(output)
	print ''.join (output)
	print ("")
	oub()

def channel_173():
	host = raw_input(" Enter ip address :")
	port = 22
	username = "root"
	password = "Fr0nt!!r"
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=host,username=username,password=password)
	print " Successful connection....", host
	time.sleep (0.5)
	os.system('clear')
	remote_connection = ssh_client.invoke_shell()
	remote_connection.send ('cd scripts/bin/\n')
	remote_connection.send ('./apset lan5g_channel 173\n')
	remote_connection.send ('./apset lan5g_txpwratten 15\n')
	remote_connection.send ('./apset lan_channel 0\n')
	remote_connection.send ('./apset eth1_poeout 0\n')
	remote_connection.send ('./apset pub_sssid_wan_enable 1\n')
	remote_connection.send ('./apset pub_sssid_enable 1\n')
	remote_connection.send ('./apset lan4_enable 1\n')
	remote_connection.send ('./apcommit\n')
	config_description()
	remote_connection.send ('./apget lan5g_channel && ./apget lan5g_txpwratten && ./apget lan_channel && ./apget eth1_poeout && ./apget pub_sssid_wan_enable && ./apget pub_sssid_enable && ./apget lan4_enable\n')
	time.sleep(3)
	output = remote_connection.recv(65535)
	type(output)
	print ''.join (output)
	print ("")
	oub()

def esmac():
	host = raw_input(" Enter ip address :")
	port = 22
	username = "operations"
	password = "Fr0nt!!r"
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=host,username=username,password=password)
	print " Successful connection....", host
	time.sleep (0.5)
	os.system('clear')
	remote_connection = ssh_client.invoke_shell()
	remote_connection.send ('enable\n')
	remote_connection.send ('Fr0nt!!r\n')
	remote_connection.send ('show version | include Address\n')
	check_description()
	output = remote_connection.recv(65535)
	type(output)
	print ''.join (output)
	print ("")
	oub()

def sw_dev_check():
	host = raw_input(" Enter ip address: ")
	port = 22
	username = "operations"
	password = "Fr0nt!!r"
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=host,username=username,password=password)
	print " Successful connection....", host
	time.sleep (0.5)
	os.system('clear')
	remote_connection = ssh_client.invoke_shell()
	remote_connection.send ('cd / \n')
	remote_connection.send ('cat /etc/board.info |grep board.name= |tail -n1\n')
	check_description()
	output = remote_connection.recv(65535)
	type(output)
	print ''.join (output)
	print ("")
	oub()

def help():
    os.system('clear')
    main = """
Command                       Information
=====================================================================

    """
    print(main)
    time.sleep(0.1)
    print("down                          Test iperf download result")
    time.sleep(0.1)
    print("up                            Test iperf upload result")
    time.sleep(0.1)
    print("downt                         Test iperf download [ Total Result ]")
    time.sleep(0.1)
    print("upt                           Test iperf upload [ Total Result ]")
    time.sleep(0.1)
    print("show run                      Show [ LAP / LAQ ]Configurations")
    time.sleep(0.1)
    print("poeon                         Eth1 PoE [ ON ]")
    time.sleep(0.1)
    print("poeoff                        Eth1 PoE [ Off ]")
    time.sleep(0.1)
    print("2G check                      Checking [ 2G Channel ] On/Off !")
    time.sleep(0.1)
    print("2G on                         2G channel [ On ]")
    time.sleep(0.1)
    print("wscan                         Scanning interference")
    time.sleep(0.1)
    print("check                         Check [ LAP ? or LAQ ? ]")
    time.sleep(0.1)
    print("duplex                        Check Duplex [ 100 Mb | 1000 Mb ]")
    time.sleep(0.1)
    print("rssi                          Show Cambium RSSI")
    time.sleep(0.1)
    print("tsmac                         Show Touch Switch [ MAC ]")
    time.sleep(0.1)
    print("vxcheck                       Check VXLan [ Activate / Not Activate ]")
    time.sleep(0.1)
    print("minimodel                     Check mini pc [ Model ]")
    time.sleep(0.1)
    print("minimac                       Check mini pc [ MAC ]")
    time.sleep(0.1)
    print("sm                            Check Switch Model")
    time.sleep(0.1)
    print("multi-ping                    Check side [ DOWN or UP ] ")
    print('')
    os.system('read answer')

try:
	num = 1
	while (num ==1):
		os.system('clear')
		Descriptions()
		go = raw_input(' What do you want to do ? >>> ')
		if go == '3':
			print(' 157 channel selecting......')
			channel_157()
		elif go == '4':
			print(' 161 channel selecting......')
			channel_161()
		elif go == '5':
			print(' 165 channel selecting......')
			channel_165()
		elif go == '1':
			print(' 149 channel selecting......')
			channel_149()
		elif go == '2':
			print(' 153 channel selecting......')
			channel_153()
		elif go == '6':
			print(' 169 channel selecting......')
			channel_169()
		elif go == '7':
			print(' 173 channel selecting......')
			channel_173()
		elif go == 'show run':
			channel_check()
		elif go == 'up':
			up()
		elif go == 'down':
			down()
		elif go == 'downt':
			downt()
		elif go == 'upt':
			upt()
		elif go == 'check':
			print(' Checking Device.......')
			model()
		elif go == 'ping':
			ptool()
		elif go == 'wscan':
			time.sleep(0.5)
			interference()
		elif go == 'poeon':
			poe_on()
		elif go == 'poeoff':
			poe_off()
		elif go == 'rssi':
			rssi()
		elif go == 'vxcheck':
			vxlan_check()
		elif go == 'duplex':
			check_duplex()
		elif go == 'minimac':
			minipc_mac()
		elif go == 'minimodel':
			minipc_model()
		elif go == 'tsmac':
			show_sw_mac()
		elif go == 'esmac':
			esmac()
		elif go == 'sm':
			sw_dev_check()
		elif go == 'snmp':
			sw_M_M()
		elif go == 'show switch interference':
			show_sw_port()
		elif go == '2G check':
			print(' Checking 2G Channel On/Off !')
			TWO_2G_Check()
		elif go == '2G on':
			TWO_2G_Append()
		elif go == 'multi-ping':
			ping_multi_ip()
		elif go == 'cls':
			os.system('clear')
		elif go == 'clear':
			os.system('clear')
		elif go == 'help':
			help()
		elif go == 'exit':
			os.system('clear')
			break
		elif go == 'exit()':
			break
		else:
			print (' Input Error')
			time.sleep(0.2)
			oub()
except Exception as e:
	print (e)
	oub()
