"""STUB: effect not implemented — do not guess mechanics.
Salamence δ (EX11 #14): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import fire_dance, fire_dance_attach


card = PokemonCardDef(
    guid="42b3c11f-78c1-5c56-8ce6-5c9cc49c7787",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salamence.Name",
    display_name="Salamence δ",
    searchable_by=["Salamence \u03b4", "Stage 2", "Salamence"],
    subtypes=["Stage 2"],
    collector_number=14,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIRE, PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shelgon.Name",
    family_id=373,
    abilities=[
        Attack(
            title="Fire Dance",
            game_text="Search your discard pile for a Fire Energy card and attach it to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=fire_dance(),
        ),
        Attack(
            title="Delta Blast",
            game_text="Discard a Metal Energy card attached to Salamence.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=fire_dance_attach(),
        ),
    ],
)