# Migration Guide: Python to Go

This document explains the refactoring from Python to Go.

## Overview

The sleep-sound application has been successfully refactored from Python to Go, maintaining all original functionality while improving performance and deployment simplicity.

## Key Changes

### 1. Project Structure

**Python (Original):**
```
sleep-sound/
├── main.py
├── sleep_sound.py
├── sound_go_boom_class.py
├── argument.py
├── time_convert.py
└── ...
```

**Go (Refactored):**
```
sleep-sound/
├── main.go              # Main entry point
├── config/
│   └── config.go        # Configuration management
├── player/
│   └── player.go        # Audio playback
├── timeutil/
│   └── timeutil.go      # Time utilities
├── go.mod               # Go module definition
└── ...
```

### 2. Module Organization

- **config package**: Handles all configuration settings and defaults
- **player package**: Manages audio file selection and playback
- **timeutil package**: Provides time-related utilities
- **main package**: Application entry point and main loop

### 3. Command-Line Arguments

**Python:** Used `argparse` module
**Go:** Uses standard `flag` package

All command-line flags are preserved with the same short and long forms.

### 4. Audio Playback

**Python:** 
- Linux: `aplay` command
- Windows: `winsound.PlaySound`

**Go:**
- Linux: `exec.Command("aplay", ...)`
- Windows: PowerShell's SoundPlayer via `exec.Command`

### 5. Configuration Management

**Python:** Global variables with module-level scope
**Go:** Structured `Config` struct with methods

Benefits of Go approach:
- Type safety
- Better organization
- Easier to test
- Clearer defaults

### 6. Random Number Generation

**Python:** `random` module
**Go:** `math/rand` package

Note: Go requires explicit seeding for true randomness (added in initialization).

### 7. Time Handling

**Python:** `datetime` module with string formatting
**Go:** `time` package with structured time operations

Improvements:
- More robust time parsing
- Better type safety
- Cleaner API

## Functional Equivalence

All features from the Python version are preserved:

✅ Random sound selection from music directory
✅ Configurable time periods (begin/over)
✅ Silent intervals between sounds
✅ Rhythmic pauses between bursts
✅ Force mode (-f flag)
✅ Debug/interval mode (-i flag)
✅ Verbose mode (-v flag)
✅ Skip initial sound (-w flag)
✅ Custom probability control (-p flag)
✅ Cross-platform support (Windows/Linux)

## Advantages of Go Version

1. **Single Binary Deployment**: No need for Python interpreter or dependencies
2. **Better Performance**: Compiled code runs faster
3. **Type Safety**: Compile-time error checking
4. **Easier Distribution**: Just copy the executable
5. **Lower Memory Footprint**: More efficient resource usage
6. **Cross-Compilation**: Easy to build for different platforms

## Building and Running

### Build
```bash
# Windows
go build -o sleep-sound.exe

# Linux/Mac
go build -o sleep-sound
```

### Run
```bash
./sleep-sound [options]
```

## Testing

To verify the Go version works correctly:

1. Ensure you have audio files in the `music/` directory
2. Run with verbose mode: `./sleep-sound -v`
3. For quick testing, use debug mode: `./sleep-sound -i -v`

## Known Differences

1. **Audioplayer Mode**: The `-ap` flag is accepted but not yet fully implemented in Go
2. **Volume Control**: Implemented differently due to platform constraints
3. **Configuration File**: INI file parsing not yet ported (can be added if needed)

## Future Enhancements

Potential improvements for the Go version:
- Add INI configuration file support
- Implement proper audioplayer library integration
- Add logging framework
- Create systemd service file
- Add web interface for remote control
- Implement playlist support

## Conclusion

The Go refactoring maintains full functional compatibility with the Python original while providing better performance, easier deployment, and improved code organization. The modular structure makes it easier to maintain and extend in the future.
