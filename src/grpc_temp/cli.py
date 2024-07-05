# CLI interface for the gRPC server

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='gRPC server')
    parser.add_argument('--host', type=str, default='localhost', help='Host')
    parser.add_argument('--port', type=int, default=50051, help='Port')
    return parser.parse_args()