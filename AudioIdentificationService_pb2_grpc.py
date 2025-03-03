# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import AudioIdentificationService_pb2 as AudioIdentificationService__pb2

GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in AudioIdentificationService_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class AudioIdentificationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Identify = channel.unary_unary(
                '/jsk.services.AudioIdentificationService/Identify',
                request_serializer=AudioIdentificationService__pb2.AudioIdentificationRequest.SerializeToString,
                response_deserializer=AudioIdentificationService__pb2.AudioIdentificationResponse.FromString,
                _registered_method=True)


class AudioIdentificationServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Identify(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AudioIdentificationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Identify': grpc.unary_unary_rpc_method_handler(
                    servicer.Identify,
                    request_deserializer=AudioIdentificationService__pb2.AudioIdentificationRequest.FromString,
                    response_serializer=AudioIdentificationService__pb2.AudioIdentificationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'jsk.services.AudioIdentificationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('jsk.services.AudioIdentificationService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class AudioIdentificationService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Identify(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/jsk.services.AudioIdentificationService/Identify',
            AudioIdentificationService__pb2.AudioIdentificationRequest.SerializeToString,
            AudioIdentificationService__pb2.AudioIdentificationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
