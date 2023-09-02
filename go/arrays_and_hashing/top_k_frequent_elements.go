package main

func topKFrequent(nums []int, k int) []int {
    freq := make(map[int]int)

    for _, num := range nums {
        freq[num] += 1
    }

    out := make([]int, k)

    for num, numFreq := range freq {
        for index, outNum := range out {
            outNumFreq := freq[outNum]
            if numFreq >= outNumFreq && num != outNum {
                for i := len(out) - 1; i > index; i-- {
                    out[i] = out[i - 1]
                }
                out[index] = num
                break
            }
        }
    }

    return out
}

