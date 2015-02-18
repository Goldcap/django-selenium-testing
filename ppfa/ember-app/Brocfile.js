/* global require, module */

var EmberApp = require('ember-cli/lib/broccoli/ember-app');

var app = new EmberApp();

// Use `app.import` to add additional libraries to the generated
// output files.
//
// If you need to use different assets in different
// environments, specify an object as the first parameter. That
// object's keys should be the environment name and the values
// should be the asset to use in that environment.
//
// If the library that you are including contains AMD or ES6
// modules that you would like to import into your application
// please specify an object with the list of modules as keys
// along with the exports of each module as its value.
                                                   
app.import('vendor/pikaday/pikaday.js');
app.import('vendor/ember-easyForm/dist/ember-easyForm.min.js');      
app.import('vendor/ember-validations/dist/ember-validations.min.js'); 
app.import('vendor/jquery-csrf/jquery.csrf.js'); 
app.import('vendor/sprintf/dist/sprintf.min.js'); 
app.import('vendor/moment/moment.js');            
app.import('vendor/foundation/js/foundation/foundation.js');    
app.import('vendor/foundation/js/foundation/foundation.offcanvas.js'); 

// Import a couple of modules;
var mergeTrees  = require('broccoli-merge-trees');
var pickFiles = require('broccoli-static-compiler');
var compileSass = require('broccoli-sass');

var appFonts = pickFiles('vendor/components-font-awesome/fonts', {
  srcDir: '/',
  files: ['*'],
  destDir: '/assets/fonts'
});

var pikadayFiles = pickFiles('vendor/pikaday', {
  srcDir: '/css',
  files: ['*'],
  destDir: '/assets'
});

// List all of the directories containing SASS source files
var sassSources = [
  'app/styles',
  'vendor/foundation/scss',
  'vendor/components-font-awesome/scss'
]

// Compile a custom sass file, with the sources that need to be included
var appCss = compileSass( sassSources , 'app_custom.scss', 'assets/app.css');


// Merge the ember app and the custom css into a single tree for export
var appAndCustomDependencies = mergeTrees([app.toTree(),appCss,appFonts,pikadayFiles], {
  overwrite: true
});

// EXPORT ALL THE THINGS!
module.exports = appAndCustomDependencies;

//module.exports = app.toTree();
