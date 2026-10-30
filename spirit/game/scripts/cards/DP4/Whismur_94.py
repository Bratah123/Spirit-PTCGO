"""DP4 Great Encounters — wired.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import mud_spit_snipe


card = PokemonCardDef(
    guid="b1cf1f58-5bcd-5954-b2d1-78c1c4e1fc73",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whismur.Name",
    display_name="Whismur",
    searchable_by=["Whismur", "Basic", "Whismur"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="DP4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=293,
    abilities=[
        Attack(
            title="Mumble",
            cost={},
            damage=10,
        ),
        Attack(
            title="Uproar",
            game_text="Flip a coin. If heads, this attack does 10 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=mud_spit_snipe(10),
        ),
    ],
)