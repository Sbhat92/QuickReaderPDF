from .pdfeditor import url_parser,copy_url,html_to_pdf,read_html_file,create_bs_obj,bolden_html,write_html,remove_html,main_func # noqa
import sys


if __name__ == '__main__':
	main_func(sys.argv[1], sys.argv[2], sys.argv[3])
	
