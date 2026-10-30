"""STUB: effect not implemented — do not guess mechanics.
Gengar (DP1 #27): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import life_drain
from spirit.game.card_effects.dp import shadow_dance


card = PokemonCardDef(
    guid="9c542e80-a3f3-5f80-9b0a-ff9c0e121523",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name",
    display_name="Gengar",
    searchable_by=["Gengar", "Stage 2", "Gengar"],
    subtypes=["Stage 2"],
    collector_number=27,
    set_code="DP1",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Attack(
            title="Life Drain",
            game_text="Flip a coin. If heads, put damage counters on the Defending Pok\u00e9mon until it is 10 HP away from being Knocked Out.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=life_drain(),
        ),
        Attack(
            title="Shadow Dance",
            game_text="Put 4 damage counters on your opponent's Pok\u00e9mon in any way you like. Then, switch Gengar with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            effect=shadow_dance(4),
        ),
    ],
)