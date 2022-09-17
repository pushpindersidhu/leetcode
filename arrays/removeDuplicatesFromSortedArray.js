/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j <= i; j++) {
      if (i === j) continue;
      if (nums[i] === nums[j]) return true;
    }
  }
  return false;
};
