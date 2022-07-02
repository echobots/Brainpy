import requests

def brainly(querydata):
	# url = "https://brainly.co.id/app/ask?entry=top&q=penemu%20lampu"
	headers = requests.utils.default_headers()
	headers.update({
		'Content-Type': 'application/json; charset=utf-8',
		'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0'
	})
	formatGraphQl = """query SearchQuery($query: String!, $first: Int!, $after: ID) {
	questionSearch(query: $query, first: $first, after: $after) {
		edges {
			node {
				content
				attachments{
					url
				}
				answers {
					nodes {
						content
						attachments{
							url
						}
					}
				}
			}
		}
	}
}
"""
	query = {
		'operationName': 'SearchQuery',
		'variables': {
			'query': querydata,
			'after': None,
			'first': 100
		},
		'query': formatGraphQl
	}
	r = requests.post('https://brainly.co.id/graphql/id', headers = headers, json = query)
	return r.json()
while True:
	print('nanya apa bos ?')
	z = input()
	a = brainly(z)

	b = a["data"]["questionSearch"]["edges"]
	i = 0
	if len(b) > 0:
		for item in b:
			i += 1
			print(item["node"]["content"])
			for item2 in item["node"]["answers"]["nodes"]:
				print(item2["content"])
			if i == 3:
				break
			# print('\n\n')