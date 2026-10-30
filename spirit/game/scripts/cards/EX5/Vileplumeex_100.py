"""STUB: effect not implemented — do not guess mechanics.
Vileplume ex (EX5 #100): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.ex import block_dust_passive, special_formula

card = PokemonCardDef(
    guid="5323c457-31cb-55d4-aad6-c24a4b528ff3",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vileplumeex.Name",
    display_name="Vileplume ex",
    searchable_by=["Vileplume ex", "Stage 2", "ex", "Vileplumeex"],
    subtypes=["Stage 2", "ex"],
    collector_number=100,
    set_code="EX5",
    rarity=Rarities.RareHoloEX,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    family_id=43,
    abilities=[
        Ability(
            title="Block Dust",
            game_text="As long as Vileplume ex is your Active Pok\u00e9mon, your opponent can't play any Trainer cards (except for Supporter cards) from his or her hand.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=block_dust_passive(),
        ),
        Attack(
            title="Special Formula",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep and Poisoned. If tails, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=special_formula(),
        ),
    ],
)