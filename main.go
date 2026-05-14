package main

import (
	"flag"
	"fmt"
	"math/rand"
	"os"
	"time"

	"sleep-sound/config"
	"sleep-sound/player"
	"sleep-sound/timeutil"
)

var (
	force           = flag.Bool("f", false, "force noise when not at booming time")
	interval        = flag.Bool("i", false, "short silent interval for debugging")
	ap              = flag.Bool("ap", false, "use audioplayer library")
	verbose         = flag.Bool("v", false, "print out silent or boom")
	begin           = flag.String("b", "", "beginning time of boom")
	over            = flag.String("o", "", "over time of boom")
	wait            = flag.Bool("w", false, "skip initial sleep sound right after execution")
	p               = flag.Bool("p", false, "to force the possibility to be true")
	rmin            = flag.Float64("rmin", 0, "rythmic pause minimum")
	rmax            = flag.Float64("rmax", 0, "rythmic pause maximum")
	smin            = flag.Int("smin", 0, "silent interval minimum")
	smax            = flag.Int("smax", 0, "silent interval maximum")
)

func main() {
	flag.Parse()

	// Initialize configuration
	cfg := config.DefaultConfig()

	// Apply command-line arguments
	if *force {
		cfg.Force = true
		fmt.Println("force is True")
	} else {
		fmt.Println("force is False")
	}

	if *interval {
		cfg.DebugInterval = true
	}

	if *ap {
		cfg.UseAudioplayer = true
	}

	if *begin != "" {
		cfg.TimeBegin = *begin
	}

	if *over != "" {
		cfg.TimeOver = *over
	}

	if *rmin > 0 {
		cfg.RythmicPauseMin = *rmin
	}

	if *rmax > 0 {
		cfg.RythmicPauseMax = *rmax
	}

	if *smin > 0 {
		cfg.SilentIntervalMin = *smin
	}

	if *smax > 0 {
		cfg.SilentIntervalMax = *smax
	}

	if *wait {
		cfg.SkipInitialSound = false
	}

	// Apply debug settings if needed
	cfg.ApplyDebugSettings()

	// Check if music directory exists
	if _, err := os.Stat(cfg.MusicDir); os.IsNotExist(err) {
		fmt.Printf("Music directory not found: %s\n", cfg.MusicDir)
		os.Exit(1)
	}

	// Create sound player
	soundPlayer := player.NewSoundPlayer(cfg.UseAudioplayer)

	// Play initial sound if not skipped
	if !cfg.SkipInitialSound {
		playRandomSound(soundPlayer, cfg)
	}

	// Main loop
	for {
		boomingTime := timeutil.IsBoomingTime(cfg.TimeBegin, cfg.TimeOver)

		if cfg.Verbose {
			if boomingTime {
				fmt.Println("booming time")
			} else {
				fmt.Println("silent time")
			}
		}

		if boomingTime || cfg.Force {
			// Set silent interval
			silentInterval := randomInt(cfg.SilentIntervalMin, cfg.SilentIntervalMax)
			fmt.Printf("Waiting for %d seconds\n", silentInterval)
			fmt.Printf("sleeping for %d\n", silentInterval)
			time.Sleep(time.Duration(silentInterval) * time.Second)

			// Randomly set how many burst sounds to play
			boomBurstMin := 1
			boomBurstMax := 1
			boomBurstAmount := randomInt(boomBurstMin, boomBurstMax)

			for boomBurstCount := 0; boomBurstCount < boomBurstAmount; boomBurstCount++ {
				willBoom := true
				if !*p {
					willBoom = randomBool(cfg.Possibility)
				}

				if willBoom {
					playRandomSound(soundPlayer, cfg)
					fmt.Printf("%d / %d\n", boomBurstCount+1, boomBurstAmount)
				}

				rythmicPause := randomFloat(cfg.RythmicPauseMin, cfg.RythmicPauseMax)
				if willBoom {
					fmt.Printf("hold on %.2f\n", rythmicPause)
				} else {
					fmt.Println("it's a dud")
				}

				time.Sleep(time.Duration(rythmicPause*1000) * time.Millisecond)
			}
		}

		time.Sleep(1 * time.Second)
	}
}

// playRandomSound plays a random sound from the music directory
func playRandomSound(soundPlayer *player.SoundPlayer, cfg *config.Config) {
	audioFile, err := player.GetRandomAudioFile(cfg.MusicDir)
	if err != nil {
		fmt.Printf("Error getting random audio file: %v\n", err)
		return
	}

	fmt.Println(audioFile)
	err = soundPlayer.PlaySound(audioFile)
	if err != nil {
		fmt.Printf("Error playing sound: %v\n", err)
	}
}

// randomInt returns a random integer between min and max (inclusive)
func randomInt(min, max int) int {
	return rand.Intn(max-min+1) + min
}

// randomFloat returns a random float64 between min and max
func randomFloat(min, max float64) float64 {
	return min + rand.Float64()*(max-min)
}

// randomBool returns true with the given probability percentage
func randomBool(probability int) bool {
	return rand.Intn(100) < probability
}
