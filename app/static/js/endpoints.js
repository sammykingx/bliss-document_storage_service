const AUTH_ENDPOINTS = {
    LOGIN: '/checkpoint', //user login
    LOGOUT: '/logout',  // user logout
    RESET_PASSWORD: '/reset_password', // reset password
    RESET_PASSWORD_REQUEST: '/request_email_token', // request for password reset
};

const USER_ENDPOINTS = {
    USER_DASHBOARD: '/dashboard', // user dashboard page
    USER_PROFILE: '/profile', // user profile page
    USER_PROFILE_UPDATE: '/update_profile', // update user profile
    USER_PROFILE_IMAGE: '/update_profile_image', // update user profile image
    USER_PROFILE_PASSWORD: '/update_profile_password', // update user password
};

const DOCUMENTS_ENDPOINTS = {
    All_DOCUMENTS: '/all_documents', // documents page
    UPLOAD_DOCUMENTS: '/upload_documents', // upload document
    DELETE_DOCUMENTS: '/delete_documents', // delete document
    DOWNLOAD_DOCUMENTS: '/download_documents', // download document
};

export { AUTH_ENDPOINTS, USER_ENDPOINTS, DOCUMENTS_ENDPOINTS };