cmd_/home/pi/Documents/ModulosKernel/pruebaProc/suma.o := gcc -Wp,-MD,/home/pi/Documents/ModulosKernel/pruebaProc/.suma.o.d  -nostdinc -isystem /usr/lib/gcc/arm-linux-gnueabihf/6/include -I./arch/arm/include -I./arch/arm/include/generated  -I./include -I./arch/arm/include/uapi -I./arch/arm/include/generated/uapi -I./include/uapi -I./include/generated/uapi -include ./include/linux/kconfig.h -D__KERNEL__ -mlittle-endian -Wall -Wundef -Wstrict-prototypes -Wno-trigraphs -fno-strict-aliasing -fno-common -fshort-wchar -Werror-implicit-function-declaration -Wno-format-security -std=gnu89 -fno-PIE -fno-dwarf2-cfi-asm -fno-omit-frame-pointer -mapcs -mno-sched-prolog -fno-ipa-sra -mabi=aapcs-linux -mfpu=vfp -funwind-tables -marm -D__LINUX_ARM_ARCH__=7 -march=armv7-a -msoft-float -Uarm -fno-delete-null-pointer-checks -Wno-frame-address -O2 --param=allow-store-data-races=0 -DCC_HAVE_ASM_GOTO -Wframe-larger-than=1024 -fno-stack-protector -Wno-unused-but-set-variable -Wno-unused-const-variable -fno-omit-frame-pointer -fno-optimize-sibling-calls -fno-var-tracking-assignments -pg -Wdeclaration-after-statement -Wno-pointer-sign -fno-strict-overflow -fno-merge-all-constants -fmerge-constants -fno-stack-check -fconserve-stack -Werror=implicit-int -Werror=strict-prototypes -Werror=date-time -Werror=incompatible-pointer-types -Werror=designated-init  -DMODULE  -DKBUILD_BASENAME='"suma"'  -DKBUILD_MODNAME='"hello"' -c -o /home/pi/Documents/ModulosKernel/pruebaProc/.tmp_suma.o /home/pi/Documents/ModulosKernel/pruebaProc/suma.c

source_/home/pi/Documents/ModulosKernel/pruebaProc/suma.o := /home/pi/Documents/ModulosKernel/pruebaProc/suma.c

deps_/home/pi/Documents/ModulosKernel/pruebaProc/suma.o := \
  include/linux/compiler_types.h \
    $(wildcard include/config/have/arch/compiler/h.h) \
    $(wildcard include/config/enable/must/check.h) \
    $(wildcard include/config/enable/warn/deprecated.h) \
  include/linux/compiler-gcc.h \
    $(wildcard include/config/arch/supports/optimized/inlining.h) \
    $(wildcard include/config/optimize/inlining.h) \
    $(wildcard include/config/retpoline.h) \
    $(wildcard include/config/gcov/kernel.h) \
    $(wildcard include/config/arch/use/builtin/bswap.h) \

/home/pi/Documents/ModulosKernel/pruebaProc/suma.o: $(deps_/home/pi/Documents/ModulosKernel/pruebaProc/suma.o)

$(deps_/home/pi/Documents/ModulosKernel/pruebaProc/suma.o):
