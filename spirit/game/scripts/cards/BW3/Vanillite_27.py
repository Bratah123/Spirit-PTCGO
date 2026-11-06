from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus

card = PokemonCardDef(
    guid="8bb04aed-9cda-5884-973e-dd73b1ae1e88",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillite.Name",
    display_name="Vanillite",
    searchable_by=["Vanillite", "Basic", "Vanillite"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="BW3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=582,
    abilities=[
        Attack(
            title="Icicle Barb",
            game_text="Flip a coin. If heads, this attack does 10 more damage.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(10),
        ),
    ],
)
