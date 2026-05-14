package player

import (
	"fmt"
	"math/rand"
	"os"
	"os/exec"
	"path/filepath"
	"runtime"
)

// SoundPlayer handles audio playback
type SoundPlayer struct {
	useAudioplayer bool
}

// NewSoundPlayer creates a new SoundPlayer instance
func NewSoundPlayer(useAudioplayer bool) *SoundPlayer {
	return &SoundPlayer{
		useAudioplayer: useAudioplayer,
	}
}

// GetRandomAudioFile returns a random audio file path from the music directory
func GetRandomAudioFile(musicDir string) (string, error) {
	files, err := os.ReadDir(musicDir)
	if err != nil {
		return "", fmt.Errorf("failed to read music directory: %w", err)
	}

	var audioFiles []string
	for _, file := range files {
		if !file.IsDir() {
			audioFiles = append(audioFiles, file.Name())
		}
	}

	if len(audioFiles) == 0 {
		return "", fmt.Errorf("no audio files found in %s", musicDir)
	}

	randomIndex := rand.Intn(len(audioFiles))
	selectedFile := audioFiles[randomIndex]
	fmt.Println("Selected", selectedFile)

	fullPath := filepath.Join(musicDir, selectedFile)
	return fullPath, nil
}

// SetVolume generates a random volume level
func SetVolume(min, max float64) float64 {
	return min + rand.Float64()*(max-min)
}

// PlaySound plays an audio file using platform-specific methods
func (sp *SoundPlayer) PlaySound(audioFile string) error {
	if sp.useAudioplayer {
		// For audioplayer library (not implemented in this version)
		return fmt.Errorf("audioplayer mode not yet implemented")
	}

	platform := runtime.GOOS
	switch platform {
	case "linux":
		cmd := exec.Command("aplay", "-D", "plughw:CARD=D1,DEV=0", audioFile)
		err := cmd.Run()
		if err != nil {
			return fmt.Errorf("failed to play sound on Linux: %w", err)
		}
	case "windows":
		// On Windows, we'll use PowerShell to play sound
		cmd := exec.Command("powershell", "-c", 
			fmt.Sprintf(`(New-Object Media.SoundPlayer "%s").PlaySync()`, audioFile))
		err := cmd.Run()
		if err != nil {
			return fmt.Errorf("failed to play sound on Windows: %w", err)
		}
	default:
		return fmt.Errorf("unsupported platform: %s", platform)
	}

	fmt.Println("BOOM")
	return nil
}
