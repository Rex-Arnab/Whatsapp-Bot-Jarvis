##def trns(word,lang="en"):
        #    trans = tr(to_lang=lang)
        #    trans = trans.translate(word)
        #    return trans
        #reg = match.group("msg")
        #reg = reg.split(" ")
        #lang=reg[0]
        #word=" ".join(reg[1:])
        #text = trns(word,lang)
        return TextMessageProtocolEntity(word + " <=> " + text , to=message.getFrom())
