"""STUB: effect not implemented — do not guess mechanics.
Dragonite ex δ (EX15 #91): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import disconnect_lock_items, dragon_roar_8_counters_overflow


card = PokemonCardDef(
    guid="cf4be401-a979-5e72-8ad6-87afdb1b740d",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragoniteex.Name",
    display_name="Dragonite ex δ",
    searchable_by=["Dragonite ex \u03b4", "Stage 2", "ex", "Dragoniteex"],
    subtypes=["Stage 2", "ex"],
    collector_number=91,
    set_code="EX15",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    family_id=149,
    abilities=[
        Attack(
            title="Deafen",
            game_text="Your opponent can't play any Trainer cards (except for Supporter cards) from his or her hand during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=disconnect_lock_items(),
        ),
        Attack(
            title="Dragon Roar",
            game_text="Put 8 damage counters on the Defending Pok\u00e9mon. If that Pok\u00e9mon would be Knocked Out by this attack, put any damage counters not necessary to Knock Out the Defending Pok\u00e9mon on your opponent's Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=dragon_roar_8_counters_overflow(),
        ),
    ],
)