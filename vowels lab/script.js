/**
 * Created by greenman on 6/23/17.
 */
// var char = prompt('Enter a character');
var vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'y', 'Y']
function isVowel(char) {
    if (vowels.indexOf(char) === -1){
        alert('The character you entered is not a vowel')
    }
    else if (vowels.indexOf(char) === 10 || vowels.indexOf(char) === 11){
        alert('Y is sometimes a vowel')
    }
    else{
        alert('You entered a vowel')
    }


}
var char = prompt('Enter a character');
isVowel(char);
var Continue = true;
while (Continue === true) {
    char = prompt('Enter a character');
    if(!char){Continue = false}
    isVowel(char);
}