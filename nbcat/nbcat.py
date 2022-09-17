from __future__ import print_function
import argparse, sys
import sys
import json


def print_flush(*args, **kwargs):
    end = kwargs.pop('end', '')
    print(*args, **kwargs, end=end)
    sys.stdout.flush()


class NBcat:

    COMMENT = "# "

    def __init__(self,
                 notebook: dict,
                 align: bool,
                 pad_width: int = 16):
        """
        Args:
            notebook : A parsed json of notebook content
            str      : Stream object, e.g. std::cout
            align    : Align prompt for copy. (e.g. IN [...], OUT [...])
            pad_witdh: Padding width for prompt, when align == false
        """
        self.root = notebook
        self.align = align
        self.pad_width = pad_width
        self.padding = "" if align else " " * pad_width

    # Returns -1 on error.
    # Returns 0 in normal.
    def display(self):
        self.show_splitline()
        for cell in self.root['cells']:
            self.display_cell(cell)
            self.show_splitline()
        return 0

    def show_header(self, hdr: str):
        hdr = f"`{hdr}`"
        left = (self.pad_width - len(hdr)) // 2
        if self.align:
            print_flush(f"{self.COMMENT}{hdr}", end='\n')
        else:
            right = self.pad_width - left - len(hdr)
            print_flush(f"{self._pad_n(left)}{hdr}{self._pad_n(right)}")


    def show_splitline(self):
        line = "========================================"\
            "================================="
        print_flush(f"{self.padding}{line}", end='\n')
    
    def show_sub_splitlint(self):
        sub_line = "----------------------------------------"\
            "---------------------------------"
        print_flush(f"{self.padding}{sub_line}", end='\n') 

    @staticmethod
    def _pad_n(n):
        return ' ' * n

    def display_cell(self, cell):
        pad_flag = False
        cell_type = cell['cell_type']
        if cell_type == 'raw':
            self.show_header('raw')
        elif cell_type == 'code':
            self.show_count(cell['execution_count'], 'In')
        elif cell_type == 'markdown':
            self.show_header('markdown')
        else:
            return
        
        for source_text in cell['source']:
            if pad_flag:
                print_flush(f"{self.padding}")
            else:
                pad_flag = True;
            print_flush(source_text)
        print_flush('\n')

        if 'outputs' not in cell or len(cell['outputs']) == 0:
            return
        self.show_sub_splitlint()

        pad_flag = False
        out_flag = True
        for output in cell['outputs']:
            output_type = output['output_type']
            if output_type == 'stream':
                self.show_header(output['name'])
                self.show_textplain(output['text'], False)
                pad_flag = True
            elif output_type == 'execute_result':
                if out_flag:
                    self.show_count(cell['execution_count'], 'Out')
                    out_flag = False
                    pad_flag = False
                self.show_textplain(output['data']['text/plain'], pad_flag)
            else:
                self.show_discard(output)
            print_flush('\n')

    
    def show_count(self, j, leading: str):
        """ 
        leading: one of {"In", "Out"}
        """
        num_str = " " if j is None else j
        if leading == 'In':
            out = f"{leading} [{num_str}]: "
        elif leading == 'Out':
            out = f"{leading}[{num_str}]: "
        else:
            raise ValueError(f"Unknown leading {leading}.")
        if self.align:
            print_flush(f"{self.COMMENT}{out}", end='\n')
        else:
            print_flush(f"{self._pad_n(self.pad_width - len(out))}{out}")
    
    """ Display texts/codes """
    def show_textplain(self, texts, pad_flag: bool):
        for text in texts:
            if pad_flag:
                print_flush(self.padding)
            else:
                pad_flag = True
            print_flush(text)
    
    """ Display discarded messages on unsupport data, e.g. images """
    def show_discard(self, j):
        if 'data' in j and 'text/plain' in j['data']:
            text = j['data']['text/plain']
        else:
            text = None
        if text is None:
            print_flush(
                f"{self.padding}`discard output_type: {j['output_type']}`")
        else:
            text = str(text).replace("'", '"')
            print_flush(f"{self.padding}{text}")


def app_main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser("nbcat")
    parser.add_argument("notebook", type=str,
                        help='A json parsable notebook file (*.ipynb).')
    parser.add_argument('-a', '--align', action='store_true', default=False,
                        help='Align prompt (In/Out) for copy.')
    args = parser.parse_args(argv)

    with open(args.notebook, 'r') as fp:
        notebook = json.load(fp)
    nbcat = NBcat(notebook, align=args.align)
    nbcat.display()


if __name__ == '__main__':
    fname = 'examples/example-cifar10.ipynb'
    with open(fname, 'r') as fp:
        notebook = json.load(fp)
    nbcat = NBcat(notebook, align=False)
    nbcat.display()
