odoo.define('resume_screening.custom_animations', function (require) {
'use strict';

var publicWidget = require('web.public.widget');

publicWidget.registry.JobApplicationAnimation = publicWidget.Widget.extend({
    selector: '.o_job_application_form',

    start: function () {
        this._super();
        this.$('.o_job_application_form').addClass('fade-in');
    },
});

});
