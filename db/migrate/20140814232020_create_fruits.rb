class CreateFruits < ActiveRecord::Migration
  def change
    create_table :fruits do |t|
      t.string :name
      t.string :latinName
      t.text :otherNames
      t.text :description
      t.string :image

      t.timestamps
    end
  end
end
