from flask import Blueprint, request, jsonify
import requests
from models import db, Cve

main = Blueprint("main", __name__)


@main.route("/sync")
def sync_data():

    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"

    start = 0
    limit = 50

    #while True:
    for _ in range(1):

        params = {
            "startIndex": start,
            "resultsPerPage": limit
        }

        res = requests.get(url, params=params)
        data = res.json()

        total = data.get("totalResults", 0)
        items = data.get("vulnerabilities", [])

        if not items:
            break

        for item in items:

            cve_data = item.get("cve", {})
            cve_id = cve_data.get("id")

            if not cve_id:
                continue

            # skip duplicate
            old = Cve.query.filter_by(cve_id=cve_id).first()
            if old:
                continue

            desc = cve_data.get("descriptions", [{}])[0].get("value")
            pub = cve_data.get("published")
            mod = cve_data.get("lastModified")

            score = None
            metrics = cve_data.get("metrics", {})
            if "cvssMetricV31" in metrics:
                score = metrics["cvssMetricV31"][0]["cvssData"]["baseScore"]

            row = Cve(
                cve_id=cve_id,
                description=desc,
                published=pub,
                modified=mod,
                score_v3=score
            )

            db.session.add(row)

        db.session.commit()

        start += limit
        if start >= total:
            break

    return {"message": "data syncing completed. "}


@main.route("/api/cves")
def get_all():

    query = Cve.query

    year = request.args.get("year")
    min_score = request.args.get("min_score")
    sort = request.args.get("sort", "published")
    order = request.args.get("order", "asc")

    if year:
        query = query.filter(Cve.cve_id.like(f"CVE-{year}%"))

    if min_score:
        query = query.filter(Cve.score_v3 >= float(min_score))

    column = getattr(Cve, sort, Cve.published)

    if order == "desc":
        query = query.order_by(column.desc())
    else:
        query = query.order_by(column.asc())

    data = query.all()

    return jsonify([x.to_json() for x in data])


@main.route("/api/cves/<cve_id>")
def get_one(cve_id):

    item = Cve.query.filter_by(cve_id=cve_id).first()

    if not item:
        return {"error": "not found"}, 404

    return jsonify(item.to_json())