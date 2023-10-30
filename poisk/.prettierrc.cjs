module.exports = {
    trailingComma : 'all',
   tabWidth      : 4,
   semi          : false,
   singleQuote   : true,
   arrowParens   : 'always',
   quoteProps    : 'consistent',
   endOfLine     : 'auto',
   overrides     : [

        {
            files: '*.{json,yml,md}',
            options: {
                tabWidth: 2,
            },
        },
        {
            files: '*.{ts,tsx}',
            options: {
                parser: 'typescript',
            },
        },
    ],
}
