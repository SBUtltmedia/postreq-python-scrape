from pyquery import PyQuery as pq
from tqdm import tqdm
from src.utils import flatten


def scrape_requirement_paragraph(p):
    parts = p.text().split(':', 1)
    if len(parts) < 2:  # TODO: Allow extra data (# of credits, etc.)
        return []
    else:
        return {parts[0]: parts[1].strip()}


def scrape_course(subject, div):
    return {
        'course': subject + ' ' + div.attr.id,
        'name': div('h3').text()[9:],
        'description': div('p').eq(0).text(),
        'requirements': flatten([scrape_requirement_paragraph(p) for p in div('p').filter(lambda i: i != 0).items()])
    }


def scrape_page(subject):
    d = pq(url='http://sb.cc.stonybrook.edu/bulletin/current/courses/' + subject.lower())
    return [scrape_course(subject, course) for course in d('.course').items()]


def scrape_all_pages(subjects):
    return [scrape_page(subject) for subject in tqdm(subjects)]


def main():
    pass


if __name__ == '__main__':
    main()
