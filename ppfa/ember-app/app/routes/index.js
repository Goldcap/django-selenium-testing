import Ember from "ember";
import OperisPpfatestsRoute from "ember-app/routes/operis-ppfa-tests";

var IndexRoute = OperisPpfatestsRoute.extend({
    
    actions: {
        
        updateTest: function() {
            this.modelFor('test').reload();
        },
        
        refresh: function() {
             //console.log(this.modelFor('index'));
             this.modelFor('runs').forEach(function(item){
                item.reload();
             });
             this.modelFor('index').forEach(function(item,id){
                item.reload();
             });
        }
    }
        
});

export default IndexRoute;