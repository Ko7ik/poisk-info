/** Для запрета приватных путей */
const DENIED_PATH_GROUPS = [
    // Private imports are prohibited, use public imports instead
    'app/**',
    'pages/**',
    'features/**',
    'shared/*/**',
    'models.gen',
    '../**/app',
    '../**/pages',
    '../**/features',
    '../**/shared',
    '../**/models',
]

module.exports = {
    parser: '@babel/eslint-parser',
    parserOptions: {
        ecmaVersion: 2020,
        ecmaFeatures: {
            jsx: true,
            modules: true,
        },
        sourceType: 'module',
    },
    env: {
        browser: true,
        es6: true,
    },
    plugins: ['react', 'simple-import-sort'],
    extends: [
        'react-app',
        'eslint:recommended',
        'plugin:import/errors',
        'plugin:import/warnings',
        'plugin:prettier/recommended',
        'plugin:react/recommended',
        'plugin:react/jsx-runtime',
        'plugin:react-hooks/recommended',
        'prettier',
    ],
    rules: {
        // imports
        'simple-import-sort/imports': [
            'error',
            {
                groups: [
                    ['^react'],
                    ['^antd'],
                    ['^@?\\w'],
                    ['^shared*|^pages*|^features*|^widgets*|^models'],
                    ['@/(.*)'],
                    ['^[./]'],
                ],
            },
        ],
        'import/export': 0,
        'import/first': 2,
        'import/no-unresolved': 0, // относительный путь
        'no-restricted-imports': [2, { patterns: DENIED_PATH_GROUPS }],
        // 'linebreak-style': ['error', 'unix'],
        // variables
        'prefer-const': 2, // не используемые переменные
        'no-var': 2, // без var
        'no-unused-vars': 1,
        // base
        'camelcase': [
            1,
            {
                ignoreDestructuring: true,
                ignoreImports: true,
                properties: 'never',
            },
        ],
        'no-else-return': 2, // нормальный return в if else
        'max-len': [1, { code: 120 }],
        'dot-notation': 2, // var x = foo["bar"]; не хорошо
        'eol-last': 2, // новая строка в непустом файле
        // alert, console
        'no-alert': 2, // нет алертам
        'no-console': 0, // console в коде
        // equals
        'eqeqeq': 1, // три равно ===
        'no-eq-null': 2, // сравнение с null через ===
        // function
        'max-params': [1, 2], // колво параметров в функции
        // 'max-lines-per-function': [1, 48], // длина строк в функции
        'arrow-parens': [2, 'always'], // скобки в одиночный аргументах
        //react
        'react/prop-types': 0, // проверка типов
        'react/react-in-jsx-scope': 0,
        // 'no-multi-spaces': 2,
        // 'jsx-quotes': [2, 'prefer-double'],
    },
}
