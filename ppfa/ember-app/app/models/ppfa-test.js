import OperisPpfatest from 'ember-app/models/operis-ppfa-test';

var Ppfatest = OperisPpfatest.extend({
    
    validations: {
        name: {
          presence: true,
          length: { minimum: 3 }
        },
        location: {
          presence: true,
          length: { minimum: 3 }
        }
      }
      
});

export default Ppfatest;