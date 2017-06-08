formatter = "%r %r %r %r"
# variable with string %r
# %r will be defined bellow
# "%r" can reed any kind of data

print formatter % (1, 2, 3, 4)
# print variable formatter
# replace the 4 %r in string with % (1, 2, 3, 4)

print formatter % ("one", "two", "three", "four")
# print variable formattter
# replace %rs with   % (one, two, three, four)

print formatter % (True, False, False, True)
# print variable formatter replace with   % ()
# True and False are built-in keywords that don't need quotes

print formatter % (formatter, formatter, formatter, formatter)
# calling formatter variable on its self
# reads the formatter variable literally as text

print formatter % (
   "I had this thing.",
   "That you could type up right.",
   "But it didn't sing.",
   "So I said goodnight."
)
# print variable formatter replaces %r with whats in parentheses
