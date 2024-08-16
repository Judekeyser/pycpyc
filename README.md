# License

MIT License

Copyright (c) 2024 Judekeyser

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# PycPyc

Boilerplate project for Python and C. It uses the built-in `ctypes` module.

See : https://docs.python.org/3/library/ctypes.html

## Further work

### Make a Cython alternative

Or maybe not. Advantage of `ctypes` is that it doesn't require a build process.

### Make sure the example works on other platforms

Currently we have to hardcode the extension of libraries, which doesn't sound convenient for usages on other platforms. There should be a way to detect the platform at runtime, and decide for the best extension to look for. Should we make a small configuration file for both the extension and the library location?