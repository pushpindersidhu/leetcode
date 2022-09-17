/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function (nums1, nums2) {
  const intersection = [];
  for (let i = 0; i < nums1.length; i++) {
    const num1 = nums1[i];
    for (let j = 0; j < nums2.length; j++) {
      const num2 = nums2[j];
      if (num1 === num2) {
        intersection.push(num1);
        nums2.splice(j, 1);
        break;
      }
    }
  }
  return intersection;
};
