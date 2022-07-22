For generate cli command document:   
`python generate_rst.py 'quoted/full_path/to/xoa_driver/internals/core/commands/*_commands.py' > target_filename.rst`

For generate XMP document(json only at the moment):   
`python generate_xmp.py 'quoted/full_path/to/xoa_driver/internals/core/commands/*_commands.py' > target_filename.json`
    
   
`*_commands.py` means the script will search command in files that filename ending with `_commands.py`.   
You may limit single file by change to `p_commands.py`, `c_commands.py` etc..
