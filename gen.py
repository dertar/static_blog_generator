import option
import re
import os
import shutil

def preparation():
    try:
        os.rmdir(option.name)
    except FileNotFoundError:
        pass
    except OSError:
        rfile = os.listdir(option.name)
        for a in rfile: 
            os.remove(option.name + '/' + a)
        os.rmdir(option.name)

    os.mkdir(option.name)
    flist = os.listdir('./themes/' + option.themes + '/')
    for a in flist:
        if (a != 'index.template') and (a != 'content.template') and (a != 'page.template'):
            shutil.copy('./themes/' + option.themes + '/' + a,'./' + option.name + '/' + a)
'''
    create file name, template , [NAME,NAME OF CONTENT]
'''
def genPage(name,template,contentInfo):
    page = open('./' + option.name + '/' + name +'.html','w',encoding='utf-8')
    templatePage = open('./themes/' + option.themes + '/' + template + '.template','r',encoding='utf-8')
    for line in templatePage:
        lem = re.search('\{@[A-Z]+@}',line)
        if lem:
            if lem.group(0) == '{@TITLE@}':
                line = line.replace('{@TITLE@}',option.title)
            elif lem.group(0) == '{@WHILECONTENT@}':
                    line = ''
                    for a in option.content:
                        line += option.linkContent.format(a[1]+'.html',a[0])
            elif lem.group(0) == '{@BOTTOMNAME@}':
                line = line.replace('{@BOTTOMNAME@}',option.bottomName)
            elif lem.group(0) == '{@TITLEART@}':
                line = line.replace('{@TITLEART@}',contentInfo[0])
            elif lem.group(0) == '{@CONTENT@}':
                htmlContent = open('./content/' + contentInfo[1] ,'r',encoding='utf-8')
                for c in htmlContent:
                    page.write(c)
                htmlContent.close()
                line = ''
            elif lem.group(0) == '{@MENU@}':
                line = ''
                for a in option.menu:
                    if a[1] == name + '.html':
                        line += option.linkUP.format(a[0])
                    else :
                        line += option.linkMenu.format(a[1],a[0])
        page.write(line)
    templatePage.close()
    page.close()    


def main():
    preparation()
    genPage('index','index',['index','index'])
    for a in option.content:
        genPage(a[1],'content',a)
    genPage('program','page',['Programs','program'])
    genPage('link','page',['link','link'])
    print('blog generated at "' + option.name + '" folder')


if __name__ == '__main__':
    main()