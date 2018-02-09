from core.labels import Vision
from core.crypt import Aes
import sys

Vision.detect_labels('{}'.format(sys.argv[1]))
