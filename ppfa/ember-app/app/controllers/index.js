import Ember from "ember";
import OperisPpfatestsController from 'ember-app/controllers/operis-ppfa-tests';
//https://gist.github.com/aloysius-lim/c793c1383fb17e3f4410

var IndexController = OperisPpfatestsController.extend({
    
    queryParams: ['page'],
    needs: ['runs'],
    
    actions: {
        show_runs: function( ppfa_test ) {
            ppfa_test.get('ppfa_test_runs');
        },
        
        runRun: function( ppfa_test ) {
            
            var scope = this;
            var ppfa_test_run = this.store.createRecord('ppfa_test_run',{
                "ppfa_test": ppfa_test,
                "isRunning":true
            });
            
            ppfa_test_run.save().then(function(ppfa_test_run){
                return ppfa_test.save().then(function() {
                    return ppfa_test_run;
                });
            })
            .then(function() {
                var data = {"location":ppfa_test.get('location'),"run":ppfa_test_run.get('id')};
                var params = {  url:'/api/ppfaTestRunExec',
                                data:data,
                                cache: false,
                                dataType: 'json'
                                };
                return Ember.$.ajax(params);
            })
            .then(function(response) {
                Ember.Logger.info(ppfa_test_run);
                ppfa_test_run.set("isRunning",false);
                ppfa_test_run.set("status",response.status);
                //scope.send("updateTest");
                return ppfa_test_run.save().then(function(){
                    return ppfa_test.save();
                });
            });
            
        },
        
        addRun: function( ppfa_test ) {
            var scope = this;
            var ppfa_test_run = this.store.createRecord('ppfa_test_run',{
                "ppfa_test": ppfa_test
            });
            
            ppfa_test_run.save().then(function() {
                return ppfa_test.save();
            });
        },
        
        editRun: function( ppfa_test ) {
            this.transitionToRoute('test.edit',ppfa_test);
        },
        
        deleteRun: function( ppfa_test ) {
            var scope = this;
            ppfa_test.destroyRecord().then(function(ppfa_test) {
                scope.set('deleted',ppfa_test);
                scope.transitionToRoute('index');
            });
        }
    }
});

export default IndexController;  