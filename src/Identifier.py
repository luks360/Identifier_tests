def valid_s(ch):
    if (((ch >= 'A') and (ch <= 'Z')) or ((ch >= 'a') and (ch <= 'z'))):
        return True
    else:
        return False

def valid_f(ch):
    if (((ch >= 'A') and (ch <= 'Z')) or ((ch >= 'a') and (ch <= 'z')) or ((ch > '0') and (ch <= '9'))):
        return True
    else:
        return False

def validateIdentifier(s):
    achar = ''
    valid_id = False;

    if (len(s) > 0):
        achar = s[0]
        valid_id = valid_s(achar);

        if (len(s) > 1):
            achar = s[1]                
            i = 0
            while (i < len(s)):
                achar = s[i]
                if (valid_f(achar) == False):
                    valid_id = False                    
                i += 1

        if valid_id and (len(s) >= 1) and (len(s) <= 6):
            return True
        else:
            return False

if __name__ == '__main__':
    id = input("Digite o id: ")
    if(len(id) == 0):
        print("Erro: Digite um valor");
    else:
        if(validateIdentifier(id)):
            print("Valido")
        else:
            print("Invalido")