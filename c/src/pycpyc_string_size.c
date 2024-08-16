/* String Size module
 * ==================
 * Compute the length of a short C-String.
 */


int pycpyc_string_size(const char *);


#ifdef PYCPYC_STRING_SIZE_IMPL

int pycpyc_string_size(const char *string)
{
	int length = 0;
	while(length < 32767) {
		if(*string) {
			string++;
			length++;
		} else {
			return length;
		}
	}
	return -1;
}

#endif
