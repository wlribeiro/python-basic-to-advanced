from classes import Writer
from classes import Pen
from classes import WriteMachine



writer = Writer('Ricardo')
pen = Pen('BIC')
write_machine = WriteMachine()

writer.tool = write_machine
writer.tool.write()