"""STUB: effect not implemented — do not guess mechanics.
Weavile (DP1 #40): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import nasty_plot
from spirit.game.card_effects.dp import dark_pulse

card = PokemonCardDef(
    guid="d1bf6e84-60ee-527e-b27e-e9263d2e2e01",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weavile.Name",
    display_name="Weavile",
    searchable_by=["Weavile", "Stage 1", "Weavile"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="DP1",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    family_id=215,
    abilities=[
        Attack(
            title="Nasty Plot",
            game_text="Search your deck for any 1 card and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=nasty_plot(),
        ),
        Attack(
            title="Dark Pulse",
            game_text="Does 10 damage times the total amount of Darkness Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=10,
            damage_operator="x",
            effect=dark_pulse(),
        ),
    ],
)