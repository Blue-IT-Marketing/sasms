// import the library
importScripts('/static/sw/sw-toolbox.js');
//Add Critical Resources to cache
toolbox.precache([
    '/',

    '/static/dist/favicons/apple-icon-57x57.png',
    '/static/dist/favicons/apple-icon-60x60.png',
    '/static/dist/favicons/apple-icon-72x72.png',
    '/static/dist/favicons/apple-icon-76x76.png',
    '/static/dist/favicons/apple-icon-114x114.png',
    '/static/dist/favicons/apple-icon-120x120.png',
    '/static/dist/favicons/apple-icon-144x144.png',
    '/static/dist/favicons/apple-icon-152x152.png',
    '/static/dist/favicons/apple-icon-180x180.png',
    '/static/dist/favicons/android-icon-192x192.png',
    '/static/dist/favicons/favicon-32x32.png',
    '/static/dist/favicons/favicon-96x96.png',
    '/static/dist/favicons/favicon-16x16.png',
    '/static/dist/favicons/ms-icon-144x144.png',
    '/static/dist/manifest/manifest.json',

    '/static/bootstrap/css/bootstrap.min.css',
    '/static/dist/css/AdminLTE.min.css',
    '/static/dist/css/skins/skin-blue.min.css',
    '/static/dist/css/font-awesome.min.css',
    '/static/dist/css/ionicons.min.css',
    '/static/dist/css/AdminLTE.min.css',
    '/static/dist/css/skins/skin-blue.min.css',
    '/static/plugins/datatables/dataTables.bootstrap.css',
    'static/plugins/datepicker/datepicker3.css',
    '/static/plugins/timepicker/bootstrap-timepicker.min.css',
    '/static/plugins/bootstrap-slider/slider.css',
    '/static/plugins/ionslider/ion.rangeSlider.skinNice.css',
    '/static/plugins/ionslider/ion.rangeSlider.css',
    '/static/plugins/select2/select2.min.css',
    '/static/plugins/daterangepicker/daterangepicker.css',
    '/static/dist/css/slider.css',


    '/static/plugins/jQuery/jquery-2.2.3.min.js',
    '/static/bootstrap/js/bootstrap.min.js',
    '/static/plugins/slimScroll/jquery.slimscroll.min.js',
    '/static/plugins/fastclick/fastclick.min.js',
    '/static/plugins/datatables/dataTables.bootstrap.min.js',
    '/static/plugins/datatables/jquery.dataTables.min.js',
    '/static/plugins/datepicker/bootstrap-datepicker.js',
    '/static/plugins/timepicker/bootstrap-timepicker.min.js',
    '/static/plugins/chartjs/Chart.min.js',
    '/static/dist/js/tinymce/js/tinymce/tinymce.min.js',
    '/static/plugins/bootstrap-slider/bootstrap-slider.js',
    '/static/plugins/ionslider/ion.rangeSlider.min.js',
    '/static/dist/js/moment.min.js',
    '/static/plugins/select2/select2.full.min.js',
    '/static/plugins/daterangepicker/daterangepicker.js',
    '/static/plugins/iCheck/icheck.min.js',


    '/static/dist/js/pages/admin.js',
    '/static/dist/js/pages/accounts.js',
    '/static/dist/js/pages/contacts.js',
    '/static/dist/js/pages/advertise.js',
    '/static/dist/js/pages/addmanager.js',
    '/static/dist/js/pages/affiliate.js',
    '/static/dist/js/pages/surveys/makepayments.js',
    '/static/dist/js/pages/surveys/thisschedule.js',
    '/static/dist/js/pages/surveys/multichoice.js',
    '/static/dist/js/pages/surveys/thiscontactlist.js',
    '/static/dist/js/pages/thisVerification.js',
    '/static/dist/js/pages/contact/tickets.js',
    '/static/dist/js/pages/advertise/advert.js',
    '/static/dist/js/pages/advertise/directdeposit.js',
    '/static/dist/js/pages/advertise/account.js',
    '/static/dist/js/pages/advertise/newadvert.js',
    '/static/dist/js/pages/affiliate/accountdetails.js',
    '/static/dist/js/pages/affiliate/credits.js',
    '/static/dist/js/pages/affiliate/social.js',
    'static/dist/js/pages/endpoints/userendpoints.js',
    '/static/dist/js/pages/contacts/manage.js',
    '/static/dist/js/pages/contacts/sms.js',
    '/static/dist/js/pages/contacts/contacts.js',
    '/static/dist/js/pages/dashboard/blueitmarketing.js',
    '/static/dist/js/pages/dashboard/bulksms.js',
    '/static/dist/js/pages/dashboard/leadslist.js',
    '/static/dist/js/pages/sms/deposit/direct.js',
    '/static/dist/js/pages/sms/message/editsms.js',
    '/static/dist/js/pages/sms/message/schedule.js',
    '/static/dist/js/pages/sms/message/sendsms.js',
    '/static/dist/js/pages/sms/credit/account.js',
    '/static/dist/js/pages/sms/message/createmessage.js',
    '/static/dist/js/pages/sms/groups/deletegroup.js',
    '/static/dist/js/pages/sms/groups/editgroup.js',
    '/static/dist/js/pages/sms/groups/grouplist.js',
    '/static/dist/js/pages/sms/sms.js',
    '/static/dist/js/pages/sms/message/thismessage.js',
    '/static/dist/js/pages/sms/groups/upcontacts.js',
    '/static/dist/js/pages/sms/groups/creategroups.js',
    '/static/dist/js/pages/sms/groups/thisgroup.js',
    '/static/dist/js/pages/surveys/contacts/mycontacts.js',
    '/static/dist/js/pages/surveys/contacts/sublist.js',
    '/static/dist/js/pages/surveys/multi/survey.js',
    '/static/dist/js/pages/surveys/multi/surveyquestions.js',
    '/static/dist/js/pages/surveys/orders/neworder.js',
    '/static/dist/js/pages/surveys/orders/subpayment.js',
    '/static/dist/js/pages/surveys/schedules/schedules.js',
    '/static/dist/js/pages/surveys/schedules/subschedule.js',
    '/static/dist/js/pages/surveys/accounts.js',
    '/static/dist/js/pages/surveys/mainsurvey.js',
    '/static/dist/js/pages/surveys/survey.js',
    '/static/dist/js/pages/users/accept.js',
    '/static/dist/js/pages/users/invites.js',
    '/static/dist/js/pages/users/users.js',
    '/static/dist/js/pages/contact/ticketChat.js',
    '/static/dist/js/pages/dashboard/subTicketChat.js',
    '/static/dist/js/pages/dashboard/SupportTickets.js',
    '/static/dist/js/pages/account/managecredits.js',
    '/static/dist/js/pages/fax/fax.js',
    '/static/dist/js/pages/fax/account.js',
    '/static/dist/js/pages/organization/org.js',
    '/static/dist/js/client.js',
    '/static/dist/js/social/jquery.floating-social-share.min.js'
    ]);

toolbox.router.default = toolbox.cacheFirst;

//Routers
toolbox.router.get('/',toolbox.cacheFirst);
toolbox.router.get('/contact/.*',toolbox.cacheFirst);
toolbox.router.get('/account/.*',toolbox.cacheFirst);
toolbox.router.get('/admin/.*',toolbox.cacheFirst);
toolbox.router.get('/sms/.*',toolbox.cacheFirst);
toolbox.router.get('/advertise/.*',toolbox.cacheFirst);
toolbox.router.get('/adverts/.*',toolbox.cacheFirst);
toolbox.router.get('/surveys/.*',toolbox.cacheFirst);
toolbox.router.get('/affiliates/.*',toolbox.cacheFirst);
toolbox.router.get('/dashboard/.*',toolbox.cacheFirst);
toolbox.router.get('/navigation/header', toolbox.cacheFirst);
toolbox.router.get('/navigation/sidebar', toolbox.cacheFirst);
toolbox.router.get('/navigation/footer', toolbox.cacheFirst);
toolbox.router.get('/static/.*', toolbox.cacheFirst);
toolbox.router.get('/.*', toolbox.cacheFirst);
