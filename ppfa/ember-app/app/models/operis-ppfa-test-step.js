import Ember from 'ember';
import DS from "ember-data";

var OperisPpfateststep = DS.Model.extend(Ember.Validations.Mixin,{
  subject: DS.attr('string'),
  verb: DS.attr('string'),
  object: DS.attr('string'),
  ppfa_test: DS.belongsTo('ppfa_test')
});
export default OperisPpfateststep;