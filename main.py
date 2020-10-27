
sample_text = "sample.txt"

# this separates the text block by lines as long as every sentence is already on a new line
with open(sample_text) as f:
    lines = [line.rstrip('\n') for line in f]

print(lines)

# A better way is probably to separate by ". "
with open(sample_text) as f:
    sentences = [stce.rstrip('. ') for stce in f]

print(sentences)
