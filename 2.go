package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	horizontal := 0
	depth := 0
	aim := 0
	pwd, _ := os.Getwd()
	file, err := os.Open(pwd + "\\2.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		part := strings.Split(line, " ")
		delta, _ := strconv.Atoi(part[1])
		switch part[0] {
		case "forward":
			horizontal += delta
			depth += (aim * delta)
		case "up":
			aim -= delta
			if depth < 0 {
				depth = 0
			}
		case "down":
			aim += delta
		}
	}
	println(horizontal, depth, horizontal*depth)
}
