# Sleep Sound (Go Version)

A sleep sound application that plays random audio files during specified time periods with configurable intervals.

## Features

- Plays random sounds from a music directory
- Configurable time periods for sound playback
- Random silent intervals between sounds
- Rhythmic pauses between burst sounds
- Cross-platform support (Windows and Linux)
- Command-line configuration options

## Building

```bash
go build -o sleep-sound
```

## Usage

```bash
./sleep-sound [options]
```

### Options

- `-f`: Force noise when not at booming time
- `-i`: Short silent interval for debugging
- `-ap`: Use audioplayer library (not yet implemented)
- `-v`: Verbose mode - print out silent or boom status
- `-b string`: Beginning time of boom (format: HHMM, e.g., "2138")
- `-o string`: Over time of boom (format: HHMM, e.g., "0832")
- `-w`: Skip initial sleep sound right after execution
- `-p`: Force the possibility to be true (always play)
- `-rmin float`: Rythmic pause minimum (default: 0.2)
- `-rmax float`: Rythmic pause maximum (default: 0.4)
- `-smin int`: Silent interval minimum in seconds (default: 900)
- `-smax int`: Silent interval maximum in seconds (default: 1800)

### Examples

Run with default settings:
```bash
./sleep-sound
```

Force sounds outside normal hours:
```bash
./sleep-sound -f
```

Debug mode with short intervals:
```bash
./sleep-sound -i -v
```

Custom time period:
```bash
./sleep-sound -b 2200 -o 0700
```

## Configuration

The application uses the following defaults:
- Music directory: `./music`
- Silent interval: 900-1800 seconds (15-30 minutes)
- Boom time: 21:38 to 08:32 (next day)
- Possibility: 60% chance to play sound
- Rythmic pause: 0.2-0.4 seconds

## Project Structure

```
sleep-sound/
├── main.go              # Main entry point
├── config/
│   └── config.go        # Configuration management
├── player/
│   └── player.go        # Audio playback functionality
├── timeutil/
│   └── timeutil.go      # Time utilities
├── music/               # Directory for audio files
└── go.mod               # Go module file
```

## Platform Support

- **Linux**: Uses `aplay` for audio playback
- **Windows**: Uses PowerShell's SoundPlayer for audio playback

## Migration from Python

This is a Go refactoring of the original Python sleep-sound application. The functionality remains the same while providing better performance and easier deployment (single binary).
