# PySNMP SMI module. Autogenerated from smidump -f python NETSCREEN-ZONE-MIB
# by libsmi2pysnmp-0.1.3 at Sat Oct 18 16:44:19 2014,
# Python version sys.version_info(major=2, minor=7, micro=3, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( netscreenZone, ) = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenZone")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")

# Objects

netscreenZoneMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 8, 0)).setRevisions(("2004-05-03 20:22","2004-05-03 00:00","2004-03-03 00:00","2003-11-13 00:00","2001-09-28 00:00","2000-05-08 00:00",))
if mibBuilder.loadTexts: netscreenZoneMibModule.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: netscreenZoneMibModule.setContactInfo("Customer Support\n\n1194 North Mathilda Avenue \nSunnyvale, California 94089-1206\nUSA\n\nTel: 1-800-638-8296\nE-mail: customerservice@juniper.net\nHTTP://www.juniper.net")
if mibBuilder.loadTexts: netscreenZoneMibModule.setDescription("This module defines the object that are used to monitor all\nthe security zones")
nsZoneCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 8, 1))
nsZoneCfgTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 8, 1, 1))
if mibBuilder.loadTexts: nsZoneCfgTable.setDescription("NetScreen device can have lots of secure zone. This table\ncollects the zones exiting in NetScreen device.")
nsZoneCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 8, 1, 1, 1)).setIndexNames((0, "NETSCREEN-ZONE-MIB", "nsZoneCfgId"))
if mibBuilder.loadTexts: nsZoneCfgEntry.setDescription("Each entry in the table holds a set of configuration\nparameters associated  with an instance of secure zone.")
nsZoneCfgId = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 8, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsZoneCfgId.setDescription("A unique value for zone table.  Its value ranges between 1 and\n65535 and may not be contiguous.  the index has no other\nmeaning but a pure index")
nsZoneCfgName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 8, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsZoneCfgName.setDescription("Secure zone name.")
nsZoneCfgType = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 8, 1, 1, 1, 3), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,0,4,3,)).subtype(namedValues=NamedValues(("regular", 0), ("layer2", 1), ("tunnel", 2), ("null", 3), ("func", 4), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsZoneCfgType.setDescription("Secure zone type. Regular is sec(L3) and layer2 is sec(L2) type")
nsZoneCfgVsys = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 8, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsZoneCfgVsys.setDescription("VSYS this security zone belongs to.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("NETSCREEN-ZONE-MIB", PYSNMP_MODULE_ID=netscreenZoneMibModule)

# Objects
mibBuilder.exportSymbols("NETSCREEN-ZONE-MIB", netscreenZoneMibModule=netscreenZoneMibModule, nsZoneCfg=nsZoneCfg, nsZoneCfgTable=nsZoneCfgTable, nsZoneCfgEntry=nsZoneCfgEntry, nsZoneCfgId=nsZoneCfgId, nsZoneCfgName=nsZoneCfgName, nsZoneCfgType=nsZoneCfgType, nsZoneCfgVsys=nsZoneCfgVsys)

