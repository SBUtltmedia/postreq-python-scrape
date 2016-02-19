from pyquery import PyQuery as pq
from tqdm import tqdm


def scrape_course(subject, div):
    name = subject + ' ' + div.attr.id
    title = div('h3').text()[len(name + ': '):]
    description = div('p').eq(0).text()


def scrape_page(subject):
    d = pq(url='http://sb.cc.stonybrook.edu/bulletin/current/courses/' + subject.lower())
    return [scrape_course(subject, course) for course in d('.course').items()]


def scrape_all_pages(subjects):
    return [scrape_page(subject) for subject in tqdm(subjects)]


def main():
    pass


if __name__ == '__main__':
    main()
