// Task
// Find longest palindrome in a string, my way keeps timing out oh well.

function is_Palindrome(str1) {
    var rev = str1.split("").reverse().join("");
    return str1 == rev;
}
    
function longestPalindrome(str1){

    if (str1.length == 0) {
        return 0;
    }
    
    var max_length = 0,
    maxp = '';
    
    for(var i=0; i < str1.length; i++) {
        var subs = str1.substr(i, str1.length);
    
        for(var j=subs.length; j>=0; j--) {
            var sub_subs_str = subs.substr(0, j);
            if (sub_subs_str.length <= 1)
            continue;
    
            if (is_Palindrome(sub_subs_str)) {
                if (sub_subs_str.length > max_length) {
                    max_length = sub_subs_str.length;
                    maxp = sub_subs_str;
                }
            }
        }
    }

    if (maxp.length == 0) {
        return 1; 
    } else {
        return maxp.length;
    }
}

console.log(longestPalindrome("a"));
console.log(longestPalindrome("aab"));
console.log(longestPalindrome("abcde"));
console.log(longestPalindrome("zzbaabcd"));
console.log(longestPalindrome(""));
console.log(longestPalindrome("zyabyz"));
console.log(longestPalindrome("baabcd"));
console.log(longestPalindrome("baablkj12345432133d"));