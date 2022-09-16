while True:
    from random import randint as r
    from random import choice as c
    from time import sleep as s
    from math import floor as f

    player_num=int(input("玩家数量(建议≤10个)："))
    if player_num>=10:
        print('爬')
    if player_num>=100:
        print('捏麻麻石蜡')
        break
    player_1=[]
    player_blood=[]
    player_buff=[]
    for i in range(player_num):
        player_blood.append(1)
        player_buff.append('')

    for i in range(player_num):
        m=input(f"玩家{i+1}名称：")
        n=r(250,350)
        n1=r(1,10)
        if n1<=2:
            n-=100
        elif n>=8:
            n+=50
        player_1.append(m)
        player_blood[i]=n

    player={'name':player_1,'blood':player_blood,'buff':player_buff}

    for i in range(len(player_1)):
        ls1=player['name'][i]
        ls2=player['blood'][i]
        print(f'{ls1}的血量：{ls2}')

    roundcnt=0
    killer=[]
    lk,um,unum=0,0,0

    while True:
        roundcnt+=1
        s(0.05)

        if len(player['name'])!=len(list(set(player['name']))):
            break
        for i in range(len(player['blood'])):
            bl=player['blood'][i]
            if bl<=0:
                killer.append(player_1[i])
                killer=list(set(killer))
        if len(list(set(killer)))+1>=len(player['name']):
            break
        luckey=c(player['name'])
        unlucky=c(player['name'])
        for i in range(len(player['name'])):
            if player['name'][i]==luckey:
                luckey_num=i
        while player['blood'][luckey_num]<=0:
            luckey=c(player['name'])
            for i in range(len(player['name'])):
                if player['name'][i]==luckey:
                    luckey_num=i
        for i in range(len(player['name'])):
            if player['name'][i]==unlucky:
                unlucky_num=i
        while unlucky==luckey or player['blood'][unlucky_num]<=0:
            unlucky=c(player['name'])
            for i in range(len(player['name'])):
                if player['name'][i]==unlucky:
                    unlucky_num=i
        for i in range(len(player['buff'])):
            bf=player['buff'][i]
            if player['blood'][i]<=0:
                pass
            else:
                if bf=='强力' and lk==2:
                    pl=player['name'][i]
                    for j in range(len(player['name'])):
                        if j!=i:
                            kl=player['name'][j]
                            player['blood'][j]=-1
                            print(f'{pl}给{kl}以致命一击，{kl}寄了')
                    break
                if bf=='中毒I':
                    j=r(5,20)
                    player['blood'][i]-=j
                    zdblood=player['blood'][i]
                    zdname=player['name'][i]
                    print(f'{zdname}中毒，受到{j}点伤害\n{zdname}剩余血量{zdblood}',end='')
                    if zdblood<=0:
                        print('，寄了',end='')
                    print()
                if bf=='中毒II':
                    j=r(25,80)
                    player['blood'][i]-=j
                    zdblood=player['blood'][i]
                    zdname=player['name'][i]
                    print(f'{zdname}中毒，受到{j}点伤害\n{zdname}剩余血量{zdblood}',end='')
                    if zdblood<=0:
                        print('，寄了',end='')
                    print()
                if bf=='中毒III':
                    j=r(85,120)
                    player['blood'][i]-=j
                    zdblood=player['blood'][i]
                    zdname=player['name'][i]
                    print(f'{zdname}中毒，受到{j}点伤害\n{zdname}剩余血量{zdblood}',end='')
                    if zdblood<=0:
                        print('，寄了',end='')
                    print()
                if bf=='中毒IV':
                    j=r(150,200)
                    player['blood'][i]-=j
                    zdblood=player['blood'][i]
                    zdname=player['name'][i]
                    print(f'{zdname}中毒，受到{j}点伤害\n{zdname}剩余血量{zdblood}',end='')
                    if zdblood<=0:
                        print('，寄了',end='')
                    print()
                if bf=='中毒V':
                    player['blood'][i]=-1
                    zdname=player['name'][i]
                    print(f'{zdname}中毒，直接寄了')
                    print()
        if bf=='强力':
            break

        i=r(0,100)
        if i<=20:
            k=r(1,16)
            if k==1:
                j=r(25,50)
                print(f'{luckey}对{unlucky}发动吸血，造成{j}点伤害')
                player['blood'][unlucky_num]-=j
                player['blood'][luckey_num]+=j
                m=player['blood'][luckey_num]
                n=player['blood'][unlucky_num]
                print(f'{luckey}剩余血量{m}，{unlucky}剩余血量{n}',end='')
                if n<=0:
                    print('，寄了')
                else:
                    print()
            if k==2:
                j=r(125,175)
                print(f'{luckey}对{unlucky}发动暴击，造成{j}点伤害')
                player['blood'][unlucky_num]-=j
                n=player['blood'][unlucky_num]
                print(f'{unlucky}剩余血量{n}',end='')
                if n<=0:
                    print('，寄了')
                else:
                    print()
            if k==3:
                print(f'{luckey}技能失控，爆炸了')
                player['blood'][luckey_num]=-1
            if k==4:
                print(f'{unlucky}被{luckey}诅咒，爆炸了')
                player['blood'][unlucky_num]=-1
            if k==5:
                print(f'{luckey}与{unlucky}交换血量')
                player['blood'][luckey_num],player['blood'][unlucky_num]=player['blood'][unlucky_num],player['blood'][luckey_num]
                m=player['blood'][luckey_num]
                n=player['blood'][unlucky_num]
                print(f'{luckey}剩余血量{m}，{unlucky}剩余血量{n}')
            if k==6:
                j=r(150,200)
                print(f'{luckey}对{unlucky}发动暴击，但是受到反弹，对自己造成{j}点伤害')
                player['blood'][luckey_num]-=j
                m=player['blood'][luckey_num]
                print(f'{luckey}剩余血量{m}',end='')
                if m<=0:
                    print('，寄了')
                else:
                    print()
            if k==7:
                j=r(25,75)
                print(f'{luckey}回血{j}点')
                player['blood'][luckey_num]+=j
                m=player['blood'][luckey_num]
                print(f'{luckey}剩余血量{m}')
            if k==8:
                print(f'{luckey}对{unlucky}发动魔法攻击，扣除一半血量')
                player['blood'][unlucky_num]/=2
                n=f(player['blood'][unlucky_num])
                print(f'{unlucky}剩余血量{n}',end='')
                if n<=0:
                    print('，寄了')
                else:
                    print()
            if k==9:
                j=r(0,3)
                print(f'{luckey}对{unlucky}发动攻击，{unlucky}使用防御，造成{j}点伤害')
                player['blood'][unlucky_num]-=j
                n=f(player['blood'][unlucky_num])
                print(f'{unlucky}剩余血量{n}',end='')
                if n<=0:
                    print('，寄了')
                else:
                    print()
            if k==10:
                j=r(2,4)
                print(f'{luckey}对{unlucky}发动连击',end='')
                for z in range(j):
                    y=r(25,75)
                    if y>=50:
                        x=r(1,3)
                        if x==1:
                            pass
                        else:
                            y-=r(5,20)
                    player['blood'][unlucky_num]-=y
                    n=f(player['blood'][unlucky_num])
                    print(f'，造成{y}点伤害\n{unlucky}剩余血量{n}',end='')
                    if n<=0:
                        print('，寄了',end='')
                        break
                    else:
                        if z<j-1:
                            s(0.05)
                            print(f'\n{luckey}继续发动连击',end='')
                print(f'\n{luckey}停止连击')
            if k==11:
                print(f'{luckey}误把自己当作攻击对象')
                j=r(1,10)
                for z in range(j):
                    y=r(30,100)
                    x=r(1,10)
                    if x==1:
                        y=r(100,300)
                    print(f'{luckey}被自己薄纱，对自己造成{y}点伤害')
                    player['blood'][luckey_num]-=y
                    m=f(player['blood'][luckey_num])
                    print(f'{luckey}剩余血量{m}',end='')
                    if m<=0:
                        print(f'，寄了')
                        break
                    else:
                        print()
                    if z<j-1:
                        s(0.05)
                        print(f'{luckey}依旧发疯，大家深表同情')
            if k==12:
                j=r(2,5)
                print(f'{luckey}超级加倍')
                player['blood'][luckey_num]*=j
                m=player['blood'][luckey_num]
                if m>=1500:
                    player['blood'][luckey_num]=1500
                    print(f'{luckey}剩余血量1500，成为了一个一个野獣先辈哼哼啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊')
                else:
                    print(f'{luckey}剩余血量{m}，全场震惊')
            if k==13:
                print(f'{luckey}对{unlucky}施加魔法，{unlucky}中毒')
                if player['buff'][unlucky_num]=='':
                    player['buff'][unlucky_num]='中毒I'
                elif player['buff'][unlucky_num]=='中毒I':
                    player['buff'][unlucky_num]='中毒II'
                elif player['buff'][unlucky_num]=='中毒II':
                    player['buff'][unlucky_num]='中毒III'
                elif player['buff'][unlucky_num]=='中毒III':
                    player['buff'][unlucky_num]='中毒IV'
                elif player['buff'][unlucky_num]=='中毒IV':
                    player['buff'][unlucky_num]='中毒V'
                elif player['buff'][unlucky_num]=='中毒V':
                    pass
                else:
                    player['buff'][unlucky_num]='中毒V'
                unlucky_buff=player['buff'][unlucky_num]
                print(f'{unlucky}目前中毒效果：{unlucky_buff}\n{unlucky}：哼哼啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊')
            if k==14:
                player['buff'][luckey_num]='强力'
                print(f'{luckey}成为了一拳超人，力量倍增')
                lk=r(1,2)
                if lk==1:
                    print(f'{luckey}被群殴致死')
                    player['blood'][luckey_num]=-1
            if k==15:
                un=r(1,2)
                if un==1:
                    unluckiest=luckey
                    unum=luckey_num
                else:
                    unluckiest=unlucky
                    unum=unlucky_num
                print(f'作者一怒之下鲨了{unluckiest}')
                player['blood'][unum]=-1
            if k==16:
                print(f'{luckey}一口吞下了{unlucky}',end='')
                player['blood'][luckey_num]+=player['blood'][unlucky_num]
                un=r(1,2)
                if un==1:
                    print(f'\n{luckey}发生意外，也寄了')
                    player['blood'][luckey_num]=-1
                else:
                    m=player['blood'][luckey_num]
                    print(f'{luckey}剩余血量{m}')
                player['blood'][unlucky_num]=-1

        else:
                j=r(25,75)
                if j>=50:
                    l=r(1,3)
                    if l==1:
                        pass
                    else:
                        j-=r(5,20)
                print(f'{luckey}对{unlucky}发动普通攻击，造成{j}点伤害')
                player['blood'][unlucky_num]-=j
                n=player['blood'][unlucky_num]
                print(f'{unlucky}剩余血量{n}',end='')
                if n<=0:
                    print('，寄了')
                else:
                    print()

    if len(list(set(killer)))+1==len(player['name']) or bf=='强力':
        for i in range(len(player['blood'])):
            if player['blood'][i]>0:
                winner=player['name'][i]
                winner_blood=player['blood'][i]
        print(f'{winner}胜利，剩余血量{winner_blood}')
    else:
        print('Oops……无人生还……')

    caidan=input('若要继续，请按Enter...')
    print()
    if caidan=='tt':
        break
print('你来此何干呐(其实是彩蛋')
s(1)
print('但是你好像回不去了捏')
s(5)
while True:
    print('蚌')
