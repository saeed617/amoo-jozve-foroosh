var gulp = require('gulp');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var imagemin = require('gulp-imagemin');
var rename = require('gulp-rename');
var cleanCSS = require('gulp-clean-css');


var paths = {
    dev: {
        node: 'node_modules/',
    },
    productoin: {
        vendor: 'static/vendor/'
    }
};

function noty_js() {
    return gulp.src(paths.dev.node + 'noty/lib/noty.min.js')
        .pipe(uglify()).pipe(gulp.dest(paths.productoin.vendor + 'noty'));
}

function jquery() {
    return gulp.src(paths.dev.node + 'jquery/dist/jquery.min.js')
        .pipe(uglify()).pipe(gulp.dest(paths.productoin.vendor + 'jquery'))
}

function noty_css() {
    return gulp.src(paths.dev.node + 'noty/lib/noty.css')
        .pipe(cleanCSS()).pipe(gulp.dest(paths.productoin.vendor + 'noty'));
}

const js = gulp.series(noty_js, jquery);
const css = gulp.series(noty_css);

exports.default = gulp.series(
    js,
    css
);