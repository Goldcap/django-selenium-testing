import OperisPpfatestrun from 'ember-app/models/operis-ppfa-test-run';

var Ppfatestrun = OperisPpfatestrun.extend({
    
    isRunning: false,
    
    running: function() {
        return (this.get('isRunning')) ? "( Running )" : "";
    }.property('isRunning')
});

export default Ppfatestrun;