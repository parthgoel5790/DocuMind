from models import Document

class IntelligenceSystem:
  def __init__(self):
    self.control={}
  def add_document(self,doc_object):
    filename=doc_object.get_filename()
    self.control[filename]=doc_object
  def search_keyword(self,keyword):
    word_dict={}
    for doc in self.control:
      content=self.control[doc].read_content()
      if(content is None):
        continue
      lines=content.split('\n')
      for line in range(0,len(lines)):
        if(keyword in lines[line]):
          if(doc not in word_dict):
            word_dict[doc]=[line+1]
          else:
            word_dict[doc].append(line+1)

    return word_dict
