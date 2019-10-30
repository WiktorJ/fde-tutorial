### Hints
To get code base for this exercise run `git clone https://gitlab.db.in.tum.de/Josef/tpchjoin`

If you are not familiar with `git` I highly recommend to learn it. 
You can take a simple tutorial for example [here](https://rogerdudler.github.io/git-guide/)

Description of TPC-H dataset can be found [here](http://www.tpc.org/tpc_documents_current_versions/pdf/tpc-h_v2.18.0.pdf)
In particular on the page 13 TPC-H Schema from which we can find out that the `EXTENDEDPRICE` is 6th field in `LINEITEM` table.

### GNU utils
Now, we can implement the solution for the exercise using AWK in following way:

`awk -F '|' 'START {sum=0}{sum=sum+$6} END {print sum}' lineitem.tbl`

If you encounter some errors you can try to run like that:

`LC_NUMERIC=C awk -F '|' 'START {sum=0}{sum=sum+$6} END {print sum}' lineitem.tbl`

it will make the `awk` recognize `.` as decimal point.

### C++

In this exercise whole structure is prepared beforehand. 
However, the structure of `sum.cpp` is a bit misleading and the easiest solution is to modify the whole file
instead of just adding code in marked place i.e.
```c++
int64_t ToInt(std::string_view s) {
     int64_t result = 0;
     for (auto c : s) {
         if (c != '.') {
             result = result * 10 + (c - '0');
         }
     }
     return result;
 }
 
 int64_t sum_extendedprice(const std::string& file_name) {
     std::ifstream f(file_name);
     CsvParser lineitem = CsvParser(f).delimiter('|');
 
     int64_t price_sum = 0;
     for (auto row : lineitem) {
             price_sum += ToInt(row[5]);
     }
 
     return price_sum;
 }
```

After implementation you should follow the instructions in the README.md to build the project.

The following instruction from the exercise:
> It is advisable to compile your program with debug information (add the -g argument for g++) in order
> to obtain the original code lines together with the corresponding symbols.`

Is equivalent to passing `-DCMAKE_BUILD_TYPE=Debug` flag for cmake, so again just use the command from README.md.

#### Rebuilding the project

After you make some changes in your code, you have to run `make` command again to re-compile the code. 
It is not necessary to run cmake again (cmake **does not**  compile any of your code)  


### Profiling

The most important commands are

`perf record main lineitem.tbl`

and 

`perf report`

Those will give you the information about which part of the code should be optimized (we will do it next week)

#### Profiling on Mac

`perf` does not work on mac. There are several tools you can use instead. However, by far the easiest to use (and very good at the same time) is `dtrace` in `Clion`.

* Clion is C++ IDE from JetBrains. It is a very powerful tool for C++ programming and profiling the code is just one of many features of this program. Personally, I recommend JetBrains tools for (almost) every programming language. You can download the Clion [here](https://www.jetbrains.com/clion/). As students you can get full version for free.

* Instructions on how to profile C++ code on Mac within Clion can be found [here](https://www.jetbrains.com/help/clion/cpu-profiler.html)