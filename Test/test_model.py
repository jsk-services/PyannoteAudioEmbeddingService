import datetime
import os
import grpc
import AudioIdentificationService_pb2 as Messages
import AudioIdentificationService_pb2_grpc as Services


if __name__ == "__main__":
    with open("test.wav", "rb") as file:
        audio = file.read()

    timestamp = datetime.datetime.now()

    with grpc.insecure_channel('localhost:50001') as channel:
        stub = Services.AudioIdentificationServiceStub(channel)
        response = stub.Identify(Messages.AudioIdentificationRequest(Audio=audio))

        print(f"Time taken: {(datetime.datetime.now() - timestamp).microseconds / 1000} ms")

        pass