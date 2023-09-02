package main

func groupAnagrams(strs []string) [][]string {
    m := map[[26]int][]string{}

    a := int('a')
    for _, str := range strs {
        var count [26]int

        for _, ch := range str {
            count[int(ch) - a] += 1
        }

        m[count] = append(m[count], str)
    }

    out := make([][]string, len(m))
    i := 0
    for _, value := range m {
        out[i] = value
        i++
    }

    return out
}

