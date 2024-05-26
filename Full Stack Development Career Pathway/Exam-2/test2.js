function formatNumber(num) {
    if (num === undefined || num === null || typeof num === 'string') {
        return num;
    }

    const sign = num < 0 ? "-" : "";
    let numStringArray = Math.abs(num).toString().split('');

    let start = numStringArray.indexOf('.');
    if (start === -1) { // if num is an integer
        start = numStringArray.length;
    }

    for (let i = start - 3; i > 0; i -= 3) {
        numStringArray.splice(i, 0, ',');
    }

    return sign + numStringArray.join('');
}

module.exports = formatNumber;
