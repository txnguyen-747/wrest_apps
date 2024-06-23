import argparse
import logging


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', required=True, type=str, help='Source directory for files to transcribe.')
    parser.add_argument('-d', '--destination-dir', required=True, type=str, help='Destnation directory for transcriobed files.')
    args, unknown = parser.parse_known_args()
    return args

def main(args):
    logger = logging.getLogger('transcription_file_observer')
    print(f'{args}')

if __name__ == '__main__':
    args = parse_arguments()
    main(args)
    