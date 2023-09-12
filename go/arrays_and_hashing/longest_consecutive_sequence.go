package main

func longestConsecutive(nums []int) int {
    numSet := map[int]bool{}
    longest := 0

    for _, num := range nums {
        numSet[num] = true
    }

    for _, num := range nums {
        _, exists := numSet[num - 1]
        if !exists {
            length := 1
            for numSet[num + length] {
                length++
            }
            if length > longest {
                longest = length
            }
        }
    }

    return longest
}

