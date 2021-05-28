def cripto(msg=""):
    translate = ''
    main_alpha = ['Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii', 'Jj', 'Kk', 'Ll', 'Mm', 'Nn', 'Oo', 'Pp', 'Qq', 'Rr', 'Ss', 'Tt', 'Uu', 'Vv', 'Ww', 'Xx', 'Yy', 'Zz']
    main_char = ['!', '@', '#']

        
    for index in msg:
        for i in main_alpha:
            if index in i:
                translate += main_char[0]
                return print(translate)
            
            