#ifndef _STRING_H
#define _STRING_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
    #endif

    extern void* memset (void * p, int val, size_t len);
    extern void* memcpy (void* to, const void* from, size_t len);

    #ifdef __cplusplus
}
#endif
#endif
