from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing, spread_damage


card = PokemonCardDef(
    guid="24f0220e-cccf-5b1e-aee7-5346cc7fe6ab",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksDiglett.Name",
    display_name="Brock's Diglett",
    searchable_by=["Brock's Diglett", "Basic", "BrocksDiglett"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=50,
    abilities=[
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=flip_or_nothing(),
        ),
        Attack(
            title="Tremor",
            game_text="Does 10 damage to each of your own Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=spread_damage(10, side="mine", also_base=True),
        ),
    ],
)
