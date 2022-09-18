/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function (digits) {
  let index = digits.length - 1;
  let digit = digits[index];

  while (digit == 9) {
    digits[index] = 0;
    index--;
    digit = digits[index];
  }

  if (index < 0) digits.unshift(1);
  digits[index] = digit + 1;
  return digits;
};
