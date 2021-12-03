package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	pwd, _ := os.Getwd()
	file, err := os.Open(pwd + "\\3b.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	line := 0
	bits := []int{}
	length := 0
	o2_numbers := make([]string, 0)
	co2_numbers := make([]string, 0)
	for scanner.Scan() {
		line += 1
		line := scanner.Text()
		o2_numbers = append(o2_numbers, line)
		co2_numbers = append(co2_numbers, line)
		length = len(line)
		for i := 0; i < length; i++ {
			bit := string([]rune(line)[i])
			if len(bits) < length && bit == "0" {
				bits = append(bits, 0)
			} else if len(bits) < length && bit == "1" {
				bits = append(bits, 1)
			} else if len(bits) >= length && bit == "1" {
				bits[i]++
			}
		}
	}
	gamma := 0
	epsilon := 0
	for i := 0; i < length; i++ {
		gamma = gamma << 1
		epsilon = epsilon << 1
		if line-bits[i] < bits[i] {
			gamma = gamma | 1
		}
		if line-bits[i] > bits[i] {
			epsilon = epsilon | 1
		}
	}
	o2_rating, _ := strconv.ParseInt(get_o2_rating(line, o2_numbers, bits), 2, 64)
	// co2_rating, _ := strconv.ParseInt(get_co2_rating(line, co2_numbers, bits), 2, 64)
	fmt.Println(bits)
	println("O2 Generator Rating: ", o2_rating)
	// println("CO2 Generator Rating: ", co2_rating)
	println("Gamma: ", gamma)
	println("Epsilon: ", epsilon)
	println("Power consumption: ", gamma*epsilon)
	// println("Life support rating: ", o2_rating*co2_rating)
}

func most_used(line int, position int, bits []int) string {
	// println("*", line, position, bits[position])
	if line-bits[position] > bits[position] {
		// println(line, "-", bits[position], ">", bits[position], "at position", position)
		return "0"
	} else {
		return "1"
	}
}

func least_used(line int, position int, bits []int) string {
	// println("*", line, position, bits[position])
	if line-bits[position] <= bits[position] {
		// println(line, "-", bits[position], "<=", bits[position], "at position", position)
		return "0"
	} else {
		return "1"
	}
}

func get_o2_rating(line int, o2_numbers []string, bits []int) string {
	bit_length := len(o2_numbers[0])
	fmt.Println(o2_numbers)
	for i := 0; i < bit_length; i++ {
		most_used := most_used(len(o2_numbers), i, bits)
		o2_numbers = remove_numbers(o2_numbers, i, most_used)
		if len(o2_numbers) == 1 {
			println("FOUND O2 NUMBER")
			return o2_numbers[0]
		}
		bits = get_bitmap(o2_numbers)
	}
	println("FAILED, TOO MANY O2 NUMBERS", len(o2_numbers))
	return o2_numbers[0]
}

func get_co2_rating(line int, co2_numbers []string, bits []int) string {
	bit_length := len(co2_numbers[0])
	for i := 0; i < bit_length; i++ {
		fmt.Println("position", i, "bits", bits, "for", len(co2_numbers), co2_numbers)
		least_used := least_used(len(co2_numbers), i, bits)
		co2_numbers = remove_numbers(co2_numbers, i, least_used)
		if len(co2_numbers) == 1 {
			return co2_numbers[0]
		}
		bits = get_bitmap(co2_numbers)
	}
	return co2_numbers[0]
}

func get_bitmap(numbers []string) []int {
	bits := []int{}
	length := len(numbers[0])
	for n := 0; n < len(numbers); n++ {
		for i := 0; i < length; i++ {
			line := numbers[n]
			bit := string([]rune(line)[i])
			if len(bits) < length && bit == "0" {
				bits = append(bits, 0)
			} else if len(bits) < length && bit == "1" {
				bits = append(bits, 1)
			} else if len(bits) >= length && bit == "1" {
				bits[i]++
			}
		}
	}
	return bits
}

func remove_numbers(numbers []string, position int, required string) []string {
	i := 0
	for {
		if i >= len(numbers) {
			break
		}
		bit := string([]rune(numbers[i])[position])
		if bit != required {
			println("removing", numbers[i], "because bit", position, "is not", required, "i = ", i)
			if position == len(numbers[i])-1 {
				numbers = append(numbers[:position])
				break
			} else if position == 0 {
				numbers = numbers[1:]
			} else {
				numbers = append(numbers[:i], numbers[i+1:]...)
				continue
			}
		}
		i++
	}
	fmt.Println("#", numbers)
	return numbers
}
