package config

import (
	"fmt"
	"os"
	"path/filepath"
)

// Config holds all configuration for the sleep sound application
type Config struct {
	MusicDir           string
	SilentIntervalMin  int
	SilentIntervalMax  int
	TimeBegin          string
	TimeOver           string
	Possibility        int
	Force              bool
	SkipInitialSound   bool
	Verbose            bool
	UseAudioplayer     bool
	RythmicPauseMin    float64
	RythmicPauseMax    float64
	DebugInterval      bool
}

// DefaultConfig returns a Config with default values
func DefaultConfig() *Config {
	runningDir, _ := os.Getwd()
	musicDir := filepath.Join(runningDir, "music")

	return &Config{
		MusicDir:          musicDir,
		SilentIntervalMin: 900,
		SilentIntervalMax: 1800,
		TimeBegin:         "2138",
		TimeOver:          "0832",
		Possibility:       60,
		Force:             false,
		SkipInitialSound:  true,
		Verbose:           false,
		UseAudioplayer:    false,
		RythmicPauseMin:   0.2,
		RythmicPauseMax:   0.4,
		DebugInterval:     false,
	}
}

// ApplyDebugSettings applies debug settings when debug interval mode is enabled
func (c *Config) ApplyDebugSettings() {
	if c.DebugInterval {
		c.SilentIntervalMin = 1
		c.SilentIntervalMax = 2
		c.RythmicPauseMin = 0.2
		c.RythmicPauseMax = 0.4
		fmt.Println("short silent interval")
	}
}
