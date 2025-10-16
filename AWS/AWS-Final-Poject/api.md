# 1)
upload file:
  FP_Roles.yaml
  FP_Streaming.yaml
  FP_Datastores.yaml
  FP_Lambda_Compute.yaml

# 2)
SYMBOL="INTC"
API_KEY="d3h8bo9r01qstnq84kl0d3h8bo9r01qstnq84klg"
PRICE=$(curl -s "https://finnhub.io/api/v1/quote?symbol=$SYMBOL&token=$API_KEY" | jq -r .c)
DATE=$(date -u +"%Y-%m-%d")

# notice to change the url from streaming output
curl -X POST \
  https://uhegms4ngg.execute-api.us-east-1.amazonaws.com/Prod/Stock \
  -H "Content-Type: application/json" \
  -H "x-api-key: d3h8bo9r01qstnq84kl0d3h8bo9r01qstnq84klg" \
  -d "{\"symbol\": \"$SYMBOL\", \"price\": $PRICE, \"date\": \"$DATE\"}"

# 3)
FP_Analytics.yaml

# 4) 
aws glue start-crawler --name ProcessedDataCrawler

# 5)
aws glue get-crawler --name ProcessedDataCrawler --query 'Crawler.State'

# 6)
  FP_Dashboard.yaml