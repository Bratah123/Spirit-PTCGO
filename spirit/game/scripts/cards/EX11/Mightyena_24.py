"""STUB: effect not implemented — do not guess mechanics.
Mightyena δ (EX11 #24): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import delta_fang_lock_ex, gang_up_dark_metal
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="53b1e488-1e79-58ec-acae-d0e8820299f5",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mightyena.Name",
    display_name="Mightyena δ",
    searchable_by=["Mightyena \u03b4", "Stage 1", "Mightyena"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="EX11",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.DARKNESS, PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poochyena.Name",
    family_id=261,
    abilities=[
        Attack(
            title="Delta Fang",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, that Pok\u00e9mon can't attack during your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=delta_fang_lock_ex(),
        ),
        Attack(
            title="Gang Up",
            game_text="Does 10 damage times the number of Darkness Pok\u00e9mon and Metal Pok\u00e9mon you have in play.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=gang_up_dark_metal(10),
        ),
    ],
)