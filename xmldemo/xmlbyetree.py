import xml.etree.ElementTree as ET
tree=ET.parse('test.xml')
root = tree.getroot()
for child in root:
    # 第二层节点的标签名称和属性
    print(child.tag,":", child.attrib)
    print(child.keys())#打印element的属性序列
    # 遍历xml文档的第三层
    for children in child:
        # 第三层节点的标签名称和属性
        #print(children.tag, ":", children.text)
        ET.dump(children)
movies=root.find('movie')
e=ET.Element('new')
e.set('desc','test')
e.text='haha,success'
movies.append(e)
tree.write('test.xml')
