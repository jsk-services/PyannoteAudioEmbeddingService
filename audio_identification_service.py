import os
from concurrent import futures
from io import BytesIO

import grpc
import AudioIdentificationService_pb2 as Messages
import AudioIdentificationService_pb2_grpc as Services
from pyannote.audio import Model
from pyannote.audio import Inference
import torch


class AudioIdentificationService(Services.AudioIdentificationServiceServicer):

    def __init__(self, inference: Inference):
        self._inference = inference
        pass

    def Identify(self, request: Messages.AudioIdentificationRequest, context):
        embedding = self._inference(BytesIO(request.Audio))
        return Messages.AudioIdentificationResponse(Embedding=embedding)


if __name__ == "__main__":
    port = os.environ.get("PORT", 50000)
    token = os.environ.get("TOKEN", "")
    
    print("Preparing models...")
    
    audio_model = Model.from_pretrained("pyannote/embedding", strict=False, use_auth_token=token)
    audio_inference = Inference(audio_model, window="whole").to(torch.device("cuda"))
    print("Preparing server...")

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Services.add_AudioIdentificationServiceServicer_to_server(
        AudioIdentificationService(audio_inference),
        server)

    print(f"Server address: [::]:{port}")

    server.add_insecure_port(f"[::]:{port}")
    server.start()
    server.wait_for_termination()
    pass