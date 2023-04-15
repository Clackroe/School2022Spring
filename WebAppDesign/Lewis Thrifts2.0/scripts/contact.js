$(function () {
    fm_options = {
		feedback_url : "",
        position : "left-top",
        jQueryUI : false,
        bootstrap : false,
        show_email : false,
        show_radio_button_list : false,
        close_on_click_outisde: true,
        name_label : "Name",
  
        message_label : "Message",
        
        submit_label : "Send",
        title_label : "Contact Form",
        trigger_label : "Contact Me!",
        custom_params : {},
        show_form: true,
        custom_html: "",
        delayed_close : true,
        
	};

	fm.init(fm_options);
});