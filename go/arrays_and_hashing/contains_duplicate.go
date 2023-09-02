package main

func containsDuplicate(nums []int) bool {
    map := make(map[int]bool)

    for _, num := range nums {
        _, exists := m[num]
        if exists {
            return true
        }
        m[num] = true
    }

    return false
}

