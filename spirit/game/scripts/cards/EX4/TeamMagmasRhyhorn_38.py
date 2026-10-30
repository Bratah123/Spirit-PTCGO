"""STUB: effect not implemented — do not guess mechanics.
Team Magma's Rhyhorn (EX4 #38): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.ex import damage_each_active


card = PokemonCardDef(
    guid="c75fa241-16a2-5804-8f39-e1334b6109dc",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasRhyhorn.Name",
    display_name="Team Magma's Rhyhorn",
    searchable_by=["Team Magma's Rhyhorn", "Basic", "TeamMagmasRhyhorn"],
    subtypes=["Basic"],
    collector_number=38,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=111,
    abilities=[
        Attack(
            title="Double Damage",
            game_text="Does 10 damage to each Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=damage_each_active(10),
        ),
        Attack(
            title="Horn Rush",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=flip_or_nothing(),
        ),
    ],
)