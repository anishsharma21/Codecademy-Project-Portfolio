const formatNumber = require('../test2');

test('formatNumber should format positive integer correctly', () => {
  expect(formatNumber(1000)).toBe('1,000');
  expect(formatNumber(1000000)).toBe('1,000,000');
  expect(formatNumber(123456789)).toBe('123,456,789');
});

test('formatNumber should format negative integer correctly', () => {
  expect(formatNumber(-1000)).toBe('-1,000');
  expect(formatNumber(-1000000)).toBe('-1,000,000');
  expect(formatNumber(-123456789)).toBe('-123,456,789');
});

test('formatNumber should format positive float correctly', () => {
  expect(formatNumber(1234.56)).toBe('1,234.56');
  expect(formatNumber(1234567.89)).toBe('1,234,567.89');
});

test('formatNumber should format negative float correctly', () => {
  expect(formatNumber(-1234.56)).toBe('-1,234.56');
  expect(formatNumber(-1234567.89)).toBe('-1,234,567.89');
});

test('formatNumber should return the same string for non-numeric input', () => {
  expect(formatNumber('1234')).toBe('1234');
  expect(formatNumber('abc')).toBe('abc');
  expect(formatNumber(null)).toBe(null);
});

test('formatNumber should handle zero correctly', () => {
  expect(formatNumber(0)).toBe('0');
});

test('formatNumber should handle very large numbers correctly', () => {
  expect(formatNumber(9007199254740991)).toBe('9,007,199,254,740,991');
});

test('formatNumber should handle very small numbers correctly', () => {
  expect(formatNumber(0.000123456789)).toBe('0.000123456789');
});

test('formatNumber should handle undefined correctly', () => {
  expect(formatNumber(undefined)).toBe(undefined);
});