# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/util/memmapped_file_system.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/util/memmapped_file_system.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_pb=_b('\n0tensorflow/core/util/memmapped_file_system.proto\x12\ntensorflow\"C\n#MemmappedFileSystemDirectoryElement\x12\x0e\n\x06offset\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\"`\n\x1cMemmappedFileSystemDirectory\x12@\n\x07\x65lement\x18\x01 \x03(\x0b\x32/.tensorflow.MemmappedFileSystemDirectoryElementB\x03\xf8\x01\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MEMMAPPEDFILESYSTEMDIRECTORYELEMENT = _descriptor.Descriptor(
  name='MemmappedFileSystemDirectoryElement',
  full_name='tensorflow.MemmappedFileSystemDirectoryElement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='offset', full_name='tensorflow.MemmappedFileSystemDirectoryElement.offset', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.MemmappedFileSystemDirectoryElement.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=131,
)


_MEMMAPPEDFILESYSTEMDIRECTORY = _descriptor.Descriptor(
  name='MemmappedFileSystemDirectory',
  full_name='tensorflow.MemmappedFileSystemDirectory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='element', full_name='tensorflow.MemmappedFileSystemDirectory.element', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=133,
  serialized_end=229,
)

_MEMMAPPEDFILESYSTEMDIRECTORY.fields_by_name['element'].message_type = _MEMMAPPEDFILESYSTEMDIRECTORYELEMENT
DESCRIPTOR.message_types_by_name['MemmappedFileSystemDirectoryElement'] = _MEMMAPPEDFILESYSTEMDIRECTORYELEMENT
DESCRIPTOR.message_types_by_name['MemmappedFileSystemDirectory'] = _MEMMAPPEDFILESYSTEMDIRECTORY

MemmappedFileSystemDirectoryElement = _reflection.GeneratedProtocolMessageType('MemmappedFileSystemDirectoryElement', (_message.Message,), dict(
  DESCRIPTOR = _MEMMAPPEDFILESYSTEMDIRECTORYELEMENT,
  __module__ = 'tensorflow.core.util.memmapped_file_system_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.MemmappedFileSystemDirectoryElement)
  ))
_sym_db.RegisterMessage(MemmappedFileSystemDirectoryElement)

MemmappedFileSystemDirectory = _reflection.GeneratedProtocolMessageType('MemmappedFileSystemDirectory', (_message.Message,), dict(
  DESCRIPTOR = _MEMMAPPEDFILESYSTEMDIRECTORY,
  __module__ = 'tensorflow.core.util.memmapped_file_system_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.MemmappedFileSystemDirectory)
  ))
_sym_db.RegisterMessage(MemmappedFileSystemDirectory)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\370\001\001'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
