.PHONY: another-app
# not all targets are listed in PHONY

# Might bw correct< but 'build' and 'app' are different targets'
build: main.c
	gcc main.c -o app

# correct np PHONY
app: main.c
	gcc main.c -o app

# incorrect: listed in PHONY
another-app: main.c
	gcc main.c -o another-app