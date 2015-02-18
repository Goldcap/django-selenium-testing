import Ember from 'ember';

var Router = Ember.Router.extend({
  location: EmberAppENV.locationType
});

Router.map(function() {
    this.resource('index', { path : "/" }, function() {
        this.resource('test', { path: "/test/:ppfa_test_id"}, function() {
            this.route('add', {path: "/add"});
            this.route('edit', {path: "/edit"});
            this.resource('runs', { path: "/runs"}, function() {
                this.resource('run', { path: "/:ppfa_test_run_id"}, function() {
                    this.resource('assertions', { path: "/assertions"});
                });
            });
            this.resource('steps', { path: "/steps"}, function() {
                this.route('add', {path: "/add"});
                this.route('edit', {path: "/edit/:ppfa_test_step_id"});
            });
        });
    });
    this.resource('ppfa_tests', { path : "/ppfa_tests" }, function() {
        this.route('index');
        this.route('ppfa_test_ppfa_test_runs', { path: "/:ppfa_test_id/runs"});                             
    });
    this.route("ppfa_test", { path : "/ppfa_test/:ppfa_test_id" });
    this.resource('ppfa_test_runs', { path : "/ppfa_test_runs" }, function() {
        this.route('index');                             
    });
    this.route("ppfa_test_run", { path : "/ppfa_test_run/:ppfa_test_run_id" });
    this.resource('ppfa_test_assertions', { path : "/ppfa_test_assertions" }, function() {
        this.route('index');                             
    });
    this.route("ppfa_test_assertion", { path : "/ppfa_test_assertion/:ppfa_test_assertion_id" });
});

export default Router;
