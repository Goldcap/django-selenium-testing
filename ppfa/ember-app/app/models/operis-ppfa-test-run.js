import Ember from 'ember';
import DS from "ember-data";

var OperisPpfatestrun = DS.Model.extend(Ember.Validations.Mixin,{
  ppfa_test: DS.belongsTo('ppfa_test'),
  date_created: DS.attr('isodate'),
  status: DS.attr('boolean'),
  ppfa_test_assertions: DS.hasMany('ppfa_test_assertions',{async:true})
});
export default OperisPpfatestrun;