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
lib.set_library_names("oleacc.dll")
prototypes = \
    {
        #
        'LresultFromObject': SimTypeFunction([SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeBottom(label="IUnknown")], SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), arg_names=["riid", "wParam", "punk"]),
        #
        'ObjectFromLresult': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["lResult", "riid", "wParam", "ppvObject"]),
        #
        'WindowFromAccessibleObject': SimTypeFunction([SimTypeBottom(label="IAccessible"), SimTypePointer(SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["param0", "phwnd"]),
        #
        'AccessibleObjectFromWindow': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hwnd", "dwId", "riid", "ppvObject"]),
        #
        'AccessibleObjectFromEvent': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeBottom(label="IAccessible"), offset=0), SimTypePointer(SimStruct({"Anonymous": SimUnion({"Anonymous": SimStruct({"vt": SimTypeShort(signed=False, label="UInt16"), "wReserved1": SimTypeShort(signed=False, label="UInt16"), "wReserved2": SimTypeShort(signed=False, label="UInt16"), "wReserved3": SimTypeShort(signed=False, label="UInt16"), "Anonymous": SimUnion({"llVal": SimTypeLongLong(signed=True, label="Int64"), "lVal": SimTypeInt(signed=True, label="Int32"), "bVal": SimTypeChar(label="Byte"), "iVal": SimTypeShort(signed=True, label="Int16"), "fltVal": SimTypeFloat(size=32), "dblVal": SimTypeFloat(size=64), "boolVal": SimTypeShort(signed=True, label="Int16"), "__OBSOLETE__VARIANT_BOOL": SimTypeShort(signed=True, label="Int16"), "scode": SimTypeInt(signed=True, label="Int32"), "cyVal": SimTypeBottom(label="CY"), "date": SimTypeFloat(size=64), "bstrVal": SimTypePointer(SimTypeChar(label="Char"), offset=0), "punkVal": SimTypeBottom(label="IUnknown"), "pdispVal": SimTypeBottom(label="IDispatch"), "parray": SimTypePointer(SimStruct({"cDims": SimTypeShort(signed=False, label="UInt16"), "fFeatures": SimTypeShort(signed=False, label="UInt16"), "cbElements": SimTypeInt(signed=False, label="UInt32"), "cLocks": SimTypeInt(signed=False, label="UInt32"), "pvData": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "rgsabound": SimTypePointer(SimStruct({"cElements": SimTypeInt(signed=False, label="UInt32"), "lLbound": SimTypeInt(signed=True, label="Int32")}, name="SAFEARRAYBOUND", pack=False, align=None), offset=0)}, name="SAFEARRAY", pack=False, align=None), offset=0), "pbVal": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "piVal": SimTypePointer(SimTypeShort(signed=True, label="Int16"), offset=0), "plVal": SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0), "pllVal": SimTypePointer(SimTypeLongLong(signed=True, label="Int64"), offset=0), "pfltVal": SimTypePointer(SimTypeFloat(size=32), offset=0), "pdblVal": SimTypePointer(SimTypeFloat(size=64), offset=0), "pboolVal": SimTypePointer(SimTypeShort(signed=True, label="Int16"), offset=0), "__OBSOLETE__VARIANT_PBOOL": SimTypePointer(SimTypeShort(signed=True, label="Int16"), offset=0), "pscode": SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0), "pcyVal": SimTypePointer(SimTypeBottom(label="CY"), offset=0), "pdate": SimTypePointer(SimTypeFloat(size=64), offset=0), "pbstrVal": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), "ppunkVal": SimTypePointer(SimTypeBottom(label="IUnknown"), offset=0), "ppdispVal": SimTypePointer(SimTypeBottom(label="IDispatch"), offset=0), "pparray": SimTypePointer(SimTypePointer(SimStruct({"cDims": SimTypeShort(signed=False, label="UInt16"), "fFeatures": SimTypeShort(signed=False, label="UInt16"), "cbElements": SimTypeInt(signed=False, label="UInt32"), "cLocks": SimTypeInt(signed=False, label="UInt32"), "pvData": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "rgsabound": SimTypePointer(SimStruct({"cElements": SimTypeInt(signed=False, label="UInt32"), "lLbound": SimTypeInt(signed=True, label="Int32")}, name="SAFEARRAYBOUND", pack=False, align=None), offset=0)}, name="SAFEARRAY", pack=False, align=None), offset=0), offset=0), "pvarVal": SimTypePointer(SimTypeBottom(label="VARIANT"), offset=0), "byref": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "cVal": SimTypeBottom(label="CHAR"), "uiVal": SimTypeShort(signed=False, label="UInt16"), "ulVal": SimTypeInt(signed=False, label="UInt32"), "ullVal": SimTypeLongLong(signed=False, label="UInt64"), "intVal": SimTypeInt(signed=True, label="Int32"), "uintVal": SimTypeInt(signed=False, label="UInt32"), "pdecVal": SimTypePointer(SimTypeBottom(label="DECIMAL"), offset=0), "pcVal": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "puiVal": SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), "pulVal": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), "pullVal": SimTypePointer(SimTypeLongLong(signed=False, label="UInt64"), offset=0), "pintVal": SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0), "puintVal": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), "Anonymous": SimStruct({"pvRecord": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "pRecInfo": SimTypeBottom(label="IRecordInfo")}, name="_Anonymous_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="_Anonymous_e__Struct", pack=False, align=None), "decVal": SimTypeBottom(label="DECIMAL")}, name="<anon>", label="None")}, name="VARIANT", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hwnd", "dwId", "dwChildId", "ppacc", "pvarChild"]),
        #
        'AccessibleObjectFromPoint': SimTypeFunction([SimStruct({"x": SimTypeInt(signed=True, label="Int32"), "y": SimTypeInt(signed=True, label="Int32")}, name="POINT", pack=False, align=None), SimTypePointer(SimTypeBottom(label="IAccessible"), offset=0), SimTypePointer(SimStruct({"Anonymous": SimUnion({"Anonymous": SimStruct({"vt": SimTypeShort(signed=False, label="UInt16"), "wReserved1": SimTypeShort(signed=False, label="UInt16"), "wReserved2": SimTypeShort(signed=False, label="UInt16"), "wReserved3": SimTypeShort(signed=False, label="UInt16"), "Anonymous": SimUnion({"llVal": SimTypeLongLong(signed=True, label="Int64"), "lVal": SimTypeInt(signed=True, label="Int32"), "bVal": SimTypeChar(label="Byte"), "iVal": SimTypeShort(signed=True, label="Int16"), "fltVal": SimTypeFloat(size=32), "dblVal": SimTypeFloat(size=64), "boolVal": SimTypeShort(signed=True, label="Int16"), "__OBSOLETE__VARIANT_BOOL": SimTypeShort(signed=True, label="Int16"), "scode": SimTypeInt(signed=True, label="Int32"), "cyVal": SimTypeBottom(label="CY"), "date": SimTypeFloat(size=64), "bstrVal": SimTypePointer(SimTypeChar(label="Char"), offset=0), "punkVal": SimTypeBottom(label="IUnknown"), "pdispVal": SimTypeBottom(label="IDispatch"), "parray": SimTypePointer(SimStruct({"cDims": SimTypeShort(signed=False, label="UInt16"), "fFeatures": SimTypeShort(signed=False, label="UInt16"), "cbElements": SimTypeInt(signed=False, label="UInt32"), "cLocks": SimTypeInt(signed=False, label="UInt32"), "pvData": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "rgsabound": SimTypePointer(SimStruct({"cElements": SimTypeInt(signed=False, label="UInt32"), "lLbound": SimTypeInt(signed=True, label="Int32")}, name="SAFEARRAYBOUND", pack=False, align=None), offset=0)}, name="SAFEARRAY", pack=False, align=None), offset=0), "pbVal": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "piVal": SimTypePointer(SimTypeShort(signed=True, label="Int16"), offset=0), "plVal": SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0), "pllVal": SimTypePointer(SimTypeLongLong(signed=True, label="Int64"), offset=0), "pfltVal": SimTypePointer(SimTypeFloat(size=32), offset=0), "pdblVal": SimTypePointer(SimTypeFloat(size=64), offset=0), "pboolVal": SimTypePointer(SimTypeShort(signed=True, label="Int16"), offset=0), "__OBSOLETE__VARIANT_PBOOL": SimTypePointer(SimTypeShort(signed=True, label="Int16"), offset=0), "pscode": SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0), "pcyVal": SimTypePointer(SimTypeBottom(label="CY"), offset=0), "pdate": SimTypePointer(SimTypeFloat(size=64), offset=0), "pbstrVal": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), "ppunkVal": SimTypePointer(SimTypeBottom(label="IUnknown"), offset=0), "ppdispVal": SimTypePointer(SimTypeBottom(label="IDispatch"), offset=0), "pparray": SimTypePointer(SimTypePointer(SimStruct({"cDims": SimTypeShort(signed=False, label="UInt16"), "fFeatures": SimTypeShort(signed=False, label="UInt16"), "cbElements": SimTypeInt(signed=False, label="UInt32"), "cLocks": SimTypeInt(signed=False, label="UInt32"), "pvData": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "rgsabound": SimTypePointer(SimStruct({"cElements": SimTypeInt(signed=False, label="UInt32"), "lLbound": SimTypeInt(signed=True, label="Int32")}, name="SAFEARRAYBOUND", pack=False, align=None), offset=0)}, name="SAFEARRAY", pack=False, align=None), offset=0), offset=0), "pvarVal": SimTypePointer(SimTypeBottom(label="VARIANT"), offset=0), "byref": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "cVal": SimTypeBottom(label="CHAR"), "uiVal": SimTypeShort(signed=False, label="UInt16"), "ulVal": SimTypeInt(signed=False, label="UInt32"), "ullVal": SimTypeLongLong(signed=False, label="UInt64"), "intVal": SimTypeInt(signed=True, label="Int32"), "uintVal": SimTypeInt(signed=False, label="UInt32"), "pdecVal": SimTypePointer(SimTypeBottom(label="DECIMAL"), offset=0), "pcVal": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "puiVal": SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), "pulVal": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), "pullVal": SimTypePointer(SimTypeLongLong(signed=False, label="UInt64"), offset=0), "pintVal": SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0), "puintVal": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), "Anonymous": SimStruct({"pvRecord": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "pRecInfo": SimTypeBottom(label="IRecordInfo")}, name="_Anonymous_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="_Anonymous_e__Struct", pack=False, align=None), "decVal": SimTypeBottom(label="DECIMAL")}, name="<anon>", label="None")}, name="VARIANT", pack=False, align=None), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["ptScreen", "ppacc", "pvarChild"]),
        #
        'AccessibleChildren': SimTypeFunction([SimTypeBottom(label="IAccessible"), SimTypeInt(signed=True, label="Int32"), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimStruct({"Anonymous": SimUnion({"Anonymous": SimStruct({"vt": SimTypeShort(signed=False, label="UInt16"), "wReserved1": SimTypeShort(signed=False, label="UInt16"), "wReserved2": SimTypeShort(signed=False, label="UInt16"), "wReserved3": SimTypeShort(signed=False, label="UInt16"), "Anonymous": SimUnion({"llVal": SimTypeLongLong(signed=True, label="Int64"), "lVal": SimTypeInt(signed=True, label="Int32"), "bVal": SimTypeChar(label="Byte"), "iVal": SimTypeShort(signed=True, label="Int16"), "fltVal": SimTypeFloat(size=32), "dblVal": SimTypeFloat(size=64), "boolVal": SimTypeShort(signed=True, label="Int16"), "__OBSOLETE__VARIANT_BOOL": SimTypeShort(signed=True, label="Int16"), "scode": SimTypeInt(signed=True, label="Int32"), "cyVal": SimTypeBottom(label="CY"), "date": SimTypeFloat(size=64), "bstrVal": SimTypePointer(SimTypeChar(label="Char"), offset=0), "punkVal": SimTypeBottom(label="IUnknown"), "pdispVal": SimTypeBottom(label="IDispatch"), "parray": SimTypePointer(SimStruct({"cDims": SimTypeShort(signed=False, label="UInt16"), "fFeatures": SimTypeShort(signed=False, label="UInt16"), "cbElements": SimTypeInt(signed=False, label="UInt32"), "cLocks": SimTypeInt(signed=False, label="UInt32"), "pvData": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "rgsabound": SimTypePointer(SimStruct({"cElements": SimTypeInt(signed=False, label="UInt32"), "lLbound": SimTypeInt(signed=True, label="Int32")}, name="SAFEARRAYBOUND", pack=False, align=None), offset=0)}, name="SAFEARRAY", pack=False, align=None), offset=0), "pbVal": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "piVal": SimTypePointer(SimTypeShort(signed=True, label="Int16"), offset=0), "plVal": SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0), "pllVal": SimTypePointer(SimTypeLongLong(signed=True, label="Int64"), offset=0), "pfltVal": SimTypePointer(SimTypeFloat(size=32), offset=0), "pdblVal": SimTypePointer(SimTypeFloat(size=64), offset=0), "pboolVal": SimTypePointer(SimTypeShort(signed=True, label="Int16"), offset=0), "__OBSOLETE__VARIANT_PBOOL": SimTypePointer(SimTypeShort(signed=True, label="Int16"), offset=0), "pscode": SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0), "pcyVal": SimTypePointer(SimTypeBottom(label="CY"), offset=0), "pdate": SimTypePointer(SimTypeFloat(size=64), offset=0), "pbstrVal": SimTypePointer(SimTypePointer(SimTypeChar(label="Char"), offset=0), offset=0), "ppunkVal": SimTypePointer(SimTypeBottom(label="IUnknown"), offset=0), "ppdispVal": SimTypePointer(SimTypeBottom(label="IDispatch"), offset=0), "pparray": SimTypePointer(SimTypePointer(SimStruct({"cDims": SimTypeShort(signed=False, label="UInt16"), "fFeatures": SimTypeShort(signed=False, label="UInt16"), "cbElements": SimTypeInt(signed=False, label="UInt32"), "cLocks": SimTypeInt(signed=False, label="UInt32"), "pvData": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "rgsabound": SimTypePointer(SimStruct({"cElements": SimTypeInt(signed=False, label="UInt32"), "lLbound": SimTypeInt(signed=True, label="Int32")}, name="SAFEARRAYBOUND", pack=False, align=None), offset=0)}, name="SAFEARRAY", pack=False, align=None), offset=0), offset=0), "pvarVal": SimTypePointer(SimTypeBottom(label="VARIANT"), offset=0), "byref": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "cVal": SimTypeBottom(label="CHAR"), "uiVal": SimTypeShort(signed=False, label="UInt16"), "ulVal": SimTypeInt(signed=False, label="UInt32"), "ullVal": SimTypeLongLong(signed=False, label="UInt64"), "intVal": SimTypeInt(signed=True, label="Int32"), "uintVal": SimTypeInt(signed=False, label="UInt32"), "pdecVal": SimTypePointer(SimTypeBottom(label="DECIMAL"), offset=0), "pcVal": SimTypePointer(SimTypeChar(label="Byte"), offset=0), "puiVal": SimTypePointer(SimTypeShort(signed=False, label="UInt16"), offset=0), "pulVal": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), "pullVal": SimTypePointer(SimTypeLongLong(signed=False, label="UInt64"), offset=0), "pintVal": SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0), "puintVal": SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), "Anonymous": SimStruct({"pvRecord": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "pRecInfo": SimTypeBottom(label="IRecordInfo")}, name="_Anonymous_e__Struct", pack=False, align=None)}, name="<anon>", label="None")}, name="_Anonymous_e__Struct", pack=False, align=None), "decVal": SimTypeBottom(label="DECIMAL")}, name="<anon>", label="None")}, name="VARIANT", pack=False, align=None), label="LPArray", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int32"), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["paccContainer", "iChildStart", "cChildren", "rgvarChildren", "pcObtained"]),
        #
        'GetRoleTextA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["lRole", "lpszRole", "cchRoleMax"]),
        #
        'GetRoleTextW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["lRole", "lpszRole", "cchRoleMax"]),
        #
        'GetStateTextA': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Byte"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["lStateBit", "lpszState", "cchState"]),
        #
        'GetStateTextW': SimTypeFunction([SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimTypeChar(label="Char"), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypeInt(signed=False, label="UInt32"), arg_names=["lStateBit", "lpszState", "cchState"]),
        #
        'GetOleaccVersionInfo': SimTypeFunction([SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt32"), offset=0)], SimTypeBottom(label="Void"), arg_names=["pVer", "pBuild"]),
        #
        'CreateStdAccessibleObject': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hwnd", "idObject", "riid", "ppvObject"]),
        #
        'CreateStdAccessibleProxyA': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Byte"), offset=0), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hwnd", "pClassName", "idObject", "riid", "ppvObject"]),
        #
        'CreateStdAccessibleProxyW': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeChar(label="Char"), offset=0), SimTypeInt(signed=True, label="Int32"), SimTypePointer(SimTypeBottom(label="Guid"), offset=0), SimTypePointer(SimTypePointer(SimTypeBottom(label="Void"), offset=0), offset=0)], SimTypeInt(signed=True, label="Int32"), arg_names=["hwnd", "pClassName", "idObject", "riid", "ppvObject"]),
        #
        'AccSetRunningUtilityState': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypeInt(signed=False, label="UInt32"), SimTypeInt(signed=False, label="ACC_UTILITY_STATE_FLAGS")], SimTypeInt(signed=True, label="Int32"), arg_names=["hwndApp", "dwUtilityStateMask", "dwUtilityState"]),
        #
        'AccNotifyTouchInteraction': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimStruct({"x": SimTypeInt(signed=True, label="Int32"), "y": SimTypeInt(signed=True, label="Int32")}, name="POINT", pack=False, align=None)], SimTypeInt(signed=True, label="Int32"), arg_names=["hwndApp", "hwndTarget", "ptTarget"]),
    }

lib.set_prototypes(prototypes)
