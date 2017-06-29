/**
 * Created by greenman on 6/28/17.
 */

var alphabet = 'abcdefghijklmnopqrstuvwxyx'.split('');

function incrementChar(char, key){
    var index = alphabet.indexOf(char);
    if (index + key > 23){

    }
    else return alphabet[index + key]
}

function decrement(char, key){
    var index = alphabet.indexOf(char);
    return alphabet[index - key]
}

function caesarEncrypt(plainStr, key) {
    var newString = '';
    for(var i =0; i < plainStr.length; ++i){
        newString += incrementChar(plainStr[i], key);
    }
    console.log(newString);
    return newString;


}

function caesarDecrypt(plainStr, key) {
    var newString = '';
    for(var i =0; i < plainStr.length; ++i){
        newString.append(decrement(plainStr[i]));
    }
    return newString;
}

$('#encode').click(function () {
    var msg = caesarEncrypt($('#uncoded').val(), parseInt($('#key').val()));
    console.log(msg);
})