from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm12 import riled_horn

card = PokemonCardDef(
    guid="0fa9c356-157f-5863-9ef8-0b2b36db10fd",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heracross.Name",
    display_name="Heracross",
    searchable_by=["Heracross", "Basic", "Heracross"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=214,
    abilities=[
        Attack(
            title="Lunge Out",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title="Riled Horn",
            game_text="If your opponent has any TAG TEAM Pok\u00e9mon in play, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="+",
            effect=riled_horn,
        ),
    ],
)