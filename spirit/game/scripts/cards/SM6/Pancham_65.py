from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm4 import sucker_punch

card = PokemonCardDef(
    guid="a5544e39-b8dd-5185-a899-2b3d4ae30510",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pancham.Name",
    display_name="Pancham",
    searchable_by=["Pancham", "Basic", "Pancham"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="SM6",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=674,
    abilities=[
        Attack(
            title="Act Tough",
            game_text="If this Pok\u00e9mon has any Darkness Energy attached to it, this attack does 30 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator="+",
            effect=sucker_punch,
        ),
    ],
)
