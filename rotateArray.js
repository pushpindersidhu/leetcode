/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function (nums, k) {
  const length = nums.length;

  const reverse = (arr, start, end) => {
    while (start < end) {
      [arr[start], arr[end]] = [arr[end], arr[start]];
      start++;
      end--;
    }
  };

  k %= length;

  reverse(nums, 0, length - 1);
  reverse(nums, 0, k - 1);
  reverse(nums, k, length - 1);
};
