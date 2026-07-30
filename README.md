# 🐍 Python Exercises - Mundo 1 - Curso em Vídeo (Gustavo Guanabara)
This repository brings together my solutions to the challenges proposed by professor Gustavo Guanabara of the renowned Python (Mundo 1) course from the Curso em Vídeo channel.

## 📂 How to test the code?

To run any of the exercises, follow these simple instructions:

1. Have Python 3 installed on your computer.
2. Copy the code written in the files inside this repository.
3. Paste the code directly into your terminal or into any Python-supported IDE/software of your choice (such as VS Code, PyCharm, IDLE, or Jupyter Notebook) and press the Play (Run) button.
4. Follow the on-screen prompts in the console/terminal (some exercises will ask you to enter numbers, names, or select options).

## List of Exercise ( Challenges)

### 05. Exercise 05 Predecessor successor
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that reads an integer and displays its predecessor and successor
  - **Objective:** Reads an integer and shows its predecessor and successor in different colors in the terminal.
  - **Simulated Interface:** Keyboard input of an integer; formatted output with predecessor in red, current number in yellow, and successor in green.
  - **Code Logic:** Application of subtraction (n-1) and addition (n+1) and the use of ANSI escape codes to color the text.
  - **File:** [`Exercicios5a15.py`](./Exercicios5a15.py)
</details>

### 06. Exercise 06 Double triple square root
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that reads a number and shows its double, triple, and square root.
  - **Objective:** Calculates and displays the double, triple, and square root of an integer provided by the user.
  - **Simulated Interface:** The user inputs an integer via the keyboard; the program displays the results in color (red for double, yellow for triple, green for square root) and formats the square root with two decimal places.
  - **Code Logic:** Application of basic arithmetic operations (multiplication and exponentiation) and output formatting with ANSI colors.
  - **File:** [`Exercicios5a15.py`](./Exercicios5a15.py)
</details>

### 07. Exercise 07 Grades average
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that reads two grades of a student and calculates their average.
  - **Objective:** Calculates the simple arithmetic average between two grades provided by the user.
  - **Simulated Interface:** The user inputs two grades (integers) via the keyboard; the program displays the average value formatted in green.
  - **Code Logic:** Application of addition and division to calculate the arithmetic average, with colored display in the terminal.
  - **File:** [`Exercicios5a15.py`](./Exercicios5a15.py)
</details>

### 08. Exercise 08 Meters conversion
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that converts a value in meters to centimeters and millimeters.
  - **Objective:** Converts a measurement in meters to its equivalents in centimeters and millimeters.
  - **Simulated Interface:** The user inputs an integer value representing meters; the program displays the results in centimeters (yellow) and millimeters (blue).
  - **Code Logic:** Application of multiplication by conversion factors (100 for cm, 1000 for mm) and colored output.
  - **File:** [`Exercicios5a15.py`](./Exercicios5a15.py)
</details>

### 09. Exercise 09 Multiplication table
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that shows the multiplication table of a number.
  - **Objective:** Displays the multiplication table (from 1 to 10) of an integer provided by the user.
  - **Simulated Interface:** The user inputs an integer; the program prints 10 lines on the screen, each showing the multiplication operation of the number by factors from 1 to 10, with the results highlighted in purple.
  - **Code Logic:** Application of repeated multiplications (manually, without a loop) and output formatting with ANSI colors.
  - **File:** [`Exercicios5a15.py`](./Exercicios5a15.py)
</details>

### 10. Exercise 10 Real to dollar conversion
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that converts Reais to Dollars.
  - **Objective:** Calculates the amount of dollars that can be purchased with a value in Reais, considering an exchange rate of 1 dollar = 3.27 reais.
  - **Simulated Interface:** The user inputs an integer value in reais; the program displays the corresponding value in dollars (only the integer part, as it uses integer division) highlighted in green.
  - **Code Logic:** Application of integer division (//) to convert reais to dollars using the fixed rate of 3.27.
  - **File:** [`Exercicios5a15.py`](./Exercicios5a15.py)
</details>

### 11. Exercise 11 Area paint
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that calculates the area (given width and height) and the amount of paint needed to paint it (each liter of paint covers an area of 2 square meters).
  - **Objective:** Calculates the area of a rectangular surface and determines how many liters of paint are required, knowing that 1 liter covers 2 m².
  - **Simulated Interface:** The user inputs the width and height (integers); the program displays the area in square meters (blue) and the amount of paint in liters (purple), using integer division for the liters.
  - **Code Logic:** Application of multiplication to calculate the area and integer division by 2 to determine the required paint.
  - **File:** [`Exercicios5a15.py`](./Exercicios5a15.py)
</details>

### 12. Exercise 12 Discount
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that sets a new price with a discount (5% discount).
  - **Objective:** Calculates the price of a product after applying a 5% discount to the original price.
  - **Simulated Interface:** The user inputs an integer value representing the original price; the program displays the discounted price (a float value, which may contain decimal places) highlighted in green.
  - **Code Logic:** Application of subtraction and multiplication to calculate the discount (price * 5/100) and subtract it from the original value.
  - **File:** [`Exercicios5a15.py`](./Exercicios5a15.py)
</details>

### 13. Exercise 13 Salary increase
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that increases a salary by 15%.
  - **Objective:** Calculates the new salary after applying a 15% increase to the original salary.
  - **Simulated Interface:** The user inputs an integer value representing the current salary; the program displays the new salary with the increase (a float value, which may contain decimal places) highlighted in green.
  - **Code Logic:** Application of addition and multiplication to calculate the increase (salary * 15/100) and add it to the original value.
  - **File:** [`Exercicios5a15.py`](./Exercicios5a15.py)
</details>

### 14. Exercise 14 Celsius fahrenheit conversion
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that converts a temperature entered in degrees Celsius to degrees Fahrenheit.
  - **Objective:** Converts temperature from the Celsius scale to the Fahrenheit scale using the formula F = (C × 9/5) + 32.
  - **Simulated Interface:** The user inputs an integer value representing the temperature in Celsius; the program displays the converted value in Fahrenheit highlighted in blue.
  - **Code Logic:** Application of the conversion formula using multiplication, division, and addition, along with colored output formatting.
  - **File:** [`Exercicios5a15.py`](./Exercicios5a15.py)
</details>

### 15. Exercise 15 Car rental
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that asks for the number of km driven by a rental car and the number of days it was rented for. Calculates the price to pay, knowing that the car costs R$60 per day and R$0.15 per km driven.
  - **Objective:** Calculates the total cost of renting a car based on the days used and the distance driven.
  - **Simulated Interface:** The user inputs the driven mileage (integer) and the number of days (integer); the program displays the total amount to pay (float) highlighted in green.
  - **Code Logic:** Application of multiplication and addition to combine the daily cost (days × 60) and the distance cost (km × 0.15).
  - **File:** [`Exercicios5a15.py`](./Exercicios5a15.py)
</details>


### 16. Exercise 16 Integer portion
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that reads any Real number and displays its Integer portion.
  - **Objective:** Extracts and displays the integer part of a decimal number provided by the user.
  - **Simulated Interface:** The user inputs a real number (float) via the keyboard; the program displays the original number and its integer part (using integer division by 1) highlighted in blue.
  - **Code Logic:** Application of integer division (//) by 1 to truncate the decimal part and retrieve only the integer value.
  - **File:** [`Exercicios16a21.py`](./Exercicios16a21.py)
</details>

### 17. Exercise 17 Hypotenuse
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that reads the length of the opposite leg and adjacent leg of a right triangle, then calculates and displays the length of the hypotenuse.
  - **Objective:** Calculates the hypotenuse of a right triangle using the Pythagorean Theorem (h = √(ca² + co²)).
  - **Simulated Interface:** The user inputs the values of the two legs (integers); the program displays the value of the hypotenuse with two decimal places, highlighted in red.
  - **Code Logic:** Application of exponentiation (squaring), addition, and square root (raising to the power of 0.5) to calculate the hypotenuse.
  - **File:** [`Exercicios16a21.py`](./Exercicios16a21.py)
</details>

### 18. Exercise 18 Sine cosine tangent
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that reads any angle and displays the sine, cosine, and tangent values of that angle on the screen.
  - **Objective:** Calculates and displays the sine, cosine, and tangent of an angle provided in degrees, showing only the integer part (truncated) of each value.
  - **Simulated Interface:** The user inputs a real number (angle in degrees); the program displays the values of sine (yellow), cosine (green), and tangent (blue), all truncated to integers (using integer division by 1).
  - **Code Logic:** Application of the math library to convert degrees to radians (math.radians), calculation of trigonometric functions (math.sin, math.cos, math.tan), and truncation using integer division (//1).
  - **File:** [`Exercicios16a21.py`](./Exercicios16a21.py)
</details>

### 19. Exercise 19 Student draw
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that reads the names of students and displays the name of the chosen one.
  - **Objective:** Randomly draws one student from four names provided by the user.
  - **Simulated Interface:** The user inputs the names of four students (strings) via the keyboard; the program displays the drawn student's name highlighted in yellow.
  - **Code Logic:** Application of the choice() function from the random library to randomly select an element from a list containing the four names.
  - **File:** [`Exercicios16a21.py`](./Exercicios16a21.py)
</details>

### 20. Exercise 20 Drawn order
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that reads the names of four students and displays the drawn order.
  - **Objective:** Randomly shuffles the list of students and displays the new presentation order.
  - **Simulated Interface:** The program uses the student list already registered (from the previous exercise) and displays the shuffled order highlighted in blue.
  - **Code Logic:** Application of the shuffle() function from the random library to randomly permute the elements of the student list.
  - **File:** [`Exercicios16a21.py`](./Exercicios16a21.py)
</details>

### 21. Exercise 21 Play music
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** A program that plays music using the pygame library.
  - **Objective:** Plays an audio file (house_lo.mp3) and keeps the program running until the music finishes.
  - **Simulated Interface:** The program receives no user input; it only plays the audio and displays no formatted output on the screen (execution is silent, only playing the music).
  - **Code Logic:** Application of the pygame.mixer library to initialize the mixer, load the MP3 file, set the volume, start playback, and wait in a loop while the music is playing.
  - **File:** [`Exercicios16a21.py`](./Exercicios16a21.py)
</details>

### 22. Exercise 22 Name analysis
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that reads a person's full name and displays: the name in all uppercase and lowercase letters; how many total letters (excluding spaces); how many letters the first name has.
  - **Objective:** Analyzes and displays information about the provided full name, such as uppercase/lowercase versions, total count of alphabetic characters, and the length of the first name.
  - **Simulated Interface:** The user inputs a string (full name) via the keyboard; the program displays: name in uppercase (red), name in lowercase (yellow), total letters without spaces (blue), and number of letters in the first name (purple).
  - **Code Logic:** Application of string methods (upper(), lower(), replace(), split()) and the len() function for character manipulation and counting.
  - **File:** [`Exercicios22a27.py`](./Exercicios22a27.py)
</details>

### 23. Exercise 23 Separate digits
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that reads a number from 0 to 9999 and displays each of its digits separately on the screen.
  - **Objective:** Decomposes an integer into its individual digits (unit, ten, hundred, and thousand) and displays them separately.
  - **Simulated Interface:** The user inputs an integer between 0 and 9999; the program displays each digit in distinct colors: unit (red), ten (yellow), hundred (green), and thousand (blue).
  - **Code Logic:** Application of integer division and modulo operations (// and %) to extract each digit, using powers of 10 (1, 10, 100, 1000).
  - **File:** [`Exercicios22a27.py`](./Exercicios22a27.py)
</details> 

### 24. Exercise 24 City santo
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that reads the name of a city and states whether or not it starts with the name "SANTO".
  - **Objective:** Checks whether the first five characters of the city name (in uppercase) match the word "SANTO".
  - **Simulated Interface:** The user inputs a string (city name); the program displays a boolean value (True/False) indicating whether the city starts with "SANTO", highlighted in red.
  - **Code Logic:** Application of string slicing (city[:5]), conversion to uppercase (upper()), and comparison with the string "SANTO" to obtain the boolean result.
  - **File:** [`Exercicios22a27.py`](./Exercicios22a27.py)
</details> 

### 25. Exercise 25 Check silva
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that reads a person's name and states whether or not they have "SILVA" in their name.
  - **Objective:** Checks whether the substring "silva" (in lowercase) is present anywhere within the provided full name.
  - **Simulated Interface:** The user inputs a string (full name); the program displays a boolean value (True/False) indicating whether "silva" is contained in the name, highlighted in red.
  - **Code Logic:** Application of the in operator to check for the presence of the substring, after converting the name to lowercase using lower().
  - **File:** [`Exercicios22a27.py`](./Exercicios22a27.py)
</details> 

### 26. Exercise 26 Letter a count
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that reads a sentence from the keyboard and displays how many times the letter "A" appears, what position it appears in for the first time, and what position it appears in for the last time.
  - **Objective:** Counts the number of occurrences of the letter 'A' (regardless of uppercase/lowercase) in a sentence, and locates its first and last positions (using 1-based indexing).
  - **Simulated Interface:** The user inputs a sentence (string); the program displays the total count of 'A's, the position of the first occurrence (yellow), and the position of the last occurrence (blue), with positions adjusted to start at 1.
  - **Code Logic:** Application of string methods: upper() to standardize all letters to uppercase, count('A') for counting, find('A') for the first position, and rfind('A') for the last position, adding 1 to each index for 1-based display.
  - **File:** [`Exercicios22a27.py`](./Exercicios22a27.py)
</details> 

### 27. Exercise 27 First last name
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that reads a person's full name, then displays the first and last name separately.
  - **Objective:** Extracts and displays only the first name and the last name from a provided full name.
  - **Simulated Interface:** The user inputs a string (full name); the program displays the first name (red) and the last name (blue), obtained by splitting the string into parts.
  - **Code Logic:** Application of the split() method to break the name into a list of words, accessing the first element (index 0) and the last element (index -1 or list length minus 1).
  - **File:** [`Exercicios22a27.py`](./Exercicios22a27.py)
</details> 

### 28. Exercise 28 Guessing game
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** A program that makes the computer "think" of an integer between 0 and 5 and asks the user to try to guess which number was chosen by the computer.
  - **Objective:** Simulates a guessing game where the computer generates a random number and the user tries to guess it, comparing the inputs.
  - **Simulated Interface:** The user inputs an integer (guess); the program displays a "PROCESSING..." message with a 2-second pause, then informs whether the user won (in green) or lost (in red), revealing the chosen number.
  - **Code Logic:** Application of random number generation with randint(), use of the sleep() function to simulate processing, and an if/else conditional structure to compare the user's guess with the generated number.
  - **File:** [`Exercicios28a35.py`](./Exercicios28a35.py)
</details> 

### 29. Exercise 29 Speed fine
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that reads the speed of a car. (If it exceeds 80 km/h, the driver was fined. The fine will cost R$7.00 for each km over the limit).
  - **Objective:** Checks whether the provided speed exceeds the 80 km/h limit and, if so, calculates the fine amount (R$7.00 per km over the limit).
  - **Simulated Interface:** The user inputs an integer value (speed in km/h); the program displays "Ok" in green if within the limit, or a fine message and the total amount (in red) calculated based on the speed excess.
  - **Code Logic:** Application of an if/else conditional structure to compare the speed with the limit; in case of excess, calculates the difference and multiplies by 7 to obtain the fine amount.
  - **File:** [`Exercicios28a35.py`](./Exercicios28a35.py)
</details> 

### 30. Exercise 30 Even odd
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that reads the speed of a car. (If it exceeds 80 km/h, the driver was fined. The fine will cost R$7.00 for each km over the limit).
  - **Objective:** Classifies an integer as even or odd based on the remainder of its division by 2.
  - **Simulated Interface:** The user inputs an integer; the program displays "even" in yellow if the number is divisible by 2, or "odd" in red otherwise.
  - **Code Logic:** Application of the modulo operator (%) to get the remainder of division by 2 and an if/else conditional structure to determine the classification.
  - **File:** [`Exercicios28a35.py`](./Exercicios28a35.py)
</details> 

### 31. Exercise 31 Travel price
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that asks the distance of a trip in km. Calculate the ticket price, charging R$0.50 per km for trips up to 200 km and R$0.45 for longer trips.
  - **Objective:** Calculates ticket cost based on distance, applying a discounted rate for distances over 200 km.
  - **Simulated Interface:** The user inputs an integer value (distance in km); the program displays the total ticket price (in reais, highlighted in green) using the appropriate rate (0.50 for up to 200 km, 0.45 for above).
  - **Code Logic:** Application of an if/else conditional structure to select the rate based on distance and multiply by the corresponding value.
  - **File:** [`Exercicios28a35.py`](./Exercicios28a35.py)
</details> 

### 32. Exercise 32 Leap year
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that reads any year and states whether it is a leap year.
  - **Objective:** Determines whether a provided year (or the current year) is a leap year based on the rules: divisible by 4, not by 100, or divisible by 400.
  - **Simulated Interface:** The user inputs a year (integer) or 0 to use the current year; the program displays whether the year is a leap year (green) or not (red).
  - **Code Logic:** Application of the datetime library to retrieve the current year, using conditionals with logical operators (and, or) to apply leap year rules.
  - **File:** [`Exercicios28a35.py`](./Exercicios28a35.py)
</details> 

### 33. Exercise 33 Largest smallest
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that reads three numbers and shows which is the largest and which is the smallest.
  - **Objective:** Identifies and displays the smallest and largest values among three provided numbers.
  - **Simulated Interface:** The user inputs three integers; the program displays the smallest value (in red) and the largest value (in green).
  - **Code Logic:** Application of conditional structures with comparisons to determine the smallest and largest among the three numbers, storing them in variables and updating as necessary.
  - **File:** [`Exercicios28a35.py`](./Exercicios28a35.py)
</details> 

### 34. Exercise 34 Salary increase
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** A program that asks for an employee's salary and calculates their raise amount. For salaries above R$1250.00, calculate a 10% raise. For salaries less than or equal to that, the raise is 15%.
  - **Objective:** Calculates the new salary after applying a percentage increase based on whether the original salary exceeds a given threshold (R$1250.00).
  - **Simulated Interface:** The user inputs an integer (salary in reais); the program displays the updated salary (in reais, highlighted in green) after applying either a 10% or 15% increase.
  - **Code Logic:** Application of an if/else conditional structure to compare the salary against R$1250 and apply the corresponding percentage raise calculation (sal + sal * percentage / 100).
  - **File:** [`Exercicios28a35.py`](./Exercicios28a35.py)
</details> 

### 35. Exercise 35 Check triangle
<details>
  <summary><b>Click to expand project details</b></summary>
  
  - **Task:** Program that reads the length of three lines and tells the user whether or not they can form a triangle.
  - **Objective:** Checks whether three line segments satisfy the triangle inequality theorem (the sum of any two sides must be greater than the third side).
  - **Simulated Interface:** The user inputs three integers (lengths of the line segments); the program displays "can form" in green or "cannot form" in red.
  - **Code Logic:** Application of a compound conditional structure with logical operators (and) to test all three triangle inequalities simultaneously.
  - **File:** [`Exercicios28a35.py`](./Exercicios28a35.py)
</details> 
