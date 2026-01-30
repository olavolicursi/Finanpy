/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './templates/**/*.html',
        './static/**/*.js',
    ],
    theme: {
        extend: {
            colors: {
                'cyan': {
                    500: '#06b6d4',
                },
                'emerald': {
                    500: '#10b981',
                },
                'gray': {
                    900: '#111827',
                    950: '#030712',
                }
            },
        },
    },
    plugins: [],
}
