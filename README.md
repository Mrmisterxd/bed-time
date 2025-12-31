<div align="center">
<h1> <a href="https://github.com/Mrmisterxd/bed-time/tree/main">BedTime</a> </h1> 

<p>This program is needed to make it easier to set the bedtime, instead of using the inconvenient command in Win+R. The program makes this process more convenient.</p>

</div>

## ℹ️ How to use the program?
- Download the [`.exe`](https://github.com/Mrmisterxd/bed-time/releases/tag/v1.2) file from the repository, double-click the file, and you can use the script!
- The script is used like a standard [`.py`](https://github.com/Mrmisterxd/bed-time/blob/main/Bedtime.py) file.
- The .exe is simply a compiled .py file created using pyinstaller.
- The following libraries are needed:

<details>
  
  <summary>Library List:</summary>
  
```
altgraph==0.17.4
colorama==0.4.6
keyboard==0.13.5
packaging==25.0
pefile==2023.2.7
pyinstaller==6.16.0
pyinstaller-hooks-contrib==2025.9
pywin32-ctypes==0.2.3
setuptools==80.9.0
```

> - Also You can also see the list of required libraries in the [`requirements.txt`](https://github.com/Mrmisterxd/bed-time/blob/main/requirements.txt) file.
</details>

- Alternatively, you can use the .py file in any other [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment) (for example, [VS Code](https://en.wikipedia.org/wiki/Visual_Studio_Code_)).

## ℹ️ Description of choosing:
### `1. Set bedtime in seconds` 
- Sets a sleep timer for Windows in seconds. 
*It executes the command in Win+R; your value = `"shutdown -s -t <your value>"` entered in Win+R is in seconds.*

### `2. Turn off bedtime` 
- Turns off the sleep timer. 
*The meaning of this command in Win+R is `"shutdown -a"`*

### `3. Set bedtime in hours` 
- Sets a sleep timer for Windows in hours.
*It executes the command in Win+R; your value in `"shutdown -s -t <your value>"` will be seconds multiply 3600.*

### `4. Set bedtime in minutes` 
- Sets a sleep timer for Windows in minutes.
*It executes the command in Win+R; your value in `"shutdown -s -t <your value>"` will be seconds multiply 60.*

### `5.🎲 Russian roulette` - 
> [!CAUTION]
> ### Russian Roulette: you are given two numbers to choose from, the chance of choosing the first number is 50 percent, the second number is also 50 percent, and with a 50/50 chance your computer may <ins>***INSTANTLY SHUT DOWN❗❗❗***</ins>
> 
-  ### <ins>***The author is not responsible for this.***</ins>
>  [!CAUTION]
> ### With a 50/50 chance, the command "shutdown -s -t" will be **executed**, which is equivalent to an ***immediate*** computer *shutdown*. 

> [!IMPORTANT]
> ### ***Before using option 5, make <ins>**sure**</ins> you have saved important data and will not suffer any damage/risk if your computer shuts down instantly without confirmation.*** (This is the dealer's bet!)

### `6. Check bedtime` 
>[!IMPORTANT]
> ### Displays the timer set during the current session. It cannot detect timers set via Win+R or previous script runs or another script/programm.
-  This item is <ins>***ONLY***</ins> needed to calm your mind after you set the sleep time or disable it (<ins>***During the first program launch, only after selecting any of the preceding options❗***</ins>).
-  *If* you set the sleep time during a different previous launch of this program this information is also *incorrect*.
-  As I said, the information is ***only*** valid during a single program launch. *If* you set the sleep time using Win+R, this is ***also***  *incorrect*.
>[!NOTE]
>### All correct information is:
> - 1 - only after selecting any of the options
> - 2 - only during a single program launch.

### `7. Exit`
- Closes the entire script and exits the script completely.
>[!NOTE]
> ### After you exit the program, your timer remains active, as all commands are integrated into Windows.

## ℹ️ Compatibility with operating systems:
- This program is only compatible with Windows
> Windows XP, Vista, 7, 8, 8.1, 10, 11

## ⚖️ Licensing

The project is distributed under the [MIT License](https://github.com/Mrmisterxd/bed-time/blob/main/LICENSE)
