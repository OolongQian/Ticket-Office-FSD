#ifndef MYYMT_USER_H
#define MYYMT_USER_H

#include "constant.h"
#include "utility.h"
#include <iostream>

/**
 * I'm rather confused about privilege.
 * privilege seems to be an integer, but which integer represents admin, what about common loser?
 * I current let privilege 0 mean loser, and non-zero mean admin. */
namespace sjtu {

    class user_key {
    public:
        char username[ID_SIZE];

        user_key() {}
        user_key(const char *other) {
            strcpy(username, other);
        }
        /// overload huge amount of functions.
        bool operator<(const user_key &other) {
            return strcmp(username, other.username) < 0;
        }
        bool operator<=(const user_key &other) {
            return strcmp(username, other.username) <= 0;
        }
        bool operator!=(const user_key &other) {
            return strcmp(username, other.username) != 0;
        }
        bool operator==(const user_key &other) {
            return strcmp(username, other.username) == 0;
        }

        user_key &operator=(const user_key &other) {
            strcpy(username, other.username);
            return *this;
        }

        void read() {
            reader(username);
        }
    };

    class user_val {
    public:
        short privilege;
        char name[NAME_SIZE];
        char password[PASSWORD_SIZE];
        char email[EMAIL_SIZE];
        char phone[PHONE_SIZE];

    public:
        /// when fail to find, default constructed object is returned.
        user_val() {
            privilege = -1;
        }

        /// moving assign operator.

        user_val &operator=(const user_val &other) {
            privilege = other.privilege;
            strcpy(name, other.name);
            strcpy(password, other.password);
            strcpy(email, other.email);
            strcpy(phone, other.phone);
            return *this;
        }
        /**
         * read from std::cin. fill data field except user_id. */
        void read() {
            reader(name);
            reader(password);
            reader(email);
            reader(phone);
        }

        /// return whether this object is null object, which means it's constructed in default.
        bool null_obj() {
            return privilege == -1;
        }
    };
}

#endif //MYYMT_USER_H
