import Ember from 'ember';
import DS from "ember-data";

var OperisPpfatestassertion = DS.Model.extend(Ember.Validations.Mixin,{
  subject: DS.attr('string'),
  verb: DS.attr('string'),
  object: DS.attr('string'),
  status: DS.attr('boolean'),
  ppfa_test_run: DS.belongsTo('ppfa_test_run'),
  ppfa_test: DS.belongsTo('ppfa_test')
});
export default OperisPpfatestassertion;