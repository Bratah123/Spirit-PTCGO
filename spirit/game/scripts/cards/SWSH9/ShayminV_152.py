from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="45c3992e-7feb-57e2-a57b-f9df18e8196c",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShayminV.Name",
    display_name="Shaymin V",
    searchable_by=["Shaymin V", "Basic", "V", "ShayminV"],
    subtypes=["Basic", "V"],
    collector_number=152,
    set_code="SWSH9",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=492,
    abilities=[
        Attack(
            title="Flap",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
        Attack(
            title="Revenge Blast",
            game_text="This attack does 40 more damage for each Prize card your opponent has taken.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)