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
    gulp.src(paths.dev.node + 'clipboard/dist/clipboard.min.js')
        .pipe(uglify()).pipe(gulp.dest(paths.productoin.vendor + 'clipboard'));
    gulp.src(paths.dev.node + 'bxslider/dist/jquery.bxslider.min.js')
        .pipe(uglify()).pipe(rename('bxslider.min.js')).pipe(gulp.dest(paths.productoin.vendor + 'bxslider'));

    // css
    gulp.src(paths.dev.node + 'noty/lib/noty.css')
        .pipe(cleanCSS()).pipe(rename('noty.min.css')).pipe(gulp.dest(paths.productoin.vendor + 'noty'));
    gulp.src(paths.dev.semantic + 'dist/{themes/**,semantic*min.css}')
        .pipe(gulp.dest(paths.productoin.vendor + 'semantic'));
    gulp.src(paths.dev.node + 'bxslider/dist/jquery.bxslider.css')
        .pipe(cleanCSS()).pipe(rename('bxslider.min.css')).pipe(gulp.dest(paths.productoin.vendor + 'bxslider'));
});

gulp.task('default', ['build']);