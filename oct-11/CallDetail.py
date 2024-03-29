class CallDetail:
	def __init__(self, caller, receiver, dura, typ):
		self.caller = caller
		self.receiver = receiver
		self.dura = dura
		self.typ = typ


class Util:
	def __init__(self):
		self.list_of_call_object = None

	def parse_customer(self, list_of_call_string):
		self.list_of_call_object = []
		for call in list_of_call_string:
			call_detail = call.split(',')
			self.list_of_call_object.append(CallDetail(call_detail[0], call_detail[1], call_detail[2], call_detail[3]))

	def print_details(self):
		print("Call details", end='\n\n')
		for ob in self.list_of_call_object:
			print("Caller number:", ob.caller)
			print("Receiver number:", ob.receiver)
			print("Call duration:", ob.dura)
			print("Call type:", ob.typ)
			print()	


call1 = "9990000001,9330000001,23,STD"
call2 = "9990000001,9330000002,54,Local"
call3 = "9990000001,9330000003,12,ISD"

list_of_call_string = [call1, call2, call3]
ut = Util()
ut.parse_customer(list_of_call_string)
ut.print_details()
