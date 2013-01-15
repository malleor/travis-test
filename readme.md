### Concept

- **The algorithm is a script file**, exposed to the framework as an importable module.
- The manifest and input/output params are stored globally. 
- The algorithm is identified as `module_name`.

### Pros

- With default values for the `MANIFEST` and `DEF_IN_PARAMS`, the script is extremely easy to write - see `minimal.py`. 

### Cons

- No visible encapsulation of the execution context - the use of global variables.
- The need to maintain `DEF_IN_PARAMS`-`IN_PARAMS` consistency is a potential source of errors. 

Go, Travis!
