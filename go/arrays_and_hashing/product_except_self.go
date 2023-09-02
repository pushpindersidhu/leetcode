package main

func productExceptSelf(nums []int) []int {
    length := len(nums)

    result := make([]int, length)

    prefix := 1
    for i := 0; i < length; i++ {
        result[i] = prefix
        prefix *= nums[i]
    }

    postfix := 1
    for i := length - 1; i >= 0; i-- {
        result[i] *= postfix
        postfix *= nums[i]
    }

    return result
}

