package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

func main() {
	pwd, _ := os.Getwd()
	file, err := os.Open(pwd + "\\1.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	var increase = 0
	var depth = 0
	var i = 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		var line, _ = strconv.Atoi(scanner.Text())
		if i > 0 && line > depth {
			increase += 1
		}
		depth = line
		i = i + 1
	}
	println(increase)
}
