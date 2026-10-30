"""STUB: effect not implemented — do not guess mechanics.
Registeel ex (EX9 #100): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_all_opponents
from spirit.game.card_effects.ex import block_signal


card = PokemonCardDef(
    guid="2996ccfd-0687-535b-bcfb-4ebeaa04c1d1",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Registeelex.Name",
    display_name="Registeel ex",
    searchable_by=["Registeel ex", "Basic", "ex", "Registeelex"],
    subtypes=["Basic", "ex"],
    collector_number=100,
    set_code="EX9",
    rarity=Rarities.RareHoloEX,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=379,
    abilities=[
        Attack(
            title="Block Signal",
            game_text="If Regice ex is in play, flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
                        effect=block_signal(),
        ),
        Attack(
            title="Wide Laser",
            game_text="Does 20 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=damage_all_opponents(20),
        ),
    ],
)