
# Variables
playing around with Variables

## Lessons Learned

I learned how to use variables, and bult-in functions 


## Usage/Examples

```import math

#Day 2: 30 Days of python programming

#EXERCISE 1

first_name = "Marlon"
last_name = "Rivera"
full_name = "Marlon Gabriel Rivera Martinez"
country = "Italy"
city = "venice"
age = 23
year = 2024
is_married = False
is_true = True
is_light_on = False
this, is_another, person,edad, casada = "esta", "es", "Laura", 26, False 

#EXERCISE 2

type(first_name)
type(last_name)
type(full_name)
type(country)
type(city)
type(age)
type(year)
type(is_married)
type(is_true)
type(is_light_on)
type(this)
type(is_another)
type(person)
type(edad)
type(casada)


print(len(first_name))
print(len(last_name))
dife = len(first_name) - len(last_name)
print(f"there is no difference in the length of both my name: {dife}")


num_one = 5
num_two = 4

total = num_one + num_two

diff = num_two - num_two

product = num_two * num_one

division = num_one / num_two

remainder = num_two % num_one

exp = num_one ** num_two

floor_division = num_one // num_two

# the radius of a circle is 30 meters
PI = 3.14159

area_of_circle = PI * math.pow(30, 2)
circum_of_circle = 2 * PI * 30

#input return a string and we need an real number so math.pow can work
radius = input("please give me a radius: ")
#so we transform it with the built-in function int()
transform = int(radius)
area_calculated = PI * math.pow(transform, 2)


print(f"the area of 30 meter radius circle is: {area_of_circle}")
print(f"the circumference of a 30 meter radius circle is: {circum_of_circle}")
print("----------------------------")
print(f"the area of the circle that you gave me is: {area_calculated}")



name_user = input(f"please enter you name: ")
last_user = input(f"please enter your last name: ")
country_user = input("please enter your country of citizenchip: ") 
age_user = input(f"please enter your age: ")

print(f"here it is the info that you gave me: {name_user}, {last_name}, {country_user}, {age_user}")
```


## FAQ

#### Exercise 3

GNU bash, version 5.2.15(1)-release (x86_64-pc-linux-gnu)
These shell commands are defined internally.  Type `help' to see this list.
Type `help name' to find out more about the function `name'.
Use `info bash' to find out more about the shell in general.
Use `man -k' or `info' to find out more about commands not in this list.

A star (*) next to a name means that the command is disabled.

 job_spec [&]                                                                               history [-c] [-d offset] [n] or history -anrw [filename] or history -ps arg [arg...]
 (( expression ))                                                                           if COMMANDS; then COMMANDS; [ elif COMMANDS; then COMMANDS; ]... [ else COMMANDS; ] fi
 . filename [arguments]                                                                     jobs [-lnprs] [jobspec ...] or jobs -x command [args]
 :                                                                                          kill [-s sigspec | -n signum | -sigspec] pid | jobspec ... or kill -l [sigspec]
 [ arg... ]                                                                                 let arg [arg ...]
 [[ expression ]]                                                                           local [option] name[=value] ...
 alias [-p] [name[=value] ... ]                                                             logout [n]
 bg [job_spec ...]                                                                          mapfile [-d delim] [-n count] [-O origin] [-s count] [-t] [-u fd] [-C callback] [-c qua>
 bind [-lpsvPSVX] [-m keymap] [-f filename] [-q name] [-u name] [-r keyseq] [-x keyseq:sh>  popd [-n] [+N | -N]
 break [n]                                                                                  printf [-v var] format [arguments]
 builtin [shell-builtin [arg ...]]                                                          pushd [-n] [+N | -N | dir]
 caller [expr]                                                                              pwd [-LP]
 case WORD in [PATTERN [| PATTERN]...) COMMANDS ;;]... esac                                 read [-ers] [-a array] [-d delim] [-i text] [-n nchars] [-N nchars] [-p prompt] [-t tim>
 cd [-L|[-P [-e]] [-@]] [dir]                                                               readarray [-d delim] [-n count] [-O origin] [-s count] [-t] [-u fd] [-C callback] [-c q>
 command [-pVv] command [arg ...]                                                           readonly [-aAf] [name[=value] ...] or readonly -p
 compgen [-abcdefgjksuv] [-o option] [-A action] [-G globpat] [-W wordlist] [-F function]>  return [n]
 complete [-abcdefgjksuv] [-pr] [-DEI] [-o option] [-A action] [-G globpat] [-W wordlist]>  select NAME [in WORDS ... ;] do COMMANDS; done
 compopt [-o|+o option] [-DEI] [name ...]                                                   set [-abefhkmnptuvxBCEHPT] [-o option-name] [--] [-] [arg ...]
 continue [n]                                                                               shift [n]
 coproc [NAME] command [redirections]                                                       shopt [-pqsu] [-o] [optname ...]
 declare [-aAfFgiIlnrtux] [name[=value] ...] or declare -p [-aAfFilnrtux] [name ...]        source filename [arguments]
 dirs [-clpv] [+N] [-N]                                                                     suspend [-f]
 disown [-h] [-ar] [jobspec ... | pid ...]                                                  test [expr]
 echo [-neE] [arg ...]                                                                      time [-p] pipeline
 enable [-a] [-dnps] [-f filename] [name ...]                                               times
 eval [arg ...]                                                                             trap [-lp] [[arg] signal_spec ...]
 exec [-cl] [-a name] [command [argument ...]] [redirection ...]                            true
 exit [n]                                                                                   type [-afptP] name [name ...]
 export [-fn] [name[=value] ...] or export -p                                               typeset [-aAfFgiIlnrtux] name[=value] ... or typeset -p [-aAfFilnrtux] [name ...]
 false                                                                                      ulimit [-SHabcdefiklmnpqrstuvxPRT] [limit]
 fc [-e ename] [-lnr] [first] [last] or fc -s [pat=rep] [command]                           umask [-p] [-S] [mode]
 fg [job_spec]                                                                              unalias [-a] name [name ...]
 for NAME [in WORDS ... ] ; do COMMANDS; done                                               unset [-f] [-v] [-n] [name ...]
 for (( exp1; exp2; exp3 )); do COMMANDS; done                                              until COMMANDS; do COMMANDS-2; done
 function name { COMMANDS ; } or name () { COMMANDS ; }                                     variables - Names and meanings of some shell variables
 getopts optstring name [arg ...]                                                           wait [-fn] [-p var] [id ...]
 hash [-lr] [-p pathname] [-dt] [name ...]                                                  while COMMANDS; do COMMANDS-2; done
 help [-dms] [pattern ...]                                                                  { COMMANDS ; }



## Authors

- [@Asabeneh](https://github.com/Asabeneh)

