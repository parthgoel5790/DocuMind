class Document:
  def __init__(self,file_path,file_type):
    self.file_path=file_path
    self.file_type=file_type
  def get_filename(self):
    file_name=self.file_path.split('/')[-1]
    return file_name
  def read_content(self):
    try:
      with open(self.file_path,"r") as f:
        content=f.read()
        return content
    except:
      print(f"File Not Found {self.file_path}")
      return None

class TextDocument(Document):
  def get_metrics(self):
    text=self.read_content()
    if(text==None):
      return {}
    else:
      total_lines=len(text.split('\n'))
      total_words=len(text.split())
      unique_words=len(set(text.split()))
      return {"Total lines":total_lines,"Total words":total_words,"Number of unique words":unique_words}

class CodeDocument(Document):
  def parse_code(self):
    text=self.read_content()
    lines=text.split('\n')
    functions=[]
    classes=[]
    for i in range(0,len(lines)):
      lines[i]=lines[i].strip()
      if(lines[i].startswith("class ")):
        s=lines[i].split()[1].split('(')[0].rstrip(':')
        classes.append(s)
      if(lines[i].startswith("def ")):
        s=lines[i].split()[1].split('(')[0].rstrip(':')
        functions.append(s)
    return {"classes":classes,"functions":functions}
