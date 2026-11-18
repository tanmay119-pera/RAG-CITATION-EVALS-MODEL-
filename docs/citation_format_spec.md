# Verifiable Citation Format Specification

## Syntax
Every factual assertion must terminate with an inline bracketed citation tag:
```text
[<file_stem>_p<page_number>_c<chunk_index>]
```

## Example
> Students may add or drop semester-length courses during the first twelve days without penalty `[handbook_p1_c2]`.

## Verification Algorithm
1. Extract tags using regex pattern: `r"\[([a-zA-Z0-9_\.-]+)\]"`
2. Verify candidate IDs against active retrieved chunk ID set:
   ```python
   is_valid = len(invalid_ids) == 0 and len(valid_ids) > 0
   ```
3. Flag any uncited sentences exceeding 4 words.
