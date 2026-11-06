from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import raging_headbutt


card = PokemonCardDef(
    guid="d88e0f67-c5ca-5bef-8284-426d3e9956c1",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snubbull.Name",
    display_name="Snubbull",
    searchable_by=["Snubbull", "Basic", "Snubbull"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="NEO3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=209,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Raging Headbutt",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 10 damage times the number of damage counters on Snubbull. If tails, this attack does 10 damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=raging_headbutt,
        ),
    ],
)
