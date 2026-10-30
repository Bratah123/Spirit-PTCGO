from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import return_self_to_hand_on_flip


card = PokemonCardDef(
    guid="71c9276e-ac17-55e4-9c49-668327af5be4",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysStaryu.Name",
    display_name="Misty's Staryu",
    searchable_by=["Misty's Staryu", "Basic", "MistysStaryu"],
    subtypes=["Basic"],
    collector_number=92,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=120,
    abilities=[
        Attack(
            title="Star Boomerang",
            game_text="Flip a coin. If heads, return Misty's Staryu and all cards attached to it to your hand. (Either way, this attack does its damage.)",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=return_self_to_hand_on_flip(heads=True),
        ),
    ],
)
