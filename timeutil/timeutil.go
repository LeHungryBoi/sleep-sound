package timeutil

import (
	"fmt"
	"time"
)

// GetCurrentTimeInt returns current time as HHMM integer format
func GetCurrentTimeInt() int {
	now := time.Now()
	hour := now.Hour()
	minute := now.Minute()
	return hour*100 + minute
}

// IsBoomingTime checks if current time is within the booming time period
func IsBoomingTime(timeBegin, timeOver string) bool {
	currentTime := GetCurrentTimeInt()
	timeBeginInt := ParseTimeString(timeBegin)
	timeOverInt := ParseTimeString(timeOver)

	if timeBeginInt < timeOverInt {
		// Within one day
		return currentTime > timeBeginInt && currentTime < timeOverInt
	} else if timeBeginInt > timeOverInt {
		// Across two days
		return !(currentTime > timeOverInt && currentTime < timeBeginInt)
	} else {
		// Always booming
		return true
	}
}

// ParseTimeString parses a time string in HHMM format to integer
func ParseTimeString(timeStr string) int {
	var hour, minute int
	fmt.Sscanf(timeStr, "%02d%02d", &hour, &minute)
	return hour*100 + minute
}
