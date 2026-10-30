"""STUB: effect not implemented — do not guess mechanics.
Metagross ex (EX16 #95): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import magnetic_redraw, scanblast_same_name
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="306053ec-cddd-5154-adb1-bcc7ea505d52",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metagrossex.Name",
    display_name="Metagross ex",
    searchable_by=["Metagross ex", "Stage 2", "ex", "Metagrossex"],
    subtypes=["Stage 2", "ex"],
    collector_number=95,
    set_code="EX16",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    family_id=374,
    abilities=[
        Ability(
            title="Magnetic Redraw",
            game_text="Once during your turn (before your attack), if Metagross ex is your Active Pok\u00e9mon, you may use this power. Each player shuffles his or her hand into his or her deck. Then, each player draws 4 cards. This power can't be used if Metagross ex is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=magnetic_redraw(),
        ),
        Attack(
            title="Scanblast",
            game_text="Does 70 damage to each of your opponent's Benched Pok\u00e9mon that has the same name as the Defending Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            # STUB: attack effect not implemented
            effect=scanblast_same_name(70),
        ),
    ],
)