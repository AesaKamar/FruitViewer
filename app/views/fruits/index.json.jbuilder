json.array!(@fruits) do |fruit|
  json.extract! fruit, :id, :name, :latinName, :otherNames, :description, :image
  json.url fruit_url(fruit, format: :json)
end
