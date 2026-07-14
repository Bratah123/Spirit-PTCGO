from spirit.game.card_effects.trainers import star_gravity
from spirit.game.data_utils import Attack, PokemonToolCardDef, is_pokemon_v
from spirit.game.attributes import PokemonTypes, Rarities

card = PokemonToolCardDef(
    granted_abilities=[
        Attack(
            title="Star Gravity",
            game_text="Put damage counters on each of your opponent's Pokémon V until its remaining HP is 100. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            vstar=True,
            condition=lambda board, player_id, pokemon: is_pokemon_v(pokemon.archetype_id),
            effect=star_gravity,
        ),
    ],
    guid="a616915a-5b34-5ccc-ba24-f2753f8618db",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EarthenSealStone.Name",
    display_name="Earthen Seal Stone",
    searchable_by=["Earthen Seal Stone", "Item", "PokÃ©mon Tool"],
    subtypes=["Item", "Pokémon Tool"],
    collector_number=154,
    set_code="SWSH12",
    rarity=Rarities.RareHolo
)
