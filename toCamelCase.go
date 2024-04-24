//link to kata == https://www.codewars.com/kata/517abf86da9663f1d2000003/train/go

/*
Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized only if the original word was capitalized
(known as Upper Camel Case, also often referred to as Pascal case). 
The next words should be always capitalized.
Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"
*/

package main

import (

		"fmt"
		"string"

func ToCamelCase(s string) string {
	var result string //another string that will hold the string after modification since it is not possible to modify strings in a loop
	var int i 
	for i = 0;i < len(s); i++ {
		//check if the current character is a dash '_' or a hiphen '-'
		if s[i] == '-' || s[i] == '_'{
			//capitalize the next character and append it to result variable 
			result += strings.Title(string(s[i+1]))
			i++
		}else{
			result += string(s[i])
	}

	}
	return result 
}



//did not need this function
/*

func TitleCase(c byte) byte {
		//check if the character is a lowercase alphabetical character
		if c >= 'a' && c <= 'z' {
				c = c - 32 //32 since the differnce between a lowercase character and its equivalent uppercase is 32
		}
		return c
}
*/

