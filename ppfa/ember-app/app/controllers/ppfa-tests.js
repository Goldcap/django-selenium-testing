//import Ember from "ember";
import OperisPpfatestsController from 'ember-app/controllers/operis-ppfa-tests';

var PpfatestsController = OperisPpfatestsController.extend({
    actions: {
        show_runs: function( ppfa_test ) {
            ppfa_test.get('ppfa_test_runs');
        }
    }
});

export default PpfatestsController;  