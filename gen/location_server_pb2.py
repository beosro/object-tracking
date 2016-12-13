# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: location_server.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='location_server.proto',
    package='object_tracking',
    syntax='proto3',
    serialized_pb=_b(
        '\n\x15location_server.proto\x12\x0fobject_tracking\"\x1a\n\nClientInfo\x12\x0c\n\x04info\x18\x01 \x01(\t\"\x1a\n\nServerInfo\x12\x0c\n\x04info\x18\x01 \x01(\t\"?\n\x08Location\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\r\n\x05width\x18\x03 \x01(\x05\x12\x0e\n\x06height\x18\x04 \x01(\x05\"\x07\n\x05\x45mpty2\xa1\x01\n\x0eLocationServer\x12\x46\n\x08Register\x12\x1b.object_tracking.ClientInfo\x1a\x1b.object_tracking.ServerInfo\"\x00\x12G\n\x0eReportLocation\x12\x19.object_tracking.Location\x1a\x16.object_tracking.Empty\"\x00(\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_CLIENTINFO = _descriptor.Descriptor(
    name='ClientInfo',
    full_name='object_tracking.ClientInfo',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='info', full_name='object_tracking.ClientInfo.info', index=0,
            number=1, type=9, cpp_type=9, label=1,
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
    serialized_start=42,
    serialized_end=68,
)

_SERVERINFO = _descriptor.Descriptor(
    name='ServerInfo',
    full_name='object_tracking.ServerInfo',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='info', full_name='object_tracking.ServerInfo.info', index=0,
            number=1, type=9, cpp_type=9, label=1,
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
    serialized_start=70,
    serialized_end=96,
)

_LOCATION = _descriptor.Descriptor(
    name='Location',
    full_name='object_tracking.Location',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='x', full_name='object_tracking.Location.x', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='y', full_name='object_tracking.Location.y', index=1,
            number=2, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='width', full_name='object_tracking.Location.width', index=2,
            number=3, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='height', full_name='object_tracking.Location.height', index=3,
            number=4, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
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
    serialized_start=98,
    serialized_end=161,
)

_EMPTY = _descriptor.Descriptor(
    name='Empty',
    full_name='object_tracking.Empty',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
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
    serialized_start=163,
    serialized_end=170,
)

DESCRIPTOR.message_types_by_name['ClientInfo'] = _CLIENTINFO
DESCRIPTOR.message_types_by_name['ServerInfo'] = _SERVERINFO
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY

ClientInfo = _reflection.GeneratedProtocolMessageType('ClientInfo', (_message.Message,), dict(
    DESCRIPTOR=_CLIENTINFO,
    __module__='location_server_pb2'
    # @@protoc_insertion_point(class_scope:object_tracking.ClientInfo)
))
_sym_db.RegisterMessage(ClientInfo)

ServerInfo = _reflection.GeneratedProtocolMessageType('ServerInfo', (_message.Message,), dict(
    DESCRIPTOR=_SERVERINFO,
    __module__='location_server_pb2'
    # @@protoc_insertion_point(class_scope:object_tracking.ServerInfo)
))
_sym_db.RegisterMessage(ServerInfo)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), dict(
    DESCRIPTOR=_LOCATION,
    __module__='location_server_pb2'
    # @@protoc_insertion_point(class_scope:object_tracking.Location)
))
_sym_db.RegisterMessage(Location)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
    DESCRIPTOR=_EMPTY,
    __module__='location_server_pb2'
    # @@protoc_insertion_point(class_scope:object_tracking.Empty)
))
_sym_db.RegisterMessage(Empty)

try:
    # THESE ELEMENTS WILL BE DEPRECATED.
    # Please use the generated *_pb2_grpc.py files instead.
    import grpc
    from grpc.framework.common import cardinality
    from grpc.framework.interfaces.face import utilities as face_utilities
    from grpc.beta import implementations as beta_implementations
    from grpc.beta import interfaces as beta_interfaces


    class LocationServerStub(object):

        def __init__(self, channel):
            """Constructor.

            Args:
              channel: A grpc.Channel.
            """
            self.Register = channel.unary_unary(
                '/object_tracking.LocationServer/Register',
                request_serializer=ClientInfo.SerializeToString,
                response_deserializer=ServerInfo.FromString,
            )
            self.ReportLocation = channel.stream_unary(
                '/object_tracking.LocationServer/ReportLocation',
                request_serializer=Location.SerializeToString,
                response_deserializer=Empty.FromString,
            )


    class LocationServerServicer(object):

        def Register(self, request, context):
            context.set_code(grpc.StatusCode.UNIMPLEMENTED)
            context.set_details('Method not implemented!')
            raise NotImplementedError('Method not implemented!')

        def ReportLocation(self, request_iterator, context):
            context.set_code(grpc.StatusCode.UNIMPLEMENTED)
            context.set_details('Method not implemented!')
            raise NotImplementedError('Method not implemented!')


    def add_LocationServerServicer_to_server(servicer, server):
        rpc_method_handlers = {
            'Register': grpc.unary_unary_rpc_method_handler(
                servicer.Register,
                request_deserializer=ClientInfo.FromString,
                response_serializer=ServerInfo.SerializeToString,
            ),
            'ReportLocation': grpc.stream_unary_rpc_method_handler(
                servicer.ReportLocation,
                request_deserializer=Location.FromString,
                response_serializer=Empty.SerializeToString,
            ),
        }
        generic_handler = grpc.method_handlers_generic_handler(
            'object_tracking.LocationServer', rpc_method_handlers)
        server.add_generic_rpc_handlers((generic_handler,))


    class BetaLocationServerServicer(object):
        """The Beta API is deprecated for 0.15.0 and later.

        It is recommended to use the GA API (classes and functions in this
        file not marked beta) for all further purposes. This class was generated
        only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""

        def Register(self, request, context):
            context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)

        def ReportLocation(self, request_iterator, context):
            context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


    class BetaLocationServerStub(object):
        """The Beta API is deprecated for 0.15.0 and later.

        It is recommended to use the GA API (classes and functions in this
        file not marked beta) for all further purposes. This class was generated
        only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""

        def Register(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
            raise NotImplementedError()

        Register.future = None

        def ReportLocation(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
            raise NotImplementedError()

        ReportLocation.future = None


    def beta_create_LocationServer_server(servicer, pool=None, pool_size=None, default_timeout=None,
                                          maximum_timeout=None):
        """The Beta API is deprecated for 0.15.0 and later.

        It is recommended to use the GA API (classes and functions in this
        file not marked beta) for all further purposes. This function was
        generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
        request_deserializers = {
            ('object_tracking.LocationServer', 'Register'): ClientInfo.FromString,
            ('object_tracking.LocationServer', 'ReportLocation'): Location.FromString,
        }
        response_serializers = {
            ('object_tracking.LocationServer', 'Register'): ServerInfo.SerializeToString,
            ('object_tracking.LocationServer', 'ReportLocation'): Empty.SerializeToString,
        }
        method_implementations = {
            ('object_tracking.LocationServer', 'Register'): face_utilities.unary_unary_inline(servicer.Register),
            ('object_tracking.LocationServer', 'ReportLocation'): face_utilities.stream_unary_inline(
                servicer.ReportLocation),
        }
        server_options = beta_implementations.server_options(request_deserializers=request_deserializers,
                                                             response_serializers=response_serializers,
                                                             thread_pool=pool, thread_pool_size=pool_size,
                                                             default_timeout=default_timeout,
                                                             maximum_timeout=maximum_timeout)
        return beta_implementations.server(method_implementations, options=server_options)


    def beta_create_LocationServer_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
        """The Beta API is deprecated for 0.15.0 and later.

        It is recommended to use the GA API (classes and functions in this
        file not marked beta) for all further purposes. This function was
        generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
        request_serializers = {
            ('object_tracking.LocationServer', 'Register'): ClientInfo.SerializeToString,
            ('object_tracking.LocationServer', 'ReportLocation'): Location.SerializeToString,
        }
        response_deserializers = {
            ('object_tracking.LocationServer', 'Register'): ServerInfo.FromString,
            ('object_tracking.LocationServer', 'ReportLocation'): Empty.FromString,
        }
        cardinalities = {
            'Register': cardinality.Cardinality.UNARY_UNARY,
            'ReportLocation': cardinality.Cardinality.STREAM_UNARY,
        }
        stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer,
                                                         request_serializers=request_serializers,
                                                         response_deserializers=response_deserializers,
                                                         thread_pool=pool, thread_pool_size=pool_size)
        return beta_implementations.dynamic_stub(channel, 'object_tracking.LocationServer', cardinalities,
                                                 options=stub_options)
except ImportError:
    pass
# @@protoc_insertion_point(module_scope)
