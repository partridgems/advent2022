import sys

# Returns (count, source, to) where:
#   count is the number of iterations,
#   source is the source stack, and
#   target is the target stack
#
#   Lastly, 0-index all of the indices.
def parse_command(command):
  # Parsing "move XX from YY to ZZ"
  commands = command.split(' ')
  return (int(commands[1]), int(commands[3]) - 1, int(commands[5]) - 1)

# Parse the starting config data.
def parse_starting_config(start_lines):
  # Num stacks is 4 characters ("[X] ") per crate, minus one.
  num_stacks = (len(start_lines[0]) + 1) // 4
  crates = [[] for _ in range(num_stacks)]
  # We don't need the index line.
  start_lines = start_lines[:-1]
  for line in start_lines:
    for stack_i in range(num_stacks):
      crate_location = stack_i * 4 + 1
      if line[crate_location] != " ":
        # We're inserting top-to-bottom, so insert newest at the bottom
        crates[stack_i].insert(0, line[crate_location])
  return crates

# Parse just the starting lines
starting_lines = []
crates = []
reading_starting_config = True
for line in sys.stdin.readlines():
  line = line[:-1]
  if not line:
    # Finished starting config. Parse it.
    reading_starting_config = False
    crates = parse_starting_config(starting_lines)
    print("Starting crates:\n", crates)
  elif reading_starting_config:
    starting_lines.append(line)
  else:
    # Now we're moving crates around
    (count, source, target) = parse_command(line)
    # Part 1: one crate at a time.
    # for _ in range(count):
    #   crates[target].append(crates[source].pop())
    # Part 2: multiple crates. We'll just pop them to a temporary stack. Sorry,
    # Knuth.
    moved_slug = []
    for _ in range(count):
      moved_slug.append(crates[source].pop())
    for crate in reversed(moved_slug):
      crates[target].append(crate)

print("Ending crates:\n", crates)

print("Tops are: ", ''.join([crate[-1] for crate in crates]))
