# Sleep Sound

A sleep sound application that plays random audio files during specified time periods with configurable intervals.

## Quick Start

See [QUICKSTART.md](QUICKSTART.md) for immediate usage instructions.

## Documentation

- [Quick Start Guide](QUICKSTART.md) - Get started quickly
- [Go Version README](README_GO.md) - Detailed user guide
- [Migration Guide](MIGRATION.md) - Python to Go migration details
- [Refactoring Summary](REFACTORING_SUMMARY.md) - Complete refactoring overview

## Building

```bash
# Windows
.\BUILD_go.bat

# Linux/Mac
chmod +x build_go.sh
./build_go.sh
```

## Usage

```bash
# Run with defaults
./sleep-sound

# Verbose mode
./sleep-sound -v

# Debug/testing mode
./sleep-sound -i -v -p

# Force mode (ignore time restrictions)
./sleep-sound -f
```

See [QUICKSTART.md](QUICKSTART.md) for all available options and examples.
