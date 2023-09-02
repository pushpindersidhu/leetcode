package main

func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    a := int('a')
    count_s := make([]int, 26)
    count_t := make([]int, 26)

    for i := range s {
        count_s[int(s[i]) - a] += 1
        count_t[int(t[i]) - a] += 1
    }

    return compareSlices(&count_s, &count_t)
}

func compareSlices(s1 *[]int, s2 *[]int) bool {
    if len(*s1) != len(*s2) {
        return false
    }

    for i := range *s1 {
        if (*s1)[i] != (*s2)[i] {
            return false
        }
    }

    return true
}

