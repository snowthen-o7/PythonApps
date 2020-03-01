# PythonApps
Smaller individual Python apps I've made in my freetime.


## Website Blocker
Blocks a customizable list of sites from being accessible at adjustable time ranges in order to boost productivity during hours of your choosing.


## Web Map Generator
Ingests JSONs and delimited files containing geographic data such as population, altitude, latitude/longitude, etc, and plots it in an html file for easy in-browser viewing.


## Dictionary Generator, or Lists of Lists Combiner

This script combines each list from each column into one column.
The result is one list with each index of that final list
containing all the values that were in that index in the other lists.

Particularly useful in concatenating lists of years, makes, and models
that automotive parts were compatible with. 

This also deduplicates entries.

<details>
<summary>Parameters:</summary>
<ul>
<li>CSV file containing any number of columns</li>
<li>Each column contains a list of values, separated by ' > '</li>
<li>Assumes the length of each list in each column is equal</li>
<li>Like indices are concatenated using ':'</li>
<li>Indices are separated by ','</li></ul>
</details>

Example input:
<table>
<tr>
  <th>PRIMARY_KEY</th>
  <th>list_1</th>
  <th>list_2</th>
  <th>list_3</th>
</tr>
<tr>
  <td>001</td>
  <td>A > B > C</td>
  <td>D > E > F</td>
  <td>X > Y > Z</td>
</tr>
</table>

Final output:
<table>
<tr>
  <th>PRIMARY_KEY</th>
  <th>final_list</th>
</tr>
<tr>
  <td>001</td>
  <td>A:D:X,B:E:Y,C:F:Z</td>
</tr>
</table>
