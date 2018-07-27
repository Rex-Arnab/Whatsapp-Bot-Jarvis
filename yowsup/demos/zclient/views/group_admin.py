from threading import Timer
from yowsup.layers.protocol_groups.protocolentities.iq_groups_participants_promote import PromoteParticipantsIqProtocolEntity
from yowsup.layers.protocol_groups.protocolentities.iq_groups_participants_demote import DemoteParticipantsIqProtocolEntity
from yowsup.layers.protocol_groups.protocolentities.iq_groups_subject import SubjectGroupsIqProtocolEntity
from yowsup.layers.protocol_groups.protocolentities.iq_groups_info import InfoGroupsIqProtocolEntity
from yowsup.layers.protocol_groups.protocolentities.iq_groups_list import ListGroupsIqProtocolEntity
from yowsup.layers.protocol_groups.protocolentities.iq_groups_participants_add import AddParticipantsIqProtocolEntity
from yowsup.layers.protocol_groups.protocolentities.iq_groups_participants_remove import \
    RemoveParticipantsIqProtocolEntity
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
from yowsup.layers.protocol_groups.protocolentities import *
from yowsup.layers.protocol_profiles.protocolentities    import *
from yowsup.layers.protocol_groups import YowGroupsProtocolLayer
from yowsup.demos.zclient.views.include import get
from yowsup.demos.zclient.views import config
import time
def assertConnected(): 
    return True 


class GroupAdminViews():

    def __init__(self, interface_layer):
        self.user_list = ["918739056123@s.whatsapp.net","917492952988@s.whatsapp.net","918553060687@s.whatsapp.net","918402913971@s.whatsapp.net"]
        self.interface_layer = interface_layer
        self.routes = [
            # Kick with optional time parameter in seconds
            ("^kick\s(?P<phone_number>[0-9]{8,14})\s*(?P<time>[0-9]{2,3})?\s*$", self.kick),
            ("^add\s(?P<phone_number>[0-9]{8,14})\s*$", self.add),
            ("^cast (?P<status>[^$]+)$", self.broad),
            ("^user.pic\s(?P<phone_number>[0-9]{8,14})\s*$", self.contact_picturePreview),
            ("^add_all$", self.addall),
            ("^group.list$", self.group_list),
            ("^group.info$", self.group_info),
            ("^kick_all$", self.kickall),
            ("group.subject (?P<status>[^$]+)$", self.group_subject),
            ("^ban\s(?P<phone_number>[0-9]{8,14})\s*$", self.ban),
            ("^op\s(?P<phone_number>[0-9]{8,14})\s*$", self.op),
            ("^dop\s(?P<phone_number>[0-9]{8,14})\s*$", self.dop),
        ]

    def group_subject(self, message, match):
        if self._is_authorized(message):
            subject = match.group("status")
            self._set_sub(message.getFrom(), subject)

    def contact_picturePreview(self, message, match):
        if self.assertConnected():
            jid = self._get_jid(match.group("phone_number"))
            entity = GetPictureIqProtocolEntity(self.aliasToJid(jid), preview=True)
            self._sendIq(entity, self.onGetContactPictureResult)

    def group_list(self, message, match):
        #if self._is_authorized(message):
        self._list_group()

    def group_info(self, message, match):
        #if self._is_authorized(message):
        self._group_info(message.getFrom())

    def broad(self, message, match):
        subject = match.group("status")
        if "https://youtu.be/" in subject:
            subject = "https://www.youtube.com/watch?v=pEyWyMhEq2U&t=160s"
        f = open("contact.txt","r")
        txt = f.read()
        f.close()
        txt = txt.split("\n")
        self.interface_layer.toLower(TextMessageProtocolEntity("Processing", to=message.getFrom()))
        for num in txt:
            user = self._get_jid(num)
            self.interface_layer.toLower(TextMessageProtocolEntity(subject, to=user))
            

        


    def addall(self, message, match):
        if self._is_authorized(message):
            for user in self.user_list:
                self._add_user(message.getFrom(), user)
            self.interface_layer.toLower(TextMessageProtocolEntity("Done", to=message.getFrom()))

    def kickall(self, message, match):
        if self._is_authorized(message):
            for user in self.user_list:
                self._remove_user(message.getFrom(), user)
            self.interface_layer.toLower(TextMessageProtocolEntity("Done", to=message.getFrom()))

    

    def kick(self, message, match):
        if self._is_authorized(message):
            #users = ["919851478875@s.whatsapp.net","9851478875"]
            if "9851478875" in message.getAuthor():
                self.interface_layer.toLower(TextMessageProtocolEntity("Not Allowed", to=message.getFrom()))
            else:
                jid_kick = self._get_jid(match.group("phone_number"))
                self._remove_user(message.getFrom(), jid_kick)
                kick_duration = int(match.group("time")) if match.group("time") else 15
                Timer(kick_duration, self._add_user, (message.getFrom(), jid_kick)).start()
                notify_message = "[%s kicked for %d seconds]" % (match.group("phone_number"), kick_duration)
                self.interface_layer.toLower(TextMessageProtocolEntity(notify_message, to=message.getFrom()))
            #else:
            #   self.interface_layer.toLower(TextMessageProtocolEntity("Can not Kick Arnab", to=message.getFrom()))
    def add(self, message, match):
        if self._is_authorized(message):
            jid_add = self._get_jid(match.group("phone_number"))
            self._add_user(message.getFrom(), jid_add)
            time.sleep(1)
            try:
                self.interface_layer.toLower(TextMessageProtocolEntity(get("welcome"), to=message.getFrom()))
            except:
                self.interface_layer.toLower(TextMessageProtocolEntity(get("welcome"), to=message.getFrom()))
                
    def ban(self, message, match):
        if self._is_authorized(message):
            if "9851478875" in message.getAuthor():
                jid_ban = self._get_jid(match.group("phone_number"))
                self._remove_user(message.getFrom(), jid_ban)
                
            else:
                self.interface_layer.toLower(TextMessageProtocolEntity("Nice Try", to=message.getFrom()))

    def op(self, message, match):
        if self._is_authorized(message):
            if "9851478875" in message.getAuthor():
                jid_kick = self._get_jid(match.group("phone_number"))
                self._op_user(message.getFrom(), jid_kick)
                time.sleep(1)
                self.interface_layer.toLower(TextMessageProtocolEntity(jid_kick+" is Admin", to=message.getFrom()))
            else:
                self.interface_layer.toLower(TextMessageProtocolEntity("Nice Try", to=message.getFrom()))

    def dop(self, message, match):
        if self._is_authorized(message):
            if "9851478875" in message.getAuthor():
                jid_kick = self._get_jid(match.group("phone_number"))
                self._dop_user(message.getFrom(), jid_kick)
                time.sleep(1)
                self.interface_layer.toLower(TextMessageProtocolEntity(jid_kick+" is no longer Admin", to=message.getFrom()))
            else:
                self.interface_layer.toLower(TextMessageProtocolEntity("Nice Try", to=message.getFrom()))

    def _is_authorized(self, message):
        """
            Check if bot is authorized to add/remove users.
            For now just checks if the message is in group,
            # TO-DO: check if bot is in fact admin!
            # issue:
        """
        """if config.filter_groups:
            isAllowed = False
            for jid, isAdmin in message.getParticipants().iteritems():
                if jid.split("@")[0] in config.admins:
                    isAllowed = True
                    break
                else:
                    isAllowed = False
        else:
            isAllowed = True
            """
        return message.isGroupMessage()
        #return isAllowed

    def _get_jid(self, phone_number):
        """
            Build jid based on phone number.
        """
        return "%s@s.whatsapp.net" % phone_number

    def aliasToJid(self, calias):
        for alias, ajid in self.jidAliases.items():
            if calias.lower() == alias.lower():
                return Jid.normalize(ajid)

        return Jid.normalize(calias)

    def jidToAlias(self, jid):
        for alias, ajid in self.jidAliases.items():
            if ajid == jid:
                return alias
        return jid

    def _remove_user(self, group_jid, user_jid):
        entity = RemoveParticipantsIqProtocolEntity(group_jid, [user_jid, ])
        self.interface_layer.toLower(entity)

    def _add_user(self, group_jid, user_jid):
        entity = AddParticipantsIqProtocolEntity(group_jid, [user_jid, ])
        self.interface_layer.toLower(entity)
        
    def _op_user(self, group_jid, user_jid):
        entity = PromoteParticipantsIqProtocolEntity(group_jid, [user_jid, ])
        self.interface_layer.toLower(entity)

    def _dop_user(self, group_jid, user_jid):
        entity = DemoteParticipantsIqProtocolEntity(group_jid, [user_jid, ])
        self.interface_layer.toLower(entity)

    def _set_sub(self, group_jid, subject):
        entity = SubjectGroupsIqProtocolEntity(group_jid, subject.upper())
        self.interface_layer.toLower(entity)

    def _list_group(self):
        entity = ListGroupsIqProtocolEntity()
        self.interface_layer.toLower(entity)

    def _group_info(self, group_jid):
        entity = InfoGroupsIqProtocolEntity(self.aliasToJid(group_jid))
        self.interface_layer.toLower(entity)
