# PySNMP SMI module. Autogenerated from smidump -f python NETSCREEN-SERVICE-MIB
# by libsmi2pysnmp-0.1.3 at Sat Oct 18 16:43:49 2014,
# Python version sys.version_info(major=2, minor=7, micro=3, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( netscreenService, ) = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenService")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")

# Objects

netscreenServiceMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 13, 0)).setRevisions(("2004-05-03 20:22","2004-05-03 00:00","2004-03-03 00:00","2003-11-10 00:00","2001-09-28 00:00","2001-05-14 00:00",))
if mibBuilder.loadTexts: netscreenServiceMibModule.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: netscreenServiceMibModule.setContactInfo("Customer Support\n\n1194 North Mathilda Avenue \nSunnyvale, California 94089-1206\nUSA\n\nTel: 1-800-638-8296\nE-mail: customerservice@juniper.net\nHTTP://www.juniper.net")
if mibBuilder.loadTexts: netscreenServiceMibModule.setDescription("This module defines the object that are used to monitor\nservice configuration in NetScreen device.")
nsServiceTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 13, 1))
if mibBuilder.loadTexts: nsServiceTable.setDescription("Services are types of IP traffic for which protocol standards\nexist. This table collects all the service configurations\nexisting in NetScreen device.")
nsServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 13, 1, 1)).setIndexNames((0, "NETSCREEN-SERVICE-MIB", "nsServiceIndex"))
if mibBuilder.loadTexts: nsServiceEntry.setDescription("Each enry in the nsServiceTable holds a set of configuration\nparameters  associated with an instance of service.")
nsServiceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 13, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsServiceIndex.setDescription("A unique value for each address.  Its value ranges between 0\nand 65535 and may not be contiguous.")
nsServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 13, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsServiceName.setDescription("Service name.")
nsServiceCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 13, 1, 1, 3), Integer().subtype(subtypeSpec=SingleValueConstraint(3,5,1,4,2,)).subtype(namedValues=NamedValues(("remote", 1), ("email", 2), ("infoseek", 3), ("security", 4), ("other", 5), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsServiceCategory.setDescription("Category this service belongs to.")
nsServiceTransProto = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 13, 1, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(17,0,9,46,1,89,47,6,8,)).subtype(namedValues=NamedValues(("other", 0), ("icmp", 1), ("udp", 17), ("rsvp", 46), ("gre", 47), ("tcp", 6), ("egp", 8), ("ospf", 89), ("igp", 9), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsServiceTransProto.setDescription("Service trans protocol.\n6 means tcp\n17 means udp")
nsServiceSrcPortLow = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 13, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsServiceSrcPortLow.setDescription("The low source port number associated with service.")
nsServiceSrcPortHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 13, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsServiceSrcPortHigh.setDescription("The high source port number associated with service.")
nsServiceDstPortLow = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 13, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsServiceDstPortLow.setDescription("The low destination port number associated with service.")
nsServiceDstPortHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 13, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsServiceDstPortHigh.setDescription("The high source port number associated with service.")
nsServiceFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 13, 1, 1, 9), Integer().subtype(subtypeSpec=SingleValueConstraint(0,1,)).subtype(namedValues=NamedValues(("pre-define", 0), ("usr-define", 1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsServiceFlag.setDescription("Service flag used to indicate if the service is a pre-defined\none or a custom one.")
nsServiceVsys = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 13, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsServiceVsys.setDescription("Virtual system this configuration belongs to.")
nsServiceGroupTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 13, 2))
if mibBuilder.loadTexts: nsServiceGroupTable.setDescription("Services can be organized into service group for convenience.\nThis table collects all service group entries in NetScreen\ndevice.")
nsServiceGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 13, 2, 1)).setIndexNames((0, "NETSCREEN-SERVICE-MIB", "nsServiceGroupIndex"))
if mibBuilder.loadTexts: nsServiceGroupEntry.setDescription("Each entry in the nsServiceGroupTable holds a set of\ninformation about service group.")
nsServiceGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 13, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsServiceGroupIndex.setDescription("A unique value for each group.  Its value ranges between 0 and\n65535 and may not be contiguous.")
nsServiceGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 13, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsServiceGroupName.setDescription("Service group name.")
nsServiceGroupMember = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 13, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsServiceGroupMember.setDescription("Service member number in service group.")
nsServiceGroupComment = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 13, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsServiceGroupComment.setDescription("Comments for service group.")
nsServiceGroupVsys = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 13, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsServiceGroupVsys.setDescription("Virtual system this group belongs to.")
nsServiceGrpMemberTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 13, 3))
if mibBuilder.loadTexts: nsServiceGrpMemberTable.setDescription("Service group membership info table will show detail\ninformation of a service group.")
nsServiceGrpMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 13, 3, 1)).setIndexNames((0, "NETSCREEN-SERVICE-MIB", "nsServiceGrpMemberIndex"))
if mibBuilder.loadTexts: nsServiceGrpMemberEntry.setDescription("An entry containing attributes service group's member info")
nsServiceGrpMemberIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 13, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsServiceGrpMemberIndex.setDescription("A unique value for each group.  Its value ranges between 0 and\n65535 and may not be contiguous.")
nsServiceGrpName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 13, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsServiceGrpName.setDescription("Specific service group name")
nsServiceGroupMemberName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 13, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsServiceGroupMemberName.setDescription("Specific service name in the service group.")
nsServiceGroupMemberVsys = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 13, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsServiceGroupMemberVsys.setDescription("Virtual system this configuration belongs to")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("NETSCREEN-SERVICE-MIB", PYSNMP_MODULE_ID=netscreenServiceMibModule)

# Objects
mibBuilder.exportSymbols("NETSCREEN-SERVICE-MIB", netscreenServiceMibModule=netscreenServiceMibModule, nsServiceTable=nsServiceTable, nsServiceEntry=nsServiceEntry, nsServiceIndex=nsServiceIndex, nsServiceName=nsServiceName, nsServiceCategory=nsServiceCategory, nsServiceTransProto=nsServiceTransProto, nsServiceSrcPortLow=nsServiceSrcPortLow, nsServiceSrcPortHigh=nsServiceSrcPortHigh, nsServiceDstPortLow=nsServiceDstPortLow, nsServiceDstPortHigh=nsServiceDstPortHigh, nsServiceFlag=nsServiceFlag, nsServiceVsys=nsServiceVsys, nsServiceGroupTable=nsServiceGroupTable, nsServiceGroupEntry=nsServiceGroupEntry, nsServiceGroupIndex=nsServiceGroupIndex, nsServiceGroupName=nsServiceGroupName, nsServiceGroupMember=nsServiceGroupMember, nsServiceGroupComment=nsServiceGroupComment, nsServiceGroupVsys=nsServiceGroupVsys, nsServiceGrpMemberTable=nsServiceGrpMemberTable, nsServiceGrpMemberEntry=nsServiceGrpMemberEntry, nsServiceGrpMemberIndex=nsServiceGrpMemberIndex, nsServiceGrpName=nsServiceGrpName, nsServiceGroupMemberName=nsServiceGroupMemberName, nsServiceGroupMemberVsys=nsServiceGroupMemberVsys)

