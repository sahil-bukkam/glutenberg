from fastapi import Request


def build_page_url(request: Request, new_page: int) -> str:
    base_url = str(request.url).split("?")[0]
    query_params = dict(request.query_params)
    query_params["page"] = str(new_page)
    return base_url + "?" + "&".join(f"{k}={v}" for k, v in query_params.items())
