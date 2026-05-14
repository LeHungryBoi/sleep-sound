# Quick Start Guide - Sleep Sound (Go Version)

## Prerequisites

- Go 1.21 or later (only needed if you want to rebuild from source)
- Audio files in the `music/` directory

## Quick Start

### Option 1: Use Pre-built Binary (Recommended)

The Windows executable is already built and ready to use:

```bash
# Run with default settings
.\sleep-sound.exe

# Run with verbose output to see what's happening
.\sleep-sound.exe -v

# Force sounds for testing (ignores time restrictions)
.\sleep-sound.exe -f -v

# Debug mode with short intervals for quick testing
.\sleep-sound.exe -i -v -p
```

### Option 2: Build from Source

If you want to rebuild or modify the code:

```bash
# Windows
.\BUILD_go.bat

# Linux/Mac
chmod +x build_go.sh
./build_go.sh
```

## Common Use Cases

### 1. Normal Nighttime Use
Plays sounds between 21:38 and 08:32 with 15-30 minute intervals:
```bash
.\sleep-sound.exe
```

### 2. Testing Mode
Quick testing with 1-2 second intervals:
```bash
.\sleep-sound.exe -i -v -p
```

### 3. Custom Time Period
Set your own boom period (e.g., 10 PM to 6 AM):
```bash
.\sleep-sound.exe -b 2200 -o 0600
```

### 4. Force Mode
Play sounds regardless of time:
```bash
.\sleep-sound.exe -f
```

### 5. Adjust Intervals
Custom silent intervals (e.g., 5-10 minutes):
```bash
.\sleep-sound.exe -smin 300 -smax 600
```

## Command-Line Options

| Flag | Description | Example |
|------|-------------|---------|
| `-f` | Force sounds outside boom time | `-f` |
| `-i` | Debug mode (short intervals) | `-i` |
| `-v` | Verbose output | `-v` |
| `-b` | Begin time (HHMM format) | `-b 2200` |
| `-o` | End time (HHMM format) | `-o 0700` |
| `-w` | Don't skip initial sound | `-w` |
| `-p` | Always play (100% probability) | `-p` |
| `-smin` | Min silent interval (seconds) | `-smin 600` |
| `-smax` | Max silent interval (seconds) | `-smax 1200` |
| `-rmin` | Min rhythmic pause (seconds) | `-rmin 0.3` |
| `-rmax` | Max rhythmic pause (seconds) | `-rmax 0.5` |

## Default Settings

- **Music Directory**: `./music/`
- **Boom Time**: 21:38 to 08:32 (next day)
- **Silent Interval**: 900-1800 seconds (15-30 minutes)
- **Rhythmic Pause**: 0.2-0.4 seconds
- **Sound Probability**: 60%

## Troubleshooting

### No sounds playing?
1. Check that you have audio files in the `music/` directory
2. Use `-v` flag to see verbose output
3. Use `-f` flag to bypass time restrictions
4. Use `-i` flag for quick testing

### Wrong audio device?
Edit `player/player.go` and change the aplay device:
```go
// For Linux, change this line:
cmd := exec.Command("aplay", "-D", "plughw:CARD=D1,DEV=0", audioFile)
// To your desired device
```

### Want different default times?
Edit `config/config.go` and modify the `DefaultConfig()` function:
```go
TimeBegin: "2200",  // Change to your preferred start time
TimeOver: "0700",   // Change to your preferred end time
```

## Stopping the Program

Press `Ctrl+C` to stop the program.

## More Information

- See `README_GO.md` for detailed documentation
- See `MIGRATION.md` for Python to Go migration details
- See `REFACTORING_SUMMARY.md` for complete refactoring overview
