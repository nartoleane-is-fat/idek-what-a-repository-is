import time
import os
tpe = input('Input decode, or encode! ')
if tpe == 'encode':
  message = input('Message to encode: ')
  a = message.replace('`', '`')
  b = a.replace('!', '⁄')
  c = b.replace('1', '¡')
  d = c.replace('2', '™')
  e = d.replace('#', '‹')  
  f = e.replace('3', '£')
  g = f.replace('@', '€')
  h = g.replace('$', '›')
  i = h.replace('4', '¢')
  j = i.replace('5', '∞')
  k = j.replace('%', 'ﬁ')
  l = k.replace('6', '§')
  m = l.replace('^', 'ﬂ')
  n = m.replace('7', '¶')
  o = n.replace('&', '‡')
  p = o.replace('8', '•')
  q = p.replace('*', '°')
  r = q.replace('9', 'ª')
  s = r.replace('(', '·')
  t = s.replace('0', 'º')
  u = t.replace(')', '‚') 
  v = u.replace('-', '–')
  w = v.replace('_', '—')
  x = w.replace('=', '≠')
  y = x.replace('+', '±')
  z = y.replace('q', 'œ')
  aa = z.replace('w', '∑')
  ab = aa.replace('e', '´')
  ac = ab.replace('r', '®')
  ad = ac.replace('t', '†')
  ae = ad.replace('y', '¥')
  af = ae.replace('u', '¨')
  ag = af.replace('i', 'ˆ')
  ah = ag.replace('o', 'ø')
  ai = ah.replace('p', 'π')
  aj = ai.replace('[', '“')
  ak = aj.replace('{', '”')
  al = ak.replace(']', '‘')
  am = al.replace('}', '‘')
  ao = am.replace('|', '»')
  ap = ao.replace('a', 'å')
  aq = ap.replace('s', 'ß')
  ar = aq.replace('d', '∂')
  aß = ar.replace('f', 'ƒ')
  at = aß.replace('g', '©')
  au = at.replace('h', '˙')
  av = au.replace('j', '∆')
  aw = av.replace('k', '˚')
  ax = aw.replace('l', '¬')
  ay = ax.replace(';', '…')
  az = ay.replace(':', 'Ú')
  ba = az.replace('’', 'æ')
  bb = ba.replace('"', 'Æ')
  bc = bb.replace('z', 'Ω')
  bd = bc.replace('x', '≈')
  be = bd.replace('c', 'ç')
  bf = be.replace('v', '√')
  bg = bf.replace('b', '∫')
  bh = bg.replace('n', '˜')
  bi = bh.replace('m', 'µ')
  bj = bi.replace(',', '≤')
  bk = bj.replace('<', '¯')
  bl = bk.replace('.', '≥')
  bm = bl.replace('>', '˘')
  bn = bm.replace('/', '÷')
  bo = bn.replace('?', '¿')
  bp = bo.replace('Z', '¸')
  bq = bp.replace('X', '˛')
  br = bq.replace('C', 'Ç')
  bs = br.replace('V', '◊')
  bt = bs.replace('B', 'ı')
  bu = bt.replace('N', 'ദ')
  bv = bu.replace('M', 'Â')
  bw = bv.replace('A', 'Å')
  bx = bw.replace('S', 'Í')
  by = bx.replace('D', 'Î')
  bz = by.replace('F', 'Ï')
  ca = bx.replace('G', '˝')
  cb = ca.replace('H', 'Ó')
  cc = cb.replace('J', 'Ô')
  cd = cc.replace('K', '')
  ce = cd.replace('L', 'Ò')
  cf = ce.replace('Q', 'Œ')
  cg = cf.replace('W', '„')
  ch = cg.replace('E', '⁰')
  ci = ch.replace('R', '‰')
  cj = ci.replace('T', 'ˇ')
  ck = cj.replace('Y', 'Á')
  cl = ck.replace('U', 'လ')
  cm = cl.replace('I', 'ඞ')
  cn = cm.replace('O', 'Ø')
  co = cn.replace('P', '∏')
  print(co)
elif tpe == 'decode':
    message = input('Message to decode: ')
    a = message.replace('`', '`')
    b = a.replace('⁄', '!')
    c = b.replace('¡', '1')
    d = c.replace('™', '2')
    e = d.replace('‹', '#')
    f = e.replace('£', '3')
    g = f.replace('€', '@')
    h = g.replace('›', '$')
    i = h.replace('¢', '4')
    j = i.replace('∞', '5')
    k = j.replace('ﬁ', '%')
    l = k.replace('§', '6')
    m = l.replace('ﬂ', '^')
    n = m.replace('¶', '7')
    o = n.replace('‡', '&')
    p = o.replace('•', '8')
    q = p.replace('°', '*')
    r = q.replace('ª', '9')
    s = r.replace('·', '(')
    t = s.replace('º', '0')
    u = t.replace('‚', ')')
    v = u.replace('–', '-')
    w = v.replace('—', '_')
    x = w.replace('≠', '=')
    y = x.replace('±', '+')
    z = y.replace('œ', 'q')
    aa = z.replace('∑', 'w')
    ab = aa.replace('´', 'e')
    ac = ab.replace('®', 'r')
    ad = ac.replace('†', 't')
    ae = ad.replace('¥', 'y')
    af = ae.replace('¨', 'u')
    ag = af.replace('ˆ', 'i')
    ah = ag.replace('ø', 'o')
    ai = ah.replace('π', 'p')
    aj = ai.replace('“', '[')
    ak = aj.replace('”', '{')
    al = ak.replace('‘', ']')
    am = al.replace('’', '}')
    ao = am.replace('»', '|')
    ap = ao.replace('å', 'a')
    aq = ap.replace('ß', 's')
    ar = aq.replace('∂', 'd')
    aß = ar.replace('ƒ', 'f')
    at = aß.replace('©', 'g')
    au = at.replace('˙', 'h')
    av = au.replace('∆', 'j')
    aw = av.replace('˚', 'k')
    ax = aw.replace('¬', 'l')
    ay = ax.replace('…', ';')
    az = ay.replace('Ú', ':')
    ba = az.replace('æ', '’')
    bb = ba.replace('Æ', '"')
    bc = bb.replace('Ω', 'z')
    bd = bc.replace('≈', 'x')
    be = bd.replace('ç', 'c')
    bf = be.replace('√', 'v')
    bg = bf.replace('∫', 'b')
    bh = bg.replace('˜', 'n')
    bi = bh.replace('µ', 'm')
    bj = bi.replace('≤', ',')
    bk = bj.replace('¯', '<')
    bl = bk.replace('≥', '.')
    bm = bl.replace('˘', '>')
    bn = bm.replace('÷', '/')
    bo = bn.replace('¿', '?')
    bp = bo.replace('¸', 'Z')
    bq = bp.replace('˛', 'X')
    br = bq.replace('Ç', 'C')
    bs = br.replace('◊', 'V')
    bt = bs.replace('ı', 'B')
    bu = bt.replace('ദ', 'N')
    bv = bu.replace('Â', 'M')
    bw = bv.replace('Å', 'A')
    bx = bw.replace('Í', 'S')
    by = bx.replace('Î', 'D')
    bz = by.replace('Ï', 'F')
    ca = bx.replace('˝', 'G')
    cb = ca.replace('Ó', 'H')
    cc = cb.replace('Ô', 'J')
    cd = cc.replace('', 'K')
    ce = cd.replace('Ò', 'L')
    cf = ce.replace('Œ', 'Q')
    cg = cf.replace('„', 'W')
    ch = cg.replace('⁰', 'E')
    ci = ch.replace('‰', 'R')
    cj = ci.replace('ˇ', 'T')
    ck = cj.replace('Á', 'Y')
    cl = ck.replace('လ', 'U')
    cm = cl.replace('ඞ', 'I')
    cn = cm.replace('Ø', 'O')
    co = cn.replace('∏', 'P')
    print(co)
elif tpe == 'access_data':
  print('Accessing Online Archives.')
  time.sleep(0.5)
  print('.')
  time.sleep(0.5)
  print('.')
  time.sleep(0.5)
  print('.')
  time.sleep(0.5)
  print('.')
  time.sleep(0.5)
  print('.')
  time.sleep(0.5)
  yessir = input('Archives Accessed. What would you like to do? ')
  if yessir == 'delete':
    arch = input('What would you like to delete? ')
    if arch == 'everything':
      yorn = input('Are you sure? This will delete the entire internet. ')
      if yorn == 'yes':
        print('Okay. Internet deleted.')
      elif yorn == 'no':
        print('Okay. Will not go forward with transaction')
      else: 
        print('Please try again')
    elif arch == 'oliver goold':
      print('Information deleted. Good riddance. Screw him and his stupid battlecats.')
    elif arch == 'august kovse':
      print('Information deleted. Good riddance. He is literally the colour orange.')
    elif arch == 'finnian lovely':
      print('Information deleted. Good riddance. He was obsessed with hi-chew.')
    elif arch == 'nicholas zhou':
      print('Information deleted. Good riddance. He supplied that madman with the hi-chews.')
    elif arch == 'ben pollard':
      ben = input('Are you sure? He can track whenever someone says yes to this question. ')
      if ben == 'yes':
        print('Okay. Prepare to die. ALERT: WAIT 30 SECONDS FOR A SURPRISE')
        time.sleep(30)
        print('Look behind you.')
        time.sleep(6)
        print('Nah jk lol you ight')
      elif ben == 'no':
        print('Okay. Will not go forward with transaction')
      else: 
        print('Please try again')
    elif arch == 'hi-chews' or arch == 'hi-chew':
      time.sleep(1)
      print('.')
      time.sleep(1)
      print('.')
      time.sleep(1)
      print('.')
      time.sleep(1)
      print("I have accessed your hard drive and given your address to the FBI, as you are clearly unstable and a menace to society.\nWhy would a sane person ever want to delete hi-chews? \nDoesn't matter anymore now anyway, because you're no longer a risk.\n\n\n;)")
    else:
      print('Information deleted.')
  elif yessir == 'edit':
    edited = input('What would you like to edit? ')
    editee = input('What would you like to change this data to? ')
    print(f"Okay. data_{edited} has been changed to data_{editee}.")
  elif yessir == 'add':
    added = input('What would you like to add? ')
    if added == 'nicholas zhou' or added == 'finnian lovely' or added == 'august kovse' or added == 'oliver goold' or added == 'ben pollard':
      print('No. Theres enough of them already.')
    elif added == 'sophie pollard':
      print('GOD NO PLEASE I WILL NOT DO IT NEVER MAKE ME THINK ABOUT TWO OF HER AGAIN!')
    else:
      print(f'Okay. data_{added} has been added')
  elif yessir == 'function':
    name = input('What is the name of this function? ')
    func = input('What would you like this function to do? ')
    print(f'Okay. func_{name} will now {func}')
  elif yessir == 'vbucks':
    sure = input('Are you sure? ')
    if sure == 'yes':
      sure = input('Are you sure? ')
      if sure == 'yes':
        sure = input('Are you sure? ')
        if sure == 'yes':
          print("Welcome to a text adventure. You will say 'yes' or 'no' to use to answer each question.\nOn some questions there will be multiple options labelled a, b, c, or d. These will usually be for talking.")
          continuel = input('EG: Would you like to continue? ')
          if continuel == 'no':
            print('Okay. GAME OVER.')
          elif continuel == 'yes':
            nme = input("Great! What is your name? ")
            if nme == '' or nme == ' ':
              print('Please enter a valid name.') 
            else:
              time.sleep(0.5)
              os.system('clear')
              inv = input('You wake up in your house. You look over at the clock. 7:00 AM. You look outside. The sun is in the air, the birds are singing, when you hear a bang downstairs.\nDo you investigate? ')
              if inv == 'no':
                os.system('clear')
                print('You go back to sleep and decide to ignore the bang, never to wake up or be seen again. GAME OVER.')
              elif inv == 'yes':
                os.system('clear')
                pot = input('You get out of bed and walk downstairs. As you enter the kitchen, you notice the front door open, and a pan on the floor. Type yes to investigate the door, type no to investigate pan. ')
                if pot == 'yes':
                  os.system('clear')
                  amogus = input('You go through the door, and step outside, look around and shrug. Do you investigate the rest of the house? Type no to go back to sleep. ')
                  if amogus == 'no':
                    os.system('clear')
                    print('You decide it was the wind and go back to sleep, never to wake up or be seen again. GAME OVER.')
                  elif amogus == 'yes':
                    os.system('clear')
                    print('Once you have explored all bedrooms, living room and kitchen, you check inside the laundry. You see a man, and that is the last thing you ever see. GAME OVER.')
                  else:
                    os.system('clear')
                    print("Please say 'yes' or 'no'.")
                elif pot == 'no':
                  os.system('clear')
                  door = input(f"You, for some reason, decide the pan is more suspicious, and as you get closer, you see it was majorly scratched in the fall. You tsk, realising you have to buy a new one, before noticing that the scratches were hand-drawn. They read: Hello {nme}. Shut and open the door 3 times, and then say 'hippity hoppity I am a hippototomaus'. HINT: REMEMBER THIS. Do you listen and follow the instructions? ")
                  if door == 'no':
                    os.system('clear')
                    amogus = input("You ignore the pan's messages and go through the door normally, step outside, look around and shrug. Do you investigate the rest of the house? Type no to go back to sleep. ")
                    if amogus == 'no':
                      os.system('clear')
                      print('You decide it was the wind and go back to sleep, never to wake up or be seen again. GAME OVER.')
                    elif amogus == 'yes':
                      os.system('clear')
                      print('Once you have explored all bedrooms, living room and kitchen, you check inside the laundry. You see a man, and that is the last thing you ever see. GAME OVER.')
                    else:
                      os.system('clear')
                      print("Please say 'yes' or 'no'.")
                  elif door == 'yes':
                    os.system('clear')
                    what = input("You walk up to the door, turn the knob 3 times, and then... type 'yes' if you say 'hippity hoppity I am a hippopotamus' and type 'no' if you say 'hippity hoppity I am a hippototomaus'. ")
                    if what == 'yes':
                      os.system('clear')
                      time.sleep(1.5)
                      print("You doubt that you were meant to say the incorrect spelling, so you say the word with the correct spelling in your head. As soon as you begin to say 'hippopotamus', you fall through floor and land on moist, yellow carpet. As you look at the obnoxious wall panneling, and flickering overhead lights, you realise you have noclipped into the backrooms. You slowly get up and look around. You wander the backrooms for all eternity. GAME OVER.")                   
                    elif what == 'no':
                      os.system('clear')
                      portal = input("As you finish saying the word 'hippototomaus', the door turns into a portal before your very eyes. Do you enter? ")
                      if portal == 'no':
                        os.system('clear')
                        print('You go back to sleep and decide to ignore the damn magic portal to another dimension, never to wake up or be seen again. GAME OVER.')
                      elif portal == 'yes':
                        os.system('clear')
                        enter = input("You enter the door, and you exit in the clouds. You feel scared at first, but then calm, as you realise you're floating on air. Suddenly, you begin to fall, slowly at first, but with gradually increasing speed. Do you admit defeat and fall to your death? ")
                        if enter == 'yes':
                          os.system('clear')
                          print("As you fall to your death, you close your eyes bracing for impact. GAME OVER.")
                        elif enter == 'yes':
                          os.system('clear')
                          land = input('You frantically flail your arms around, and realise you dramatically slow down. You begin to soar through the air like a bird, the wind rushing past your ears. You fly over mountains and rivers. Do you land? Say no to keep flying. ')
                          if land == 'yes':
                            os.system('clear')
                            print(f'You slowly fly to the ground, when you hear a growling behind you. You see a rhino charging full speed at you. This is the last thing you ever see. The ironic thing was, it sounded like he was trying to say {nme}. GAME OVER.')
                          elif land == 'no':
                            os.system('clear')
                            mountain = input("You continue to soar through the air, and see a rhino below you. You think about how lucky you are you didn't land. You see a mountain up ahead and land carefully on it. Do you fly down? Type no to gradually walk down.")
                            if mountain == 'yes':
                              os.system('clear')
                              stop = input('You spread your arms and begin to fly down. Picking up speed, you feel exhilarated. You realise you are picking up speed at an uncontrollable rate. Do you try to stop? Type no to let yourself die.')
                              if stop == 'yes':
                                os.system('clear')
                                print('Too late. You splatter on the ground and die. GAME OVER.')
                              elif stop == 'no':
                                os.system('clear')
                                print('You let yourself splatter on the ground and die. GAME OVER.')
                              else:
                                os.system('clear')
                                print("Please say 'yes' or 'no'.")
                            elif mountain == 'no':
                              os.system('clear')
                              yessiiir = input("You slowly walk down the mountain. As you do, you think about who made the clatter. You realise that it was your cousins handwriting. You look around and see that there is a wooden hut in a clearing. Do you go to it? Type no to ignore it. ")
                              if yessir == 'no': 
                                print('You ignore the man-made wooden hut and keep exploring. You go for days and days without food, and eventually die of starvation. GAME OVER.')
                              elif yessir == 'yes':
                                innerdemon = input("You fly down to the hut and knock on the door. The door opens to reveal a man, about 29, staring back at you with a gaping mouth. Do you greet him? Type no to leave and run away. ") 
                                if innerdemon == 'no':
                                  print(f'You ignore the man keep exploring as you run away your hear him shout your name {nme}. You go for days and days without food, and eventually die of starvation. GAME OVER.')
                                elif innerdemon == 'yes':
                                  idkr = print('You greet him and he explains his name, edward, how hes been alone in the world for thousands of years, and talks about how he found a tapestry lying on the ground with something drawn on it. You share your experiences and have a laugh. You live on this island together forever and have a joyous, time, flying over mountains and valleys, holding hands. THE END. Please type anything to gain ending, and bragging rights.')
                                  if idkr != '':
                                    os.system('clear')
                                    print('You unlocked the main ending! Congratulations!')
                                else:
                                  os.system('clear')
                                  print("Please say 'yes' or 'no'.")
                              else:
                                os.system('clear')
                                print("Please say 'yes' or 'no'.")
                            else:
                              os.system('clear')
                              print("Please say 'yes' or 'no'.")
                          else:
                            os.system('clear')
                            print("Please say 'yes' or 'no'.")
                        else:
                          os.system('clear')
                          print("Please say 'yes' or 'no'.")
                      else:
                        os.system('clear')
                        print("Please say 'yes' or 'no'.")
                    else:
                      os.system('clear')
                      print("Please say 'yes' or 'no'.")
                  else:
                    os.system('clear')
                    print("Please say 'yes' or 'no'.")
                else: 
                  os.system('clear')
                  print("Please say 'yes' or 'no'.")
              else:
                os.system('clear')
                print("Please say 'yes' or 'no'.")
          else:
            os.system('clear')
            print("Please say 'yes' or 'no'.")
        else:
          os.system('clear')
          print('Okay.')
      else:
        os.system('clear')
        print('Okay.')
    else:
      os.system('clear')
      print('Okay.')
  elif yessir == 'view':
    view = input('What do you want to view? ') 
    if view == 'functions':
      print('Some functions are:\n1. add,\n2. delete,\n3. function,\n4. edit,\n5. view,\n6. idk,\n7. vbucks.\nDO NOT USE VBUCKS. I definitely did not code an entire text adventure into here.')
    elif view == 'victims':
      print("Some victims are:\n1. Oliver Goold,\n2. August Kovse,\n3. Nicholas Zhou,\n4. Finnian Lovely,\n5. Dwayne 'The Rock' Johnson,\n6. Bill Nye 'The Science Guy'.")
    elif view == 'viewables':
      print('Some viewables are:\n1. functions,\n2. victims,\n3. viewables.')
    else:
      print(f"Sorry, I didn't get that. Please type viewables instead of {view}.")
  elif yessir == 'idk':
    print('Cool. Me neither. Remember when this was a normal decoder? Life was easier back then.')
  else:
    print("Sorry, I didn't get that. Please use add, delete, function, edit, or view.")
else:
  print("Sorry, I couldn't understand that! If you want to encode something, type encode! If you want to decode something, type decode! Press the play button to try again.")
