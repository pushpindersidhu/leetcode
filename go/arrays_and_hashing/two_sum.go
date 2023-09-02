package main

func twoSum(nums []int, target int) []int {
    m := make(map[int]int)

    for i, num := range nums {
        value, exists := m[num]
        if exists {
            return []int{i, value}
        }

        diff := target - num
        m[diff] = i
    }

    return []int{}
}

