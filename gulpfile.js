var gulp = require('gulp');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var imagemin = require('gulp-imagemin');
var rename = require('gulp-rename');
var cleanCSS = require('gulp-clean-css');


var paths = {
    dev: {
        node: 'node_modules/',
        semantic: 'static-dev/semantic/'
    },
    productoin: {
        vendor: 'static/vendor/'
    }
};


gulp.task('build', function () {
    // js
    gulp.src(paths.dev.node + 'noty/lib/noty.min.js')
        .pipe(uglify()).pipe(gulp.dest(paths.productoin.vendor + 'noty'));
    gulp.src(paths.dev.node + 'jquery/dist/jquery.min.js')
        .pipe(uglify()).pipe(gulp.dest(paths.productoin.vendor + 'jquery'));
    gulp.src(paths.dev.semantic + 'dist/semantic.min.js')
        .pipe(uglify()).pipe(gulp.dest(paths.productoin.vendor + 'semantic'));


    // css
    gulp.src(paths.dev.node + 'noty/lib/noty.css')
        .pipe(cleanCSS()).pipe(rename('noty.min.css')).pipe(gulp.dest(paths.productoin.vendor + 'noty'));
    gulp.src(paths.dev.semantic + 'dist/{themes/**,semantic*min.css}')
        .pipe(gulp.dest(paths.productoin.vendor + 'semantic'));
});

gulp.task('default', ['build']);