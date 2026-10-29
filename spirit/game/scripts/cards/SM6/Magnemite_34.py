from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm6 import searching_magnet

card = PokemonCardDef(
    guid="3e83f226-b7a9-5da7-9c01-c759cf101cd0",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    display_name="Magnemite",
    searchable_by=["Magnemite", "Basic", "Magnemite"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="SM6",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=81,
    abilities=[
        Attack(
            title="Searching Magnet",
            game_text="Search your deck for up to 3 Lightning Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=searching_magnet,
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)
