# pylint:disable=line-too-long
import logging

from ...sim_type import SimTypeFunction,     SimTypeShort, SimTypeInt, SimTypeLong, SimTypeLongLong, SimTypeDouble, SimTypeFloat,     SimTypePointer,     SimTypeChar,     SimStruct,     SimTypeFixedSizeArray,     SimTypeBottom,     SimUnion,     SimTypeBool
from ...calling_conventions import SimCCStdcall, SimCCMicrosoftAMD64
from .. import SIM_PROCEDURES as P
from . import SimLibrary


_l = logging.getLogger(name=__name__)


lib = SimLibrary()
lib.set_default_cc('X86', SimCCStdcall)
lib.set_default_cc('AMD64', SimCCMicrosoftAMD64)
lib.set_library_names("authz.dll")
prototypes = \
    {
        #
        'AuthzAccessCheck': SimTypeFunction([SimTypeInt(signed=False, label="AUTHZ_ACCESS_CHECK_FLAGS"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"DesiredAccess": SimTypeInt(signed=False, label="UInt32"), "PrincipalSelfSid": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "ObjectTypeList": SimTypePointer(SimTypeBottom(label="OBJECT_TYPE_LIST"), offset=0), "ObjectTypeListLength": SimTypeInt(signed=False, label="UInt32"), "OptionalArguments": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="AUTHZ_ACCESS_REQUEST", pack=False, align=None), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"Revision": SimTypeChar(label="Byte"), "Sbz1": SimTypeChar(label="Byte"), "Control": SimTypeShort(signed=False, label="UInt16"), "Owner": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "Group": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "Sacl": SimTypePointer(SimStruct({"AclRevision": SimTypeChar(label="Byte"), "Sbz1": SimTypeChar(label="Byte"), "AclSize": SimTypeShort(signed=False, label="UInt16"), "AceCount": SimTypeShort(signed=False, label="UInt16"), "Sbz2": SimTypeShort(signed=False, label="UInt16")}, name="ACL", pack=False, align=None), offset=0), "Dacl": SimTypePointer(SimStruct({"AclRevision": SimTypeChar(label="Byte"), "Sbz1": SimTypeChar(label="Byte"), "AclSize": SimTypeShort(signed=False, label="UInt16"), "AceCount": SimTypeShort(signed=False, label="UInt16"), "Sbz2": SimTypeShort(signed=False, label="UInt16")}, name="ACL", pack=False, align=None), offset=0)}, name="SECURITY_DESCRIPTOR", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimStruct({"Revision": SimTypeChar(label="Byte"), "Sbz1": SimTypeChar(label="Byte"), "Control": SimTypeShort(signed=False, label="UInt16"), "Owner": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "Group": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "Sacl": SimTypePointer(SimStruct({"AclRevision": SimTypeChar(label="Byte"), "Sbz1": SimTypeChar(label="Byte"), "AclSize": SimTypeShort(signed=False, label="UInt16"), "AceCount": SimTypeShort(signed=False, label="UInt16"), "Sbz2": SimTypeShort(signed=False, label="UInt16")}, name="ACL", pack=False, align=None), offset=0), "Dacl": SimTypePointer(SimStruct({"AclRevision": SimTypeChar(label="Byte"), "Sbz1": SimTypeChar(label="Byte"), "AclSize": SimTypeShort(signed=False, label="UInt16"), "AceCount": SimTypeShort(signed=False, label="UInt16"), "Sbz2": SimTypeShort(signed=False, label="UInt16")}, name="ACL", pack=False, align=None), offset=0)}, name="SECURITY_DESCRIPTOR", pack=False, align=None), offset=0), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"ResultListLength": SimTypeInt(signed=False, label="UInt32"), "GrantedAccessMask": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), "SaclEvaluationResults": SimTypePointer(SimTypeInt(signed=False, label="AUTHZ_GENERATE_RESULTS"), offset=0), "Error": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AUTHZ_ACCESS_REPLY", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Flags", "hAuthzClientContext", "pRequest", "hAuditEvent", "pSecurityDescriptor", "OptionalSecurityDescriptorArray", "OptionalSecurityDescriptorCount", "pReply", "phAccessCheckResults"]),
        #
        'AuthzCachedAccessCheck': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"DesiredAccess": SimTypeInt(signed=False, label="UInt32"), "PrincipalSelfSid": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "ObjectTypeList": SimTypePointer(SimTypeBottom(label="OBJECT_TYPE_LIST"), offset=0), "ObjectTypeListLength": SimTypeInt(signed=False, label="UInt32"), "OptionalArguments": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="AUTHZ_ACCESS_REQUEST", pack=False, align=None), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"ResultListLength": SimTypeInt(signed=False, label="UInt32"), "GrantedAccessMask": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), "SaclEvaluationResults": SimTypePointer(SimTypeInt(signed=False, label="AUTHZ_GENERATE_RESULTS"), offset=0), "Error": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AUTHZ_ACCESS_REPLY", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Flags", "hAccessCheckResults", "pRequest", "hAuditEvent", "pReply"]),
        #
        'AuthzOpenObjectAudit': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"DesiredAccess": SimTypeInt(signed=False, label="UInt32"), "PrincipalSelfSid": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "ObjectTypeList": SimTypePointer(SimTypeBottom(label="OBJECT_TYPE_LIST"), offset=0), "ObjectTypeListLength": SimTypeInt(signed=False, label="UInt32"), "OptionalArguments": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="AUTHZ_ACCESS_REQUEST", pack=False, align=None), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"Revision": SimTypeChar(label="Byte"), "Sbz1": SimTypeChar(label="Byte"), "Control": SimTypeShort(signed=False, label="UInt16"), "Owner": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "Group": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "Sacl": SimTypePointer(SimStruct({"AclRevision": SimTypeChar(label="Byte"), "Sbz1": SimTypeChar(label="Byte"), "AclSize": SimTypeShort(signed=False, label="UInt16"), "AceCount": SimTypeShort(signed=False, label="UInt16"), "Sbz2": SimTypeShort(signed=False, label="UInt16")}, name="ACL", pack=False, align=None), offset=0), "Dacl": SimTypePointer(SimStruct({"AclRevision": SimTypeChar(label="Byte"), "Sbz1": SimTypeChar(label="Byte"), "AclSize": SimTypeShort(signed=False, label="UInt16"), "AceCount": SimTypeShort(signed=False, label="UInt16"), "Sbz2": SimTypeShort(signed=False, label="UInt16")}, name="ACL", pack=False, align=None), offset=0)}, name="SECURITY_DESCRIPTOR", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimStruct({"Revision": SimTypeChar(label="Byte"), "Sbz1": SimTypeChar(label="Byte"), "Control": SimTypeShort(signed=False, label="UInt16"), "Owner": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "Group": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "Sacl": SimTypePointer(SimStruct({"AclRevision": SimTypeChar(label="Byte"), "Sbz1": SimTypeChar(label="Byte"), "AclSize": SimTypeShort(signed=False, label="UInt16"), "AceCount": SimTypeShort(signed=False, label="UInt16"), "Sbz2": SimTypeShort(signed=False, label="UInt16")}, name="ACL", pack=False, align=None), offset=0), "Dacl": SimTypePointer(SimStruct({"AclRevision": SimTypeChar(label="Byte"), "Sbz1": SimTypeChar(label="Byte"), "AclSize": SimTypeShort(signed=False, label="UInt16"), "AceCount": SimTypeShort(signed=False, label="UInt16"), "Sbz2": SimTypeShort(signed=False, label="UInt16")}, name="ACL", pack=False, align=None), offset=0)}, name="SECURITY_DESCRIPTOR", pack=False, align=None), offset=0), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"ResultListLength": SimTypeInt(signed=False, label="UInt32"), "GrantedAccessMask": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), "SaclEvaluationResults": SimTypePointer(SimTypeInt(signed=False, label="AUTHZ_GENERATE_RESULTS"), offset=0), "Error": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)}, name="AUTHZ_ACCESS_REPLY", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Flags", "hAuthzClientContext", "pRequest", "hAuditEvent", "pSecurityDescriptor", "OptionalSecurityDescriptorArray", "OptionalSecurityDescriptorCount", "pReply"]),
        #
        'AuthzFreeHandle': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hAccessCheckResults"]),
        #
        'AuthzInitializeResourceManager': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeFunction([SimTypeBottom(label="AUTHZ_CLIENT_CONTEXT_HANDLE"), SimTypePointer(SimTypeBottom(label="ACE_HEADER"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hAuthzClientContext", "pAce", "pArgs", "pbAceApplicable"]), offset=0), SimTypePointer(SimTypeFunction([SimTypeBottom(label="AUTHZ_CLIENT_CONTEXT_HANDLE"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="SID_AND_ATTRIBUTES"), offset=0), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="SID_AND_ATTRIBUTES"), offset=0), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hAuthzClientContext", "Args", "pSidAttrArray", "pSidCount", "pRestrictedSidAttrArray", "pRestrictedSidCount"]), offset=0), SimTypePointer(SimTypeFunction([SimTypePointer(SimTypeBottom(label="SID_AND_ATTRIBUTES"), offset=0)], SimTypeBottom(label="Void"), arg_names=["pSidAttrArray"]), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Flags", "pfnDynamicAccessCheck", "pfnComputeDynamicGroups", "pfnFreeDynamicGroups", "szResourceManagerName", "phAuthzResourceManager"]),
        #
        'AuthzInitializeResourceManagerEx': SimTypeFunction([SimTypeInt(signed=False, label="AUTHZ_RESOURCE_MANAGER_FLAGS"), SimTypePointer(SimStruct({"version": SimTypeShort(signed=False, label="UInt16"), "szResourceManagerName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "pfnDynamicAccessCheck": SimTypePointer(SimTypeFunction([SimTypeBottom(label="AUTHZ_CLIENT_CONTEXT_HANDLE"), SimTypePointer(SimTypeBottom(label="ACE_HEADER"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hAuthzClientContext", "pAce", "pArgs", "pbAceApplicable"]), offset=0), "pfnComputeDynamicGroups": SimTypePointer(SimTypeFunction([SimTypeBottom(label="AUTHZ_CLIENT_CONTEXT_HANDLE"), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="SID_AND_ATTRIBUTES"), offset=0), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="SID_AND_ATTRIBUTES"), offset=0), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hAuthzClientContext", "Args", "pSidAttrArray", "pSidCount", "pRestrictedSidAttrArray", "pRestrictedSidCount"]), offset=0), "pfnFreeDynamicGroups": SimTypePointer(SimTypeFunction([SimTypePointer(SimTypeBottom(label="SID_AND_ATTRIBUTES"), offset=0)], SimTypeBottom(label="Void"), arg_names=["pSidAttrArray"]), offset=0), "pfnGetCentralAccessPolicy": SimTypePointer(SimTypeFunction([SimTypeBottom(label="AUTHZ_CLIENT_CONTEXT_HANDLE"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hAuthzClientContext", "capid", "pArgs", "pCentralAccessPolicyApplicable", "ppCentralAccessPolicy"]), offset=0), "pfnFreeCentralAccessPolicy": SimTypePointer(SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeBottom(label="Void"), arg_names=["pCentralAccessPolicy"]), offset=0)}, name="AUTHZ_INIT_INFO", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Flags", "pAuthzInitInfo", "phAuthzResourceManager"]),
        #
        'AuthzInitializeRemoteResourceManager': SimTypeFunction([SimTypePointer(SimStruct({"version": SimTypeShort(signed=False, label="UInt16"), "ObjectUuid": SimTypePointer(SimTypeChar(label="Char"), offset=0), "ProtSeq": SimTypePointer(SimTypeChar(label="Char"), offset=0), "NetworkAddr": SimTypePointer(SimTypeChar(label="Char"), offset=0), "Endpoint": SimTypePointer(SimTypeChar(label="Char"), offset=0), "Options": SimTypePointer(SimTypeChar(label="Char"), offset=0), "ServerSpn": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="AUTHZ_RPC_INIT_INFO_CLIENT", pack=False, align=None), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["pRpcInitInfo", "phAuthzResourceManager"]),
        #
        'AuthzFreeResourceManager': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hAuthzResourceManager"]),
        #
        'AuthzInitializeContextFromToken': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimUnion({"Anonymous": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_Anonymous_e__Struct", pack=False, align=None), "u": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_u_e__Struct", pack=False, align=None), "QuadPart": SimTypeLongLong(signed=True, label="Int64")}, name="<anon>", label="None"), offset=0), SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="LUID", pack=False, align=None), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Flags", "TokenHandle", "hAuthzResourceManager", "pExpirationTime", "Identifier", "DynamicGroupArgs", "phAuthzClientContext"]),
        #
        'AuthzInitializeContextFromSid': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimUnion({"Anonymous": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_Anonymous_e__Struct", pack=False, align=None), "u": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_u_e__Struct", pack=False, align=None), "QuadPart": SimTypeLongLong(signed=True, label="Int64")}, name="<anon>", label="None"), offset=0), SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="LUID", pack=False, align=None), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Flags", "UserSid", "hAuthzResourceManager", "pExpirationTime", "Identifier", "DynamicGroupArgs", "phAuthzClientContext"]),
        #
        'AuthzInitializeContextFromAuthzContext': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimUnion({"Anonymous": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_Anonymous_e__Struct", pack=False, align=None), "u": SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="_u_e__Struct", pack=False, align=None), "QuadPart": SimTypeLongLong(signed=True, label="Int64")}, name="<anon>", label="None"), offset=0), SimStruct({"LowPart": SimTypeInt(signed=False, label="UInt32"), "HighPart": SimTypeInt(signed=True, label="Int32")}, name="LUID", pack=False, align=None), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["Flags", "hAuthzClientContext", "pExpirationTime", "Identifier", "DynamicGroupArgs", "phNewAuthzClientContext"]),
        #
        'AuthzInitializeCompoundContext': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["UserContext", "DeviceContext", "phCompoundContext"]),
        #
        'AuthzAddSidsToContext': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"Sid": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "Attributes": SimTypeInt(signed=False, label="UInt32")}, name="SID_AND_ATTRIBUTES", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"Sid": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "Attributes": SimTypeInt(signed=False, label="UInt32")}, name="SID_AND_ATTRIBUTES", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hAuthzClientContext", "Sids", "SidCount", "RestrictedSids", "RestrictedSidCount", "phNewAuthzClientContext"]),
        #
        'AuthzModifySecurityAttributes': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=False, label="AUTHZ_SECURITY_ATTRIBUTE_OPERATION"), offset=0), SimTypePointer(SimStruct({"Version": SimTypeShort(signed=False, label="UInt16"), "Reserved": SimTypeShort(signed=False, label="UInt16"), "AttributeCount": SimTypeInt(signed=False, label="UInt32"), "Attribute": SimUnion({"pAttributeV1": SimTypePointer(SimStruct({"pName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "ValueType": SimTypeShort(signed=False, label="UInt16"), "Reserved": SimTypeShort(signed=False, label="UInt16"), "Flags": SimTypeInt(signed=False, label="AUTHZ_SECURITY_ATTRIBUTE_FLAGS"), "ValueCount": SimTypeInt(signed=False, label="UInt32"), "Values": SimUnion({"pInt64": SimTypePointer(SimTypeLongLong(signed=True, label="Int64"), offset=0), "pUint64": SimTypePointer(SimTypeLongLong(signed=False, label="UInt64"), offset=0), "ppString": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), "pFqbn": SimTypePointer(SimStruct({"Version": SimTypeLongLong(signed=False, label="UInt64"), "pName": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="AUTHZ_SECURITY_ATTRIBUTE_FQBN_VALUE", pack=False, align=None), offset=0), "pOctetString": SimTypePointer(SimStruct({"pValue": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "ValueLength": SimTypeInt(signed=False, label="UInt32")}, name="AUTHZ_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE", pack=False, align=None), offset=0)}, name="<anon>", label="None")}, name="AUTHZ_SECURITY_ATTRIBUTE_V1", pack=False, align=None), offset=0)}, name="<anon>", label="None")}, name="AUTHZ_SECURITY_ATTRIBUTES_INFORMATION", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hAuthzClientContext", "pOperations", "pAttributes"]),
        #
        'AuthzModifyClaims': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="AUTHZ_CONTEXT_INFORMATION_CLASS"), SimTypePointer(SimTypeInt(signed=False, label="AUTHZ_SECURITY_ATTRIBUTE_OPERATION"), offset=0), SimTypePointer(SimStruct({"Version": SimTypeShort(signed=False, label="UInt16"), "Reserved": SimTypeShort(signed=False, label="UInt16"), "AttributeCount": SimTypeInt(signed=False, label="UInt32"), "Attribute": SimUnion({"pAttributeV1": SimTypePointer(SimStruct({"pName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "ValueType": SimTypeShort(signed=False, label="UInt16"), "Reserved": SimTypeShort(signed=False, label="UInt16"), "Flags": SimTypeInt(signed=False, label="AUTHZ_SECURITY_ATTRIBUTE_FLAGS"), "ValueCount": SimTypeInt(signed=False, label="UInt32"), "Values": SimUnion({"pInt64": SimTypePointer(SimTypeLongLong(signed=True, label="Int64"), offset=0), "pUint64": SimTypePointer(SimTypeLongLong(signed=False, label="UInt64"), offset=0), "ppString": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), "pFqbn": SimTypePointer(SimStruct({"Version": SimTypeLongLong(signed=False, label="UInt64"), "pName": SimTypePointer(SimTypeChar(label="Char"), offset=0)}, name="AUTHZ_SECURITY_ATTRIBUTE_FQBN_VALUE", pack=False, align=None), offset=0), "pOctetString": SimTypePointer(SimStruct({"pValue": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "ValueLength": SimTypeInt(signed=False, label="UInt32")}, name="AUTHZ_SECURITY_ATTRIBUTE_OCTET_STRING_VALUE", pack=False, align=None), offset=0)}, name="<anon>", label="None")}, name="AUTHZ_SECURITY_ATTRIBUTE_V1", pack=False, align=None), offset=0)}, name="<anon>", label="None")}, name="AUTHZ_SECURITY_ATTRIBUTES_INFORMATION", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hAuthzClientContext", "ClaimClass", "pClaimOperations", "pClaims"]),
        #
        'AuthzModifySids': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="AUTHZ_CONTEXT_INFORMATION_CLASS"), SimTypePointer(SimTypeInt(signed=False, label="AUTHZ_SID_OPERATION"), offset=0), SimTypePointer(SimStruct({"GroupCount": SimTypeInt(signed=False, label="UInt32"), "Groups": SimTypePointer(SimStruct({"Sid": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "Attributes": SimTypeInt(signed=False, label="UInt32")}, name="SID_AND_ATTRIBUTES", pack=False, align=None), offset=0)}, name="TOKEN_GROUPS", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hAuthzClientContext", "SidClass", "pSidOperations", "pSids"]),
        #
        'AuthzSetAppContainerInformation': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"Sid": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "Attributes": SimTypeInt(signed=False, label="UInt32")}, name="SID_AND_ATTRIBUTES", pack=False, align=None), label="LPArray", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hAuthzClientContext", "pAppContainerSid", "CapabilityCount", "pCapabilitySids"]),
        #
        'AuthzGetInformationFromContext': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="AUTHZ_CONTEXT_INFORMATION_CLASS"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hAuthzClientContext", "InfoClass", "BufferSize", "pSizeRequired", "Buffer"]),
        #
        'AuthzFreeContext': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hAuthzClientContext"]),
        #
        'AuthzInitializeObjectAccessAuditEvent': SimTypeFunction([SimTypeInt(signed=False, label="AUTHZ_INITIALIZE_OBJECT_ACCESS_AUDIT_EVENT_FLAGS"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["Flags", "hAuditEventType", "szOperationType", "szObjectType", "szObjectName", "szAdditionalInfo", "phAuditEvent", "dwAdditionalParameterCount"]),
        #
        'AuthzInitializeObjectAccessAuditEvent2': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["Flags", "hAuditEventType", "szOperationType", "szObjectType", "szObjectName", "szAdditionalInfo", "szAdditionalInfo2", "phAuditEvent", "dwAdditionalParameterCount"]),
        #
        'AuthzFreeAuditEvent': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hAuditEvent"]),
        #
        'AuthzEvaluateSacl': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"DesiredAccess": SimTypeInt(signed=False, label="UInt32"), "PrincipalSelfSid": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "ObjectTypeList": SimTypePointer(SimTypeBottom(label="OBJECT_TYPE_LIST"), offset=0), "ObjectTypeListLength": SimTypeInt(signed=False, label="UInt32"), "OptionalArguments": SimTypePointer(SimTypeBottom(label="Void"), offset=0)}, name="AUTHZ_ACCESS_REQUEST", pack=False, align=None), offset=0), SimTypePointer(SimStruct({"AclRevision": SimTypeChar(label="Byte"), "Sbz1": SimTypeChar(label="Byte"), "AclSize": SimTypeShort(signed=False, label="UInt16"), "AceCount": SimTypeShort(signed=False, label="UInt16"), "Sbz2": SimTypeShort(signed=False, label="UInt16")}, name="ACL", pack=False, align=None), offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["AuthzClientContext", "pRequest", "Sacl", "GrantedAccess", "AccessGranted", "pbGenerateAudit"]),
        #
        'AuthzInstallSecurityEventSource': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"dwFlags": SimTypeInt(signed=False, label="UInt32"), "szEventSourceName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "szEventMessageFile": SimTypePointer(SimTypeChar(label="Char"), offset=0), "szEventSourceXmlSchemaFile": SimTypePointer(SimTypeChar(label="Char"), offset=0), "szEventAccessStringsFile": SimTypePointer(SimTypeChar(label="Char"), offset=0), "szExecutableImagePath": SimTypePointer(SimTypeChar(label="Char"), offset=0), "Anonymous": SimUnion({"pReserved": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "pProviderGuid": SimTypePointer(SimTypeBottom(label="Guid"), offset=0)}, name="<anon>", label="None"), "dwObjectTypeNameCount": SimTypeInt(signed=False, label="UInt32"), "ObjectTypeNames": SimTypePointer(SimStruct({"szObjectTypeName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwOffset": SimTypeInt(signed=False, label="UInt32")}, name="AUTHZ_REGISTRATION_OBJECT_TYPE_NAME_OFFSET", pack=False, align=None), offset=0)}, name="AUTHZ_SOURCE_SCHEMA_REGISTRATION", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["dwFlags", "pRegistration"]),
        #
        'AuthzUninstallSecurityEventSource': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Char"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["dwFlags", "szEventSourceName"]),
        #
        'AuthzEnumerateSecurityEventSources': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"dwFlags": SimTypeInt(signed=False, label="UInt32"), "szEventSourceName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "szEventMessageFile": SimTypePointer(SimTypeChar(label="Char"), offset=0), "szEventSourceXmlSchemaFile": SimTypePointer(SimTypeChar(label="Char"), offset=0), "szEventAccessStringsFile": SimTypePointer(SimTypeChar(label="Char"), offset=0), "szExecutableImagePath": SimTypePointer(SimTypeChar(label="Char"), offset=0), "Anonymous": SimUnion({"pReserved": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "pProviderGuid": SimTypePointer(SimTypeBottom(label="Guid"), offset=0)}, name="<anon>", label="None"), "dwObjectTypeNameCount": SimTypeInt(signed=False, label="UInt32"), "ObjectTypeNames": SimTypePointer(SimStruct({"szObjectTypeName": SimTypePointer(SimTypeChar(label="Char"), offset=0), "dwOffset": SimTypeInt(signed=False, label="UInt32")}, name="AUTHZ_REGISTRATION_OBJECT_TYPE_NAME_OFFSET", pack=False, align=None), offset=0)}, name="AUTHZ_SOURCE_SCHEMA_REGISTRATION", pack=False, align=None), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["dwFlags", "Buffer", "pdwCount", "pdwLength"]),
        #
        'AuthzRegisterSecurityEventSource': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["dwFlags", "szEventSourceName", "phEventProvider"]),
        #
        'AuthzUnregisterSecurityEventSource': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["dwFlags", "phEventProvider"]),
        #
        'AuthzReportSecurityEvent': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=True, label="Int32"), arg_names=["dwFlags", "hEventProvider", "dwAuditId", "pUserSid", "dwCount"]),
        #
        'AuthzReportSecurityEventFromParams': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimStruct({"Length": SimTypeInt(signed=False, label="UInt32"), "Flags": SimTypeInt(signed=False, label="UInt32"), "Count": SimTypeShort(signed=False, label="UInt16"), "Parameters": SimTypePointer(SimStruct({"Type": SimTypeInt(signed=False, label="AUDIT_PARAM_TYPE"), "Length": SimTypeInt(signed=False, label="UInt32"), "Flags": SimTypeInt(signed=False, label="UInt32"), "Anonymous1": SimUnion({"Data0": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "String": SimTypePointer(SimTypeChar(label="Char"), offset=0), "u": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "psid": SimTypePointer(SimTypeBottom(label="SID"), offset=0), "pguid": SimTypePointer(SimTypeBottom(label="Guid"), offset=0), "LogonId_LowPart": SimTypeInt(signed=False, label="UInt32"), "pObjectTypes": SimTypePointer(SimStruct({"Count": SimTypeShort(signed=False, label="UInt16"), "Flags": SimTypeShort(signed=False, label="UInt16"), "pObjectTypes": SimTypePointer(SimStruct({"ObjectType": SimTypeBottom(label="Guid"), "Flags": SimTypeShort(signed=False, label="UInt16"), "Level": SimTypeShort(signed=False, label="UInt16"), "AccessMask": SimTypeInt(signed=False, label="UInt32")}, name="AUDIT_OBJECT_TYPE", pack=False, align=None), offset=0)}, name="AUDIT_OBJECT_TYPES", pack=False, align=None), offset=0), "pIpAddress": SimTypePointer(SimStruct({"pIpAddress": SimTypeFixedSizeArray(SimTypeChar(label="Byte"), 128)}, name="AUDIT_IP_ADDRESS", pack=False, align=None), offset=0)}, name="<anon>", label="None"), "Anonymous2": SimUnion({"Data1": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "LogonId_HighPart": SimTypeInt(signed=True, label="Int32")}, name="<anon>", label="None")}, name="AUDIT_PARAM", pack=False, align=None), offset=0)}, name="AUDIT_PARAMS", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["dwFlags", "hEventProvider", "dwAuditId", "pUserSid", "pParams"]),
        #
        'AuthzRegisterCapChangeNotification': SimTypeFunction([SimTypePointer(SimTypePointer(SimStruct({"unused": SimTypeInt(signed=True, label="Int32")}, name="AUTHZ_CAP_CHANGE_SUBSCRIPTION_HANDLE__", pack=False, align=None), offset=0), offset=0), SimTypePointer(SimTypeFunction([SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=False, label="UInt32"), arg_names=["lpThreadParameter"]), offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["phCapChangeSubscription", "pfnCapChangeCallback", "pCallbackContext"]),
        #
        'AuthzUnregisterCapChangeNotification': SimTypeFunction([SimTypePointer(SimStruct({"unused": SimTypeInt(signed=True, label="Int32")}, name="AUTHZ_CAP_CHANGE_SUBSCRIPTION_HANDLE__", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hCapChangeSubscription"]),
        #
        'AuthzFreeCentralAccessPolicyCache': SimTypeFunction([], SimTypeInt(signed=True, label="Int32")),
    }

lib.set_prototypes(prototypes)