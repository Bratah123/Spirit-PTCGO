"""STUB: effect not implemented — do not guess mechanics.
Crobat δ (EX11 #2): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import disconnect_lock_items, radar_jam_lock_items


card = PokemonCardDef(
    guid="4a07d164-8f81-5f83-855b-5dce40c20727",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crobat.Name",
    display_name="Crobat δ",
    searchable_by=["Crobat \u03b4", "Stage 2", "Crobat"],
    subtypes=["Stage 2"],
    collector_number=2,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.GRASS, PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name",
    family_id=41,
    abilities=[
        Attack(
            title="Radar Jam",
            game_text="Your opponent can't play any Trainer cards (except for Supporter cards) from his or her hand during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=disconnect_lock_items(),
        ),
        Attack(
            title="Target Attack",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 40 damage to that Pok\u00e9mon. If that Pok\u00e9mon already has damage counters on it, this attack does 60 damage instead. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            effect=radar_jam_lock_items(),
        ),
    ],
)