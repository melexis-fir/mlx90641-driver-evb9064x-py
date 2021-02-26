.PHONY: clean all

ifeq ($(OS),Windows_NT)
    detected_OS := Windows
else
    detected_OS := $(shell sh -c 'uname 2>/dev/null || echo Unknown')
endif


DEP_LIBS:=
SHARED_LIB_NAME:=mlx90641_driver_evb9064x
STATIC_LIB_NAME:=mlx90641_driver_evb9064x_static

STATIC_LIB_FILE:=lib$(STATIC_LIB_NAME).a
SHARED_LIB_FILE:=lib$(SHARED_LIB_NAME).so

ifeq ($(detected_OS),Windows)
MACHINE:=windows
SHARED_LIB_FILE:=$(SHARED_LIB_NAME).dll
else
MACHINE:=$(shell uname -m)
endif

CFLAGS:=-Wall -Wextra -Wstrict-prototypes -Wunused-result -Wno-stringop-truncation -O3 -std=c99 -fmessage-length=0 -fPIC -I../libs -Iinc


all: $(SHARED_LIB_FILE) $(STATIC_LIB_FILE)

clean:
	rm -f main *.o
	rm -f src/*.o
	rm -f $(SHARED_LIB_FILE) $(STATIC_LIB_FILE)

main.o: main.c
	gcc -c -o $@ $(CFLAGS) $^

src/m_sp.o: src/m_sp.c
	gcc -c -o $@ $(CFLAGS) $^

src/evb9064x.o: src/evb9064x.c
	gcc -c -o $@ $(CFLAGS) $^

src/MLX90641_I2C_Driver_evb9064x.o: src/MLX90641_I2C_Driver_evb9064x.c
	gcc -c -o $@ $(CFLAGS) $^

main: main.o src/MLX90641_I2C_Driver_evb9064x.o src/m_sp.o src/evb9064x.o
	gcc -o $@ $^ -lm -Wl,-rpath=../libs/$(MACHINE) -L../libs/$(MACHINE) $(DEP_LIBS)


$(SHARED_LIB_FILE): src/MLX90641_I2C_Driver_evb9064x.o src/m_sp.o src/evb9064x.o
	gcc -shared -o $@ $^ -L../libs/$(MACHINE) $(DEP_LIBS) -Wl,-rpath=../libs/$(MACHINE)
	@mkdir -p ../libs/$(MACHINE)
	@cp -fv $@ ../libs/$(MACHINE)

$(STATIC_LIB_FILE): src/MLX90641_I2C_Driver_evb9064x.o src/m_sp.o src/evb9064x.o
	ar rcu $@ $<
	@mkdir -p ../libs/$(MACHINE)
	@cp -fv $@ ../libs/$(MACHINE)
