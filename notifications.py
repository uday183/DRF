def sound_notification(registration_id):
    push_service = FCMNotification(api_key = FCM_API_KEY)
    for each in registration_id:
        result = push_service.notify_single_device(registration_id=each,
                                                       
                                                       sound="default",
                                                       badge=1,
                                                       message_title="Title",
                                                        message_body="data Available",

                                                       )

def background_notification(registration_id,*argv):
    
    push_service = FCMNotification(api_key = FCM_API_KEY)
    data_message={}
    data_message = {
            "alert":argv[0],
            }
    for each in registration_id:
        result = push_service.notify_single_device(registration_id=each,
                                                    data_message = data_message,
                                                    content_available=True,
                                                    )
