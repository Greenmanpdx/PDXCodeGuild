/**
 * Created by greenman on 7/5/17.
 */
var namesToAges = {
    'Alyssa': 22,
    'Charley': 25,
    'Dan': 25,
    'Jeff': 20,
    'Kasey': 20,
    'Kim': 20,
    'Morgan': 25,
    'Ryan': 25,
    'Stef': 22
};

function findRarestValue(names) {
       var currentCount = 0;
       var nextCount = 0;
       var ages = {};

       $.each(names, function (key, value) {
           if(ages === null){ ages.key = 1}
           else if(ages.key){ages.key += 1}
           else {ages.key =1}
       })

}

findRarestValue(namesToAges);
console.log(ages);