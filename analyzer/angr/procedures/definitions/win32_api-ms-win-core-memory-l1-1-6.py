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
lib.set_library_names("api-ms-win-core-memory-l1-1-6.dll")
prototypes = \
    {
        #
        'VirtualAlloc2': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="VIRTUAL_ALLOCATION_TYPE"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"Anonymous1": SimStruct({"_bitfield": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous1_e__Struct", pack=False, align=None), "Anonymous2": SimUnion({"ULong64": SimTypeLongLong(signed=False, label="UInt64"), "Pointer": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "Size": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "Handle": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "ULong": SimTypeInt(signed=False, label="UInt32")}, name="<anon>", label="None")}, name="MEM_EXTENDED_PARAMETER", pack=False, align=None), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypePointer(SimTypeBottom(label="Void"), offset=0), arg_names=["Process", "BaseAddress", "Size", "AllocationType", "PageProtection", "ExtendedParameters", "ParameterCount"]),
        #
        'MapViewOfFile3': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeLongLong(signed=False, label="UInt64"), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="VIRTUAL_ALLOCATION_TYPE"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"Anonymous1": SimStruct({"_bitfield": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous1_e__Struct", pack=False, align=None), "Anonymous2": SimUnion({"ULong64": SimTypeLongLong(signed=False, label="UInt64"), "Pointer": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "Size": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "Handle": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "ULong": SimTypeInt(signed=False, label="UInt32")}, name="<anon>", label="None")}, name="MEM_EXTENDED_PARAMETER", pack=False, align=None), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypePointer(SimTypeBottom(label="Void"), offset=0), arg_names=["FileMapping", "Process", "BaseAddress", "Offset", "ViewSize", "AllocationType", "PageProtection", "ExtendedParameters", "ParameterCount"]),
        #
        'VirtualAlloc2FromApp': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="VIRTUAL_ALLOCATION_TYPE"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"Anonymous1": SimStruct({"_bitfield": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous1_e__Struct", pack=False, align=None), "Anonymous2": SimUnion({"ULong64": SimTypeLongLong(signed=False, label="UInt64"), "Pointer": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "Size": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "Handle": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "ULong": SimTypeInt(signed=False, label="UInt32")}, name="<anon>", label="None")}, name="MEM_EXTENDED_PARAMETER", pack=False, align=None), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypePointer(SimTypeBottom(label="Void"), offset=0), arg_names=["Process", "BaseAddress", "Size", "AllocationType", "PageProtection", "ExtendedParameters", "ParameterCount"]),
        #
        'MapViewOfFile3FromApp': SimTypeFunction([SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), SimTypePointer(SimTypeBottom(label="Void"), offset=0), SimTypeLongLong(signed=False, label="UInt64"), SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), SimTypeInt(signed=False, label="VIRTUAL_ALLOCATION_TYPE"), SimTypeInt(signed=False, label="UInt32"), SimTypePointer(SimStruct({"Anonymous1": SimStruct({"_bitfield": SimTypeLongLong(signed=False, label="UInt64")}, name="_Anonymous1_e__Struct", pack=False, align=None), "Anonymous2": SimUnion({"ULong64": SimTypeLongLong(signed=False, label="UInt64"), "Pointer": SimTypePointer(SimTypeBottom(label="Void"), offset=0), "Size": SimTypePointer(SimTypeInt(signed=False, label="UInt"), label="UIntPtr", offset=0), "Handle": SimTypePointer(SimTypeInt(signed=True, label="Int"), label="IntPtr", offset=0), "ULong": SimTypeInt(signed=False, label="UInt32")}, name="<anon>", label="None")}, name="MEM_EXTENDED_PARAMETER", pack=False, align=None), label="LPArray", offset=0), SimTypeInt(signed=False, label="UInt32")], SimTypePointer(SimTypeBottom(label="Void"), offset=0), arg_names=["FileMapping", "Process", "BaseAddress", "Offset", "ViewSize", "AllocationType", "PageProtection", "ExtendedParameters", "ParameterCount"]),
    }

lib.set_prototypes(prototypes)
