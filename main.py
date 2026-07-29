from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path
from typing import Sequence


def _reports_dir() -> Path:
    """Return the configured reports directory.

    Import is deferred to avoid heavy module-level imports until a
    command is actually executed.
    """
    from brain.infrastructure.config import settings

    return settings.runtime.report_dir


def _default_report_path(audio_path: str | Path, suffix: str = "") -> Path:
    audio_name = Path(audio_path).stem
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = _reports_dir()
    output_dir.mkdir(parents=True, exist_ok=True)
    suffix = f"_{suffix}" if suffix else ""
    return output_dir / f"{timestamp}_{audio_name}{suffix}.json"


def _cmd_analyze(args: argparse.Namespace) -> int:
    """Run the deterministic V1 audio review flow through SoundBrainService."""
    from brain.application.soundbrain_service import (
        AnalysisRequest,
        SoundBrainService,
    )

    if args.output is None:
        args.output = _default_report_path(args.audio_path)

    request = AnalysisRequest(
        audio_path=args.audio_path,
        intent=args.summary,
        delivery_target=args.target,
        include_reasoning=args.semantic,
        include_rag=False,
        output_path=args.output,
    )

    service = SoundBrainService()
    try:
        result = service.analyze(request)
    except Exception as exc:
        print(f"Analysis failed: {exc}", file=sys.stderr)
        return 1

    print(f"Report saved to: {args.output}")
    return 0


def _cmd_reference(args: argparse.Namespace) -> int:
    """Compare a reference audio file against the current mix."""
    from brain.application.soundbrain_service import (
        AnalysisRequest,
        SoundBrainService,
    )

    if args.output is None:
        args.output = _default_report_path(args.current, suffix="reference")

    request = AnalysisRequest(
        audio_path=args.current,
        reference_path=args.reference,
        output_path=args.output,
    )

    service = SoundBrainService()
    try:
        service.analyze(request)
    except Exception as exc:
        print(f"Reference comparison failed: {exc}", file=sys.stderr)
        return 1

    print(f"Reference report saved to: {args.output}")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="soundbrain",
        description="SoundBrain — AI-powered Audio Intelligence Platform",
    )
    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
        help="Available commands",
    )

    analyze_parser = subparsers.add_parser(
        "analyze",
        help="Analyze an audio file and produce a deterministic engineering report.",
    )
    analyze_parser.add_argument(
        "audio_path",
        help="Path to the audio file to analyze.",
    )
    analyze_parser.add_argument(
        "--output",
        "-o",
        dest="output",
        help="Output report path (default: reports/<timestamp>_<filename>.json).",
    )
    analyze_parser.add_argument(
        "--semantic",
        action="store_true",
        help="Include semantic analysis using CLAP embeddings (requires the CLAP model).",
    )
    analyze_parser.add_argument(
        "--summary",
        default="",
        help="Optional human-provided summary context included in the report.",
    )
    analyze_parser.add_argument(
        "--target",
        default="",
        help="Optional delivery target (e.g. streaming, club, vinyl) included in the report.",
    )

    reference_parser = subparsers.add_parser(
        "reference",
        help="Compare a reference audio file against the current mix.",
    )
    reference_parser.add_argument(
        "reference",
        help="Path to the reference audio file.",
    )
    reference_parser.add_argument(
        "current",
        help="Path to the current/mix audio file.",
    )
    reference_parser.add_argument(
        "--output",
        "-o",
        dest="output",
        help="Output report path (default: reports/<timestamp>_reference.json).",
    )

    args = parser.parse_args(argv)

    if args.command == "analyze":
        return _cmd_analyze(args)
    if args.command == "reference":
        return _cmd_reference(args)

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
