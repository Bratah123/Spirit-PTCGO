"""STUB: effect not implemented — do not guess mechanics.
Vaporeon (EX10 #19): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import attach_energy_from_hand, damage_then, aqua_supply


card = PokemonCardDef(
    guid="28b1f5d4-29eb-546e-98f9-e82527270bb2",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vaporeon.Name",
    display_name="Vaporeon",
    searchable_by=["Vaporeon", "Stage 1", "Vaporeon"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="EX10",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Aqua Supply",
            game_text="You may attach a basic Energy card from your hand to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=damage_then(attach_energy_from_hand(count=1)),
        ),
        Attack(
            title="Multi Bubble",
            game_text="If Vaporeon has 3 or more different types of basic Energy cards attached to it, this attack does 40 damage plus 20 more damage and the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=aqua_supply(),
        ),
    ],
)