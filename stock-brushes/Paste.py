from pymclevel.materials import Block
from editortools.brush import createBrushMask
import mcplatform
import pymclevel

displayName = 'Paste'

def createInputs(self):
    self.inputs = (
    {'Import':self.importSchematic},
    )    
    
def importSchematic(self):
    pass
    
def getDirtyBox(self, point, size):
    pass

def applyToChunkSlices(op, chunk, slices, brushBox, brushBoxThisChunk):
    brushMask = createBrushMask(op.tool.getBrushSize(), op.options['Style'], brushBox.origin, brushBoxThisChunk, op.options['Noise'], op.options['Hollow'])

    blocks = chunk.Blocks[slices]
    data = chunk.Data[slices]

    airFill = op.options['Fill Air']

    if airFill == False:
        airtable = numpy.zeros((materials.id_limit, 16), dtype='bool')
        airtable[0] = True
        replaceMaskAir = airtable[blocks, data]
        brushMask &= ~replaceMaskAir

    chunk.Blocks[slices][brushMask] = op.options['Block'].ID
    chunk.Data[slices][brushMask] = op.options['Block'].blockData