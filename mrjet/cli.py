import argparse
import os

from mrjet.downloader import MovieDownloader
from mrjet.logger import logger


def main():
    parser = argparse.ArgumentParser(
        description="MRJet: A tool for downloading funny videos."
    )

    parser.add_argument("--url", type=str, help="The URL of the video to download.")
    parser.add_argument(
        "--output_dir",
        type=str,
        default=".",
        help="The output directory for the downloaded video.",
    )

    args = parser.parse_args()

    logger.info("Starting MRJet...")
    logger.info(f"URL: {args.url}")
    logger.info(f"Output Directory: {args.output_dir}")

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    downloader = MovieDownloader()

    downloader.download(url=args.url, output_dir=args.output_dir)


if __name__ == "__main__":
    main()
