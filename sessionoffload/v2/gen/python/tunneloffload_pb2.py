# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tunneloffload.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13tunneloffload.proto\x12\x10tunneloffload.v2\"\x13\n\x11\x43\x61pabilityRequest\"\xfc\x04\n\x12\x43\x61pabilityResponse\x12R\n\x12match_capabilities\x18\x01 \x01(\x0b\x32\x36.tunneloffload.v2.CapabilityResponse.MatchCapabilities\x12R\n\x12ipsec_capabilities\x18\x02 \x01(\x0b\x32\x36.tunneloffload.v2.CapabilityResponse.IPSecCapabilities\x12T\n\x13geneve_capabilities\x18\x03 \x01(\x0b\x32\x37.tunneloffload.v2.CapabilityResponse.GeneveCapabilities\x1a\x97\x01\n\x11MatchCapabilities\x12\"\n\x1aingress_interface_matching\x18\x01 \x01(\x08\x12\x16\n\x0evxlan_matching\x18\x02 \x01(\x08\x12\x17\n\x0fgeneve_matching\x18\x03 \x01(\x08\x12\x17\n\x0ftunnel_matching\x18\x04 \x01(\x08\x12\x14\n\x0cspi_matching\x18\x05 \x01(\x08\x1a\x8e\x01\n\x11IPSecCapabilities\x12@\n\x15tunnel_type_supported\x18\x01 \x03(\x0e\x32!.tunneloffload.v2.IPSecTunnelType\x12\x37\n\x14\x65ncryption_supported\x18\x02 \x03(\x0e\x32\x19.tunneloffload.v2.EncType\x1a=\n\x12GeneveCapabilities\x12\'\n\x1fnumber_geneve_options_supported\x18\x01 \x01(\r\"\xe5\x01\n\x13TunnelAdditionError\x12\x31\n\x0bmatch_error\x18\x01 \x01(\x0e\x32\x1c.tunneloffload.v2.MatchError\x12\x33\n\x0ctunnel_error\x18\x02 \x01(\x0e\x32\x1d.tunneloffload.v2.TunnelError\x12\x31\n\x0bipsec_error\x18\x03 \x01(\x0e\x32\x1c.tunneloffload.v2.IPSecError\x12\x33\n\x0cgeneve_error\x18\x04 \x01(\x0e\x32\x1d.tunneloffload.v2.GeneveError\"\xe8\x06\n\rMatchCriteria\x12\x19\n\x11ingress_interface\x18\x01 \x01(\t\x12,\n\tmac_match\x18\x02 \x01(\x0b\x32\x19.tunneloffload.v2.MacPair\x12\x31\n\nipv4_match\x18\x03 \x01(\x0b\x32\x1b.tunneloffload.v2.IPV4MatchH\x00\x12\x31\n\nipv6_match\x18\x04 \x01(\x0b\x32\x1b.tunneloffload.v2.IPV6MatchH\x00\x12\x11\n\ttunnel_id\x18\x05 \x01(\x04\x12\x41\n\x0bipsec_match\x18\x06 \x01(\x0b\x32*.tunneloffload.v2.MatchCriteria.IPSecMatchH\x01\x12\x43\n\x0cgeneve_match\x18\x07 \x01(\x0b\x32+.tunneloffload.v2.MatchCriteria.GeneveMatchH\x01\x12\x41\n\x0bvxlan_match\x18\x08 \x01(\x0b\x32*.tunneloffload.v2.MatchCriteria.VXLanMatchH\x01\x1a%\n\nIPSecMatch\x12\x0b\n\x03spi\x18\x01 \x01(\r\x12\n\n\x02sn\x18\x02 \x01(\r\x1a\xd1\x01\n\x0bGeneveMatch\x12\x0b\n\x03vni\x18\x01 \x01(\r\x12,\n\tmac_match\x18\x02 \x01(\x0b\x32\x19.tunneloffload.v2.MacPair\x12\x15\n\rprotocol_type\x18\x03 \x01(\r\x12\x31\n\nipv4_match\x18\x04 \x01(\x0b\x32\x1b.tunneloffload.v2.IPV4MatchH\x00\x12\x31\n\nipv6_match\x18\x05 \x01(\x0b\x32\x1b.tunneloffload.v2.IPV6MatchH\x00\x42\n\n\x08ip_match\x1a\xb9\x01\n\nVXLanMatch\x12\x0b\n\x03vni\x18\x01 \x01(\r\x12,\n\tmac_match\x18\x02 \x01(\x0b\x32\x19.tunneloffload.v2.MacPair\x12\x31\n\nipv4_match\x18\x03 \x01(\x0b\x32\x1b.tunneloffload.v2.IPV4MatchH\x00\x12\x31\n\nipv6_match\x18\x04 \x01(\x0b\x32\x1b.tunneloffload.v2.IPV6MatchH\x00\x42\n\n\x08ip_matchB\n\n\x08ip_matchB\x07\n\x05match\"\xcf\x02\n\x0fIpTunnelRequest\x12\x11\n\ttunnel_id\x18\x01 \x01(\x04\x12.\n\toperation\x18\x02 \x01(\x0e\x32\x1b.tunneloffload.v2.Operation\x12\x37\n\x0ematch_criteria\x18\x03 \x01(\x0b\x32\x1f.tunneloffload.v2.MatchCriteria\x12-\n\x0bnext_action\x18\x04 \x01(\x0e\x32\x18.tunneloffload.v2.Action\x12\x35\n\x0cipsec_tunnel\x18\x05 \x01(\x0b\x32\x1d.tunneloffload.v2.IPSecTunnelH\x00\x12*\n\x06geneve\x18\x06 \x01(\x0b\x32\x18.tunneloffload.v2.GeneveH\x00\x12$\n\x03nat\x18\x07 \x01(\x0b\x32\x15.tunneloffload.v2.NatH\x00\x42\x08\n\x06tunnel\"\x85\x01\n\x06Geneve\x12\x35\n\x0cgeneve_encap\x18\x01 \x01(\x0b\x32\x1d.tunneloffload.v2.GeneveEncapH\x00\x12\x35\n\x0cgeneve_decap\x18\x02 \x01(\x0b\x32\x1d.tunneloffload.v2.GeneveDecapH\x00\x42\r\n\x0b\x65ncap_decap\"P\n\x0cGeneveOption\x12\x14\n\x0coption_class\x18\x01 \x01(\r\x12\x0c\n\x04type\x18\x02 \x01(\r\x12\x0e\n\x06length\x18\x03 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\"\xdf\x02\n\x0bGeneveEncap\x12\x35\n\x0fouter_ipv4_pair\x18\x01 \x01(\x0b\x32\x1a.tunneloffload.v2.IPV4PairH\x00\x12\x35\n\x0fouter_ipv6_pair\x18\x02 \x01(\x0b\x32\x1a.tunneloffload.v2.IPV6PairH\x00\x12\x31\n\x0einner_mac_pair\x18\x03 \x01(\x0b\x32\x19.tunneloffload.v2.MacPair\x12\x15\n\roption_length\x18\x04 \x01(\r\x12\x16\n\x0e\x63ontrol_packet\x18\x05 \x01(\x08\x12\x1f\n\x17\x63ritical_option_present\x18\x06 \x01(\x08\x12\x0b\n\x03vni\x18\x07 \x01(\r\x12\x15\n\rprotocol_type\x18\x08 \x01(\r\x12\x35\n\rgeneve_option\x18\t \x03(\x0b\x32\x1e.tunneloffload.v2.GeneveOptionB\x04\n\x02ip\"\r\n\x0bGeneveDecap\"6\n\x07MacPair\x12\x17\n\x0f\x64\x65stination_mac\x18\x01 \x01(\x0c\x12\x12\n\nsource_mac\x18\x02 \x01(\x0c\"5\n\x08IPV4Pair\x12\x11\n\tsource_ip\x18\x01 \x01(\x07\x12\x16\n\x0e\x64\x65stination_ip\x18\x02 \x01(\x07\"5\n\x08IPV6Pair\x12\x11\n\tsource_ip\x18\x01 \x01(\x0c\x12\x16\n\x0e\x64\x65stination_ip\x18\x02 \x01(\x0c\"o\n\tIPV4Match\x12\x11\n\tsource_ip\x18\x01 \x01(\x07\x12\x18\n\x10source_ip_prefix\x18\x02 \x01(\r\x12\x16\n\x0e\x64\x65stination_ip\x18\x03 \x01(\x07\x12\x1d\n\x15\x64\x65stination_ip_prefix\x18\x04 \x01(\r\"o\n\tIPV6Match\x12\x11\n\tsource_ip\x18\x01 \x01(\x0c\x12\x18\n\x10source_ip_prefix\x18\x02 \x01(\r\x12\x16\n\x0e\x64\x65stination_ip\x18\x03 \x01(\x0c\x12\x1d\n\x15\x64\x65stination_ip_prefix\x18\x04 \x01(\r\"\x18\n\x03Nat\x12\x11\n\tsource_ip\x18\x01 \x01(\r\"\x9c\x02\n\x08IPSecEnc\x12\x36\n\x0btunnel_type\x18\x01 \x01(\x0e\x32!.tunneloffload.v2.IPSecTunnelType\x12\x32\n\x0f\x65ncryption_type\x18\x02 \x01(\x0e\x32\x19.tunneloffload.v2.EncType\x12\x31\n\x08ipsec_sa\x18\x03 \x01(\x0b\x32\x1f.tunneloffload.v2.IPSecSAParams\x12\x31\n\x0bipv4_tunnel\x18\x04 \x01(\x0b\x32\x1a.tunneloffload.v2.IPV4PairH\x00\x12\x31\n\x0bipv6_tunnel\x18\x05 \x01(\x0b\x32\x1a.tunneloffload.v2.IPV6PairH\x00\x42\x0b\n\ttunnelIps\"\xaa\x01\n\x08IPSecDec\x12\x36\n\x0btunnel_type\x18\x01 \x01(\x0e\x32!.tunneloffload.v2.IPSecTunnelType\x12\x32\n\x0f\x65ncryption_type\x18\x02 \x01(\x0e\x32\x19.tunneloffload.v2.EncType\x12\x32\n\tipsec_sas\x18\x03 \x03(\x0b\x32\x1f.tunneloffload.v2.IPSecSAParams\"d\n\rIPSecSAParams\x12\x0b\n\x03spi\x18\x01 \x01(\r\x12\x16\n\x0e\x65ncryption_key\x18\x02 \x01(\x0c\x12.\n\toperation\x18\x03 \x01(\x0e\x32\x1b.tunneloffload.v2.Operation\"x\n\x0bIPSecTunnel\x12/\n\tipsec_enc\x18\x01 \x01(\x0b\x32\x1a.tunneloffload.v2.IPSecEncH\x00\x12/\n\tipsec_dec\x18\x02 \x01(\x0b\x32\x1a.tunneloffload.v2.IPSecDecH\x00\x42\x07\n\x05ipsec\"\x1d\n\x08TunnelId\x12\x11\n\ttunnel_id\x18\x01 \x01(\x04\"\xbe\x01\n\x08\x43ounters\x12\x12\n\nin_packets\x18\x01 \x01(\x04\x12\x13\n\x0bout_packets\x18\x02 \x01(\x04\x12\x10\n\x08in_bytes\x18\x03 \x01(\x04\x12\x11\n\tout_bytes\x18\x04 \x01(\x04\x12\x18\n\x10in_packets_drops\x18\x05 \x01(\x04\x12\x19\n\x11out_packets_drops\x18\x06 \x01(\x04\x12\x16\n\x0ein_bytes_drops\x18\x07 \x01(\x04\x12\x17\n\x0fout_bytes_drops\x18\x08 \x01(\x04\"\xa7\x01\n\x17\x43reateIpTunnelResponses\x12\x39\n\x0erequest_status\x18\x01 \x01(\x0e\x32!.tunneloffload.v2.AddTunnelStatus\x12\x14\n\x0c\x65rror_status\x18\x02 \x01(\x04\x12;\n\tresponses\x18\x03 \x03(\x0b\x32(.tunneloffload.v2.CreateIpTunnelResponse\"S\n\x16\x43reateIpTunnelResponse\x12\x11\n\ttunnel_id\x18\x01 \x01(\x04\x12&\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x17.tunneloffload.v2.Error\"[\n\x05\x45rror\x12<\n\rerror_message\x18\x01 \x01(\x0b\x32%.tunneloffload.v2.TunnelAdditionError\x12\x14\n\x0c\x65rror_string\x18\x02 \x01(\t\"J\n\x11IpTunnelResponses\x12\x35\n\tresponses\x18\x01 \x03(\x0b\x32\".tunneloffload.v2.IpTunnelResponse\"\xb8\x01\n\x10IpTunnelResponse\x12\x11\n\ttunnel_id\x18\x01 \x01(\x04\x12\x34\n\tip_tunnel\x18\x02 \x01(\x0b\x32!.tunneloffload.v2.IpTunnelRequest\x12\x33\n\x0ftunnel_counters\x18\x03 \x01(\x0b\x32\x1a.tunneloffload.v2.Counters\x12&\n\x05\x65rror\x18\x04 \x01(\x0b\x32\x17.tunneloffload.v2.Error\"T\n\x16IpTunnelStatsResponses\x12:\n\tresponses\x18\x01 \x03(\x0b\x32\'.tunneloffload.v2.IpTunnelStatsResponse\"\x87\x01\n\x15IpTunnelStatsResponse\x12\x11\n\ttunnel_id\x18\x01 \x01(\x04\x12\x33\n\x0ftunnel_counters\x18\x02 \x01(\x0b\x32\x1a.tunneloffload.v2.Counters\x12&\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x17.tunneloffload.v2.Error\"0\n\x11TunnelRequestArgs\x12\x1b\n\x13tunnels_per_request\x18\x01 \x01(\r*\x90\x01\n\x0f\x41\x64\x64TunnelStatus\x12\x14\n\x10_TUNNEL_ACCEPTED\x10\x00\x12\x14\n\x10_TUNNEL_REJECTED\x10\x01\x12\x16\n\x12_TUNNEL_TABLE_FULL\x10\x02\x12\x1d\n\x19_TUNNEL_TABLE_UNAVAILABLE\x10\x03\x12\x1a\n\x16_TUNNEL_ALREADY_EXISTS\x10\x04*=\n\tOperation\x12\t\n\x05_NONE\x10\x00\x12\x0b\n\x07_CREATE\x10\x01\x12\x0b\n\x07_UPDATE\x10\x02\x12\x0b\n\x07_DELETE\x10\x03*\xe5\x01\n\x07\x45ncType\x12\x10\n\x0c_AES256GCM64\x10\x00\x12\x10\n\x0c_AES256GCM96\x10\x01\x12\x11\n\r_AES256GCM128\x10\x02\x12\x10\n\x0c_AES128GCM64\x10\x03\x12\x10\n\x0c_AES128GCM96\x10\x04\x12\x11\n\r_AES128GCM128\x10\x05\x12\x10\n\x0c_AES256CCM64\x10\x06\x12\x10\n\x0c_AES256CCM96\x10\x07\x12\x11\n\r_AES256CCM128\x10\x08\x12\x10\n\x0c_AES128CCM64\x10\t\x12\x10\n\x0c_AES128CCM96\x10\n\x12\x11\n\r_AES128CCM128\x10\x0b*0\n\x06\x41\x63tion\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07\x46ORWARD\x10\x01\x12\x0f\n\x0bRECIRCULATE\x10\x02*c\n\nMatchError\x12\x11\n\rMISING_FIELDS\x10\x00\x12\x15\n\x11INVALID_TUNNEL_ID\x10\x01\x12\x18\n\x14INVALID_CAPABILITIES\x10\x02\x12\x11\n\rINVALID_FIELD\x10\x03*\'\n\x0bTunnelError\x12\x18\n\x14NOT_SUPPORTED_TUNNEL\x10\x00*t\n\nIPSecError\x12\x0f\n\x0bINVALID_KEY\x10\x00\x12\x1c\n\x18NON_SUPPORTED_ENCRYPTION\x10\x01\x12\x1d\n\x19NON_SUPPORTED_TUNNEL_TYPE\x10\x02\x12\x18\n\x14IPSEC_MISSING_FIELDS\x10\x03*Q\n\x0bGeneveError\x12\x12\n\x0eINVALID_OPTION\x10\x00\x12\x14\n\x10TOO_MANY_OPTIONS\x10\x01\x12\x18\n\x14INVALID_GENEVE_FIELD\x10\x02*c\n\x0fIPSecTunnelType\x12\r\n\tTRANSPORT\x10\x00\x12\n\n\x06TUNNEL\x10\x01\x12\x1b\n\x17TRANSPORT_NAT_TRAVERSAL\x10\x02\x12\x18\n\x14TUNNEL_NAT_TRAVERSAL\x10\x03\x32\xc8\x04\n\x0fIpTunnelService\x12Y\n\x0c\x43\x61pabilities\x12#.tunneloffload.v2.CapabilityRequest\x1a$.tunneloffload.v2.CapabilityResponse\x12\x62\n\x0e\x43reateIpTunnel\x12!.tunneloffload.v2.IpTunnelRequest\x1a).tunneloffload.v2.CreateIpTunnelResponses\"\x00(\x01\x12O\n\x0bGetIpTunnel\x12\x1a.tunneloffload.v2.TunnelId\x1a\".tunneloffload.v2.IpTunnelResponse\"\x00\x12Y\n\x10GetIpTunnelStats\x12\x1a.tunneloffload.v2.TunnelId\x1a\'.tunneloffload.v2.IpTunnelStatsResponse\"\x00\x12_\n\x0fGetAllIpTunnels\x12#.tunneloffload.v2.TunnelRequestArgs\x1a#.tunneloffload.v2.IpTunnelResponses\"\x00\x30\x01\x12i\n\x14GetAllIpTunnelsStats\x12#.tunneloffload.v2.TunnelRequestArgs\x1a(.tunneloffload.v2.IpTunnelStatsResponses\"\x00\x30\x01\x42&Z$github.com/att/sessionOffload/protosb\x06proto3')

_ADDTUNNELSTATUS = DESCRIPTOR.enum_types_by_name['AddTunnelStatus']
AddTunnelStatus = enum_type_wrapper.EnumTypeWrapper(_ADDTUNNELSTATUS)
_OPERATION = DESCRIPTOR.enum_types_by_name['Operation']
Operation = enum_type_wrapper.EnumTypeWrapper(_OPERATION)
_ENCTYPE = DESCRIPTOR.enum_types_by_name['EncType']
EncType = enum_type_wrapper.EnumTypeWrapper(_ENCTYPE)
_ACTION = DESCRIPTOR.enum_types_by_name['Action']
Action = enum_type_wrapper.EnumTypeWrapper(_ACTION)
_MATCHERROR = DESCRIPTOR.enum_types_by_name['MatchError']
MatchError = enum_type_wrapper.EnumTypeWrapper(_MATCHERROR)
_TUNNELERROR = DESCRIPTOR.enum_types_by_name['TunnelError']
TunnelError = enum_type_wrapper.EnumTypeWrapper(_TUNNELERROR)
_IPSECERROR = DESCRIPTOR.enum_types_by_name['IPSecError']
IPSecError = enum_type_wrapper.EnumTypeWrapper(_IPSECERROR)
_GENEVEERROR = DESCRIPTOR.enum_types_by_name['GeneveError']
GeneveError = enum_type_wrapper.EnumTypeWrapper(_GENEVEERROR)
_IPSECTUNNELTYPE = DESCRIPTOR.enum_types_by_name['IPSecTunnelType']
IPSecTunnelType = enum_type_wrapper.EnumTypeWrapper(_IPSECTUNNELTYPE)
_TUNNEL_ACCEPTED = 0
_TUNNEL_REJECTED = 1
_TUNNEL_TABLE_FULL = 2
_TUNNEL_TABLE_UNAVAILABLE = 3
_TUNNEL_ALREADY_EXISTS = 4
_NONE = 0
_CREATE = 1
_UPDATE = 2
_DELETE = 3
_AES256GCM64 = 0
_AES256GCM96 = 1
_AES256GCM128 = 2
_AES128GCM64 = 3
_AES128GCM96 = 4
_AES128GCM128 = 5
_AES256CCM64 = 6
_AES256CCM96 = 7
_AES256CCM128 = 8
_AES128CCM64 = 9
_AES128CCM96 = 10
_AES128CCM128 = 11
NONE = 0
FORWARD = 1
RECIRCULATE = 2
MISING_FIELDS = 0
INVALID_TUNNEL_ID = 1
INVALID_CAPABILITIES = 2
INVALID_FIELD = 3
NOT_SUPPORTED_TUNNEL = 0
INVALID_KEY = 0
NON_SUPPORTED_ENCRYPTION = 1
NON_SUPPORTED_TUNNEL_TYPE = 2
IPSEC_MISSING_FIELDS = 3
INVALID_OPTION = 0
TOO_MANY_OPTIONS = 1
INVALID_GENEVE_FIELD = 2
TRANSPORT = 0
TUNNEL = 1
TRANSPORT_NAT_TRAVERSAL = 2
TUNNEL_NAT_TRAVERSAL = 3


_CAPABILITYREQUEST = DESCRIPTOR.message_types_by_name['CapabilityRequest']
_CAPABILITYRESPONSE = DESCRIPTOR.message_types_by_name['CapabilityResponse']
_CAPABILITYRESPONSE_MATCHCAPABILITIES = _CAPABILITYRESPONSE.nested_types_by_name['MatchCapabilities']
_CAPABILITYRESPONSE_IPSECCAPABILITIES = _CAPABILITYRESPONSE.nested_types_by_name['IPSecCapabilities']
_CAPABILITYRESPONSE_GENEVECAPABILITIES = _CAPABILITYRESPONSE.nested_types_by_name['GeneveCapabilities']
_TUNNELADDITIONERROR = DESCRIPTOR.message_types_by_name['TunnelAdditionError']
_MATCHCRITERIA = DESCRIPTOR.message_types_by_name['MatchCriteria']
_MATCHCRITERIA_IPSECMATCH = _MATCHCRITERIA.nested_types_by_name['IPSecMatch']
_MATCHCRITERIA_GENEVEMATCH = _MATCHCRITERIA.nested_types_by_name['GeneveMatch']
_MATCHCRITERIA_VXLANMATCH = _MATCHCRITERIA.nested_types_by_name['VXLanMatch']
_IPTUNNELREQUEST = DESCRIPTOR.message_types_by_name['IpTunnelRequest']
_GENEVE = DESCRIPTOR.message_types_by_name['Geneve']
_GENEVEOPTION = DESCRIPTOR.message_types_by_name['GeneveOption']
_GENEVEENCAP = DESCRIPTOR.message_types_by_name['GeneveEncap']
_GENEVEDECAP = DESCRIPTOR.message_types_by_name['GeneveDecap']
_MACPAIR = DESCRIPTOR.message_types_by_name['MacPair']
_IPV4PAIR = DESCRIPTOR.message_types_by_name['IPV4Pair']
_IPV6PAIR = DESCRIPTOR.message_types_by_name['IPV6Pair']
_IPV4MATCH = DESCRIPTOR.message_types_by_name['IPV4Match']
_IPV6MATCH = DESCRIPTOR.message_types_by_name['IPV6Match']
_NAT = DESCRIPTOR.message_types_by_name['Nat']
_IPSECENC = DESCRIPTOR.message_types_by_name['IPSecEnc']
_IPSECDEC = DESCRIPTOR.message_types_by_name['IPSecDec']
_IPSECSAPARAMS = DESCRIPTOR.message_types_by_name['IPSecSAParams']
_IPSECTUNNEL = DESCRIPTOR.message_types_by_name['IPSecTunnel']
_TUNNELID = DESCRIPTOR.message_types_by_name['TunnelId']
_COUNTERS = DESCRIPTOR.message_types_by_name['Counters']
_CREATEIPTUNNELRESPONSES = DESCRIPTOR.message_types_by_name['CreateIpTunnelResponses']
_CREATEIPTUNNELRESPONSE = DESCRIPTOR.message_types_by_name['CreateIpTunnelResponse']
_ERROR = DESCRIPTOR.message_types_by_name['Error']
_IPTUNNELRESPONSES = DESCRIPTOR.message_types_by_name['IpTunnelResponses']
_IPTUNNELRESPONSE = DESCRIPTOR.message_types_by_name['IpTunnelResponse']
_IPTUNNELSTATSRESPONSES = DESCRIPTOR.message_types_by_name['IpTunnelStatsResponses']
_IPTUNNELSTATSRESPONSE = DESCRIPTOR.message_types_by_name['IpTunnelStatsResponse']
_TUNNELREQUESTARGS = DESCRIPTOR.message_types_by_name['TunnelRequestArgs']
CapabilityRequest = _reflection.GeneratedProtocolMessageType('CapabilityRequest', (_message.Message,), {
  'DESCRIPTOR' : _CAPABILITYREQUEST,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.CapabilityRequest)
  })
_sym_db.RegisterMessage(CapabilityRequest)

CapabilityResponse = _reflection.GeneratedProtocolMessageType('CapabilityResponse', (_message.Message,), {

  'MatchCapabilities' : _reflection.GeneratedProtocolMessageType('MatchCapabilities', (_message.Message,), {
    'DESCRIPTOR' : _CAPABILITYRESPONSE_MATCHCAPABILITIES,
    '__module__' : 'tunneloffload_pb2'
    # @@protoc_insertion_point(class_scope:tunneloffload.v2.CapabilityResponse.MatchCapabilities)
    })
  ,

  'IPSecCapabilities' : _reflection.GeneratedProtocolMessageType('IPSecCapabilities', (_message.Message,), {
    'DESCRIPTOR' : _CAPABILITYRESPONSE_IPSECCAPABILITIES,
    '__module__' : 'tunneloffload_pb2'
    # @@protoc_insertion_point(class_scope:tunneloffload.v2.CapabilityResponse.IPSecCapabilities)
    })
  ,

  'GeneveCapabilities' : _reflection.GeneratedProtocolMessageType('GeneveCapabilities', (_message.Message,), {
    'DESCRIPTOR' : _CAPABILITYRESPONSE_GENEVECAPABILITIES,
    '__module__' : 'tunneloffload_pb2'
    # @@protoc_insertion_point(class_scope:tunneloffload.v2.CapabilityResponse.GeneveCapabilities)
    })
  ,
  'DESCRIPTOR' : _CAPABILITYRESPONSE,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.CapabilityResponse)
  })
_sym_db.RegisterMessage(CapabilityResponse)
_sym_db.RegisterMessage(CapabilityResponse.MatchCapabilities)
_sym_db.RegisterMessage(CapabilityResponse.IPSecCapabilities)
_sym_db.RegisterMessage(CapabilityResponse.GeneveCapabilities)

TunnelAdditionError = _reflection.GeneratedProtocolMessageType('TunnelAdditionError', (_message.Message,), {
  'DESCRIPTOR' : _TUNNELADDITIONERROR,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.TunnelAdditionError)
  })
_sym_db.RegisterMessage(TunnelAdditionError)

MatchCriteria = _reflection.GeneratedProtocolMessageType('MatchCriteria', (_message.Message,), {

  'IPSecMatch' : _reflection.GeneratedProtocolMessageType('IPSecMatch', (_message.Message,), {
    'DESCRIPTOR' : _MATCHCRITERIA_IPSECMATCH,
    '__module__' : 'tunneloffload_pb2'
    # @@protoc_insertion_point(class_scope:tunneloffload.v2.MatchCriteria.IPSecMatch)
    })
  ,

  'GeneveMatch' : _reflection.GeneratedProtocolMessageType('GeneveMatch', (_message.Message,), {
    'DESCRIPTOR' : _MATCHCRITERIA_GENEVEMATCH,
    '__module__' : 'tunneloffload_pb2'
    # @@protoc_insertion_point(class_scope:tunneloffload.v2.MatchCriteria.GeneveMatch)
    })
  ,

  'VXLanMatch' : _reflection.GeneratedProtocolMessageType('VXLanMatch', (_message.Message,), {
    'DESCRIPTOR' : _MATCHCRITERIA_VXLANMATCH,
    '__module__' : 'tunneloffload_pb2'
    # @@protoc_insertion_point(class_scope:tunneloffload.v2.MatchCriteria.VXLanMatch)
    })
  ,
  'DESCRIPTOR' : _MATCHCRITERIA,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.MatchCriteria)
  })
_sym_db.RegisterMessage(MatchCriteria)
_sym_db.RegisterMessage(MatchCriteria.IPSecMatch)
_sym_db.RegisterMessage(MatchCriteria.GeneveMatch)
_sym_db.RegisterMessage(MatchCriteria.VXLanMatch)

IpTunnelRequest = _reflection.GeneratedProtocolMessageType('IpTunnelRequest', (_message.Message,), {
  'DESCRIPTOR' : _IPTUNNELREQUEST,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.IpTunnelRequest)
  })
_sym_db.RegisterMessage(IpTunnelRequest)

Geneve = _reflection.GeneratedProtocolMessageType('Geneve', (_message.Message,), {
  'DESCRIPTOR' : _GENEVE,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.Geneve)
  })
_sym_db.RegisterMessage(Geneve)

GeneveOption = _reflection.GeneratedProtocolMessageType('GeneveOption', (_message.Message,), {
  'DESCRIPTOR' : _GENEVEOPTION,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.GeneveOption)
  })
_sym_db.RegisterMessage(GeneveOption)

GeneveEncap = _reflection.GeneratedProtocolMessageType('GeneveEncap', (_message.Message,), {
  'DESCRIPTOR' : _GENEVEENCAP,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.GeneveEncap)
  })
_sym_db.RegisterMessage(GeneveEncap)

GeneveDecap = _reflection.GeneratedProtocolMessageType('GeneveDecap', (_message.Message,), {
  'DESCRIPTOR' : _GENEVEDECAP,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.GeneveDecap)
  })
_sym_db.RegisterMessage(GeneveDecap)

MacPair = _reflection.GeneratedProtocolMessageType('MacPair', (_message.Message,), {
  'DESCRIPTOR' : _MACPAIR,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.MacPair)
  })
_sym_db.RegisterMessage(MacPair)

IPV4Pair = _reflection.GeneratedProtocolMessageType('IPV4Pair', (_message.Message,), {
  'DESCRIPTOR' : _IPV4PAIR,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.IPV4Pair)
  })
_sym_db.RegisterMessage(IPV4Pair)

IPV6Pair = _reflection.GeneratedProtocolMessageType('IPV6Pair', (_message.Message,), {
  'DESCRIPTOR' : _IPV6PAIR,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.IPV6Pair)
  })
_sym_db.RegisterMessage(IPV6Pair)

IPV4Match = _reflection.GeneratedProtocolMessageType('IPV4Match', (_message.Message,), {
  'DESCRIPTOR' : _IPV4MATCH,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.IPV4Match)
  })
_sym_db.RegisterMessage(IPV4Match)

IPV6Match = _reflection.GeneratedProtocolMessageType('IPV6Match', (_message.Message,), {
  'DESCRIPTOR' : _IPV6MATCH,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.IPV6Match)
  })
_sym_db.RegisterMessage(IPV6Match)

Nat = _reflection.GeneratedProtocolMessageType('Nat', (_message.Message,), {
  'DESCRIPTOR' : _NAT,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.Nat)
  })
_sym_db.RegisterMessage(Nat)

IPSecEnc = _reflection.GeneratedProtocolMessageType('IPSecEnc', (_message.Message,), {
  'DESCRIPTOR' : _IPSECENC,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.IPSecEnc)
  })
_sym_db.RegisterMessage(IPSecEnc)

IPSecDec = _reflection.GeneratedProtocolMessageType('IPSecDec', (_message.Message,), {
  'DESCRIPTOR' : _IPSECDEC,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.IPSecDec)
  })
_sym_db.RegisterMessage(IPSecDec)

IPSecSAParams = _reflection.GeneratedProtocolMessageType('IPSecSAParams', (_message.Message,), {
  'DESCRIPTOR' : _IPSECSAPARAMS,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.IPSecSAParams)
  })
_sym_db.RegisterMessage(IPSecSAParams)

IPSecTunnel = _reflection.GeneratedProtocolMessageType('IPSecTunnel', (_message.Message,), {
  'DESCRIPTOR' : _IPSECTUNNEL,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.IPSecTunnel)
  })
_sym_db.RegisterMessage(IPSecTunnel)

TunnelId = _reflection.GeneratedProtocolMessageType('TunnelId', (_message.Message,), {
  'DESCRIPTOR' : _TUNNELID,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.TunnelId)
  })
_sym_db.RegisterMessage(TunnelId)

Counters = _reflection.GeneratedProtocolMessageType('Counters', (_message.Message,), {
  'DESCRIPTOR' : _COUNTERS,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.Counters)
  })
_sym_db.RegisterMessage(Counters)

CreateIpTunnelResponses = _reflection.GeneratedProtocolMessageType('CreateIpTunnelResponses', (_message.Message,), {
  'DESCRIPTOR' : _CREATEIPTUNNELRESPONSES,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.CreateIpTunnelResponses)
  })
_sym_db.RegisterMessage(CreateIpTunnelResponses)

CreateIpTunnelResponse = _reflection.GeneratedProtocolMessageType('CreateIpTunnelResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEIPTUNNELRESPONSE,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.CreateIpTunnelResponse)
  })
_sym_db.RegisterMessage(CreateIpTunnelResponse)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), {
  'DESCRIPTOR' : _ERROR,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.Error)
  })
_sym_db.RegisterMessage(Error)

IpTunnelResponses = _reflection.GeneratedProtocolMessageType('IpTunnelResponses', (_message.Message,), {
  'DESCRIPTOR' : _IPTUNNELRESPONSES,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.IpTunnelResponses)
  })
_sym_db.RegisterMessage(IpTunnelResponses)

IpTunnelResponse = _reflection.GeneratedProtocolMessageType('IpTunnelResponse', (_message.Message,), {
  'DESCRIPTOR' : _IPTUNNELRESPONSE,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.IpTunnelResponse)
  })
_sym_db.RegisterMessage(IpTunnelResponse)

IpTunnelStatsResponses = _reflection.GeneratedProtocolMessageType('IpTunnelStatsResponses', (_message.Message,), {
  'DESCRIPTOR' : _IPTUNNELSTATSRESPONSES,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.IpTunnelStatsResponses)
  })
_sym_db.RegisterMessage(IpTunnelStatsResponses)

IpTunnelStatsResponse = _reflection.GeneratedProtocolMessageType('IpTunnelStatsResponse', (_message.Message,), {
  'DESCRIPTOR' : _IPTUNNELSTATSRESPONSE,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.IpTunnelStatsResponse)
  })
_sym_db.RegisterMessage(IpTunnelStatsResponse)

TunnelRequestArgs = _reflection.GeneratedProtocolMessageType('TunnelRequestArgs', (_message.Message,), {
  'DESCRIPTOR' : _TUNNELREQUESTARGS,
  '__module__' : 'tunneloffload_pb2'
  # @@protoc_insertion_point(class_scope:tunneloffload.v2.TunnelRequestArgs)
  })
_sym_db.RegisterMessage(TunnelRequestArgs)

_IPTUNNELSERVICE = DESCRIPTOR.services_by_name['IpTunnelService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z$github.com/att/sessionOffload/protos'
  _ADDTUNNELSTATUS._serialized_start=4945
  _ADDTUNNELSTATUS._serialized_end=5089
  _OPERATION._serialized_start=5091
  _OPERATION._serialized_end=5152
  _ENCTYPE._serialized_start=5155
  _ENCTYPE._serialized_end=5384
  _ACTION._serialized_start=5386
  _ACTION._serialized_end=5434
  _MATCHERROR._serialized_start=5436
  _MATCHERROR._serialized_end=5535
  _TUNNELERROR._serialized_start=5537
  _TUNNELERROR._serialized_end=5576
  _IPSECERROR._serialized_start=5578
  _IPSECERROR._serialized_end=5694
  _GENEVEERROR._serialized_start=5696
  _GENEVEERROR._serialized_end=5777
  _IPSECTUNNELTYPE._serialized_start=5779
  _IPSECTUNNELTYPE._serialized_end=5878
  _CAPABILITYREQUEST._serialized_start=41
  _CAPABILITYREQUEST._serialized_end=60
  _CAPABILITYRESPONSE._serialized_start=63
  _CAPABILITYRESPONSE._serialized_end=699
  _CAPABILITYRESPONSE_MATCHCAPABILITIES._serialized_start=340
  _CAPABILITYRESPONSE_MATCHCAPABILITIES._serialized_end=491
  _CAPABILITYRESPONSE_IPSECCAPABILITIES._serialized_start=494
  _CAPABILITYRESPONSE_IPSECCAPABILITIES._serialized_end=636
  _CAPABILITYRESPONSE_GENEVECAPABILITIES._serialized_start=638
  _CAPABILITYRESPONSE_GENEVECAPABILITIES._serialized_end=699
  _TUNNELADDITIONERROR._serialized_start=702
  _TUNNELADDITIONERROR._serialized_end=931
  _MATCHCRITERIA._serialized_start=934
  _MATCHCRITERIA._serialized_end=1806
  _MATCHCRITERIA_IPSECMATCH._serialized_start=1348
  _MATCHCRITERIA_IPSECMATCH._serialized_end=1385
  _MATCHCRITERIA_GENEVEMATCH._serialized_start=1388
  _MATCHCRITERIA_GENEVEMATCH._serialized_end=1597
  _MATCHCRITERIA_VXLANMATCH._serialized_start=1600
  _MATCHCRITERIA_VXLANMATCH._serialized_end=1785
  _IPTUNNELREQUEST._serialized_start=1809
  _IPTUNNELREQUEST._serialized_end=2144
  _GENEVE._serialized_start=2147
  _GENEVE._serialized_end=2280
  _GENEVEOPTION._serialized_start=2282
  _GENEVEOPTION._serialized_end=2362
  _GENEVEENCAP._serialized_start=2365
  _GENEVEENCAP._serialized_end=2716
  _GENEVEDECAP._serialized_start=2718
  _GENEVEDECAP._serialized_end=2731
  _MACPAIR._serialized_start=2733
  _MACPAIR._serialized_end=2787
  _IPV4PAIR._serialized_start=2789
  _IPV4PAIR._serialized_end=2842
  _IPV6PAIR._serialized_start=2844
  _IPV6PAIR._serialized_end=2897
  _IPV4MATCH._serialized_start=2899
  _IPV4MATCH._serialized_end=3010
  _IPV6MATCH._serialized_start=3012
  _IPV6MATCH._serialized_end=3123
  _NAT._serialized_start=3125
  _NAT._serialized_end=3149
  _IPSECENC._serialized_start=3152
  _IPSECENC._serialized_end=3436
  _IPSECDEC._serialized_start=3439
  _IPSECDEC._serialized_end=3609
  _IPSECSAPARAMS._serialized_start=3611
  _IPSECSAPARAMS._serialized_end=3711
  _IPSECTUNNEL._serialized_start=3713
  _IPSECTUNNEL._serialized_end=3833
  _TUNNELID._serialized_start=3835
  _TUNNELID._serialized_end=3864
  _COUNTERS._serialized_start=3867
  _COUNTERS._serialized_end=4057
  _CREATEIPTUNNELRESPONSES._serialized_start=4060
  _CREATEIPTUNNELRESPONSES._serialized_end=4227
  _CREATEIPTUNNELRESPONSE._serialized_start=4229
  _CREATEIPTUNNELRESPONSE._serialized_end=4312
  _ERROR._serialized_start=4314
  _ERROR._serialized_end=4405
  _IPTUNNELRESPONSES._serialized_start=4407
  _IPTUNNELRESPONSES._serialized_end=4481
  _IPTUNNELRESPONSE._serialized_start=4484
  _IPTUNNELRESPONSE._serialized_end=4668
  _IPTUNNELSTATSRESPONSES._serialized_start=4670
  _IPTUNNELSTATSRESPONSES._serialized_end=4754
  _IPTUNNELSTATSRESPONSE._serialized_start=4757
  _IPTUNNELSTATSRESPONSE._serialized_end=4892
  _TUNNELREQUESTARGS._serialized_start=4894
  _TUNNELREQUESTARGS._serialized_end=4942
  _IPTUNNELSERVICE._serialized_start=5881
  _IPTUNNELSERVICE._serialized_end=6465
# @@protoc_insertion_point(module_scope)
