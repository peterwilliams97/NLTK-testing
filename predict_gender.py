from __future__ import division
"""

Predict gender from a name.

Uses NLTK to do so

Created on 30/10/2010

@author: peter
"""
import sys, optparse, nlptest

        
if __name__ == '__main__':
    
    parser = optparse.OptionParser('usage: python ' + sys.argv[0] + ' [options] <name1> <name2> ...')
    parser.add_option('-c', '--classifier', action='store_true', dest='classify_only', default=False, help='use classifier only')
    parser.add_option('-d', '--dict', action='store_true', dest='dict_only', default=False, help='use dictionaray look-up only')
    parser.add_option('-v', '--verbose', action='store_true', dest='verbose', default=False, help='show details in output')
    
    (options, args) = parser.parse_args()

    if len(args) < 2:
        print parser.usage
        print 'options:', options
        print 'args', args
        exit()
        
    if options.classify_only and options.dict_only:
        print 'need one prediction method'
        exit()

    for name in args:
        gender, method = nlptest.predictGender(name, options.classify_only, options.dict_only)
        details = '(' + method + ')' if options.verbose else ''
        print '%20s is %-6s' % (name, gender), details
            
