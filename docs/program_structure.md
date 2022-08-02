# Program Structure

Modes (Menu, Practice, Modify Dict, Personal Statistics, Change User, Quit)
  ^
  |
 Menu <-> TUI <-> User

Menu -> (Special list other modes)

Practice		-> Reads dictionary
			   Displays questions	-> Ask question, inform result
			   Tallies results
			   Saves results

Modify Dict		-> List options		-> Add entry
						   Remove entry
						   Modify entry
						   Read entries from storage (auto?)
						   Save entries to storage (auto?)

Personal Statistics	-> Display overall statistics (Correct, wrong, total, best words, worst words)
			   Display individual statistics	-> Per word stats (Correct, wrong, total, first seen, last seen)

Change User		-> Select user
			   Create user
			   Delete user

Quit			-> Are you sure?		-> Yes
							   No
