"""STUB: effect not implemented — do not guess mechanics.
Milotic ex (EX9 #96): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import magma_ring_no_retreat, mystic_scale_discard_tms, mystic_scale_passive, reflect_energy_basic


card = PokemonCardDef(
    guid="2ac32853-57c3-5cca-9639-dad2fd18a733",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miloticex.Name",
    display_name="Milotic ex",
    searchable_by=["Milotic ex", "Stage 1", "ex", "Miloticex"],
    subtypes=["Stage 1", "ex"],
    collector_number=96,
    set_code="EX9",
    rarity=Rarities.RareHoloEX,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    family_id=349,
    abilities=[
        Ability(
            title="Mystic Scale",
            game_text="As long as Milotic ex is in play, each player can't play any Technical Machine cards from his or her hand. Discard all Technical Machine cards in play (both yours and your opponent's).",
            ability_type=AbilityTypes.POKE_BODY,
            passive=mystic_scale_passive(),
        ),
        Ability(
            title="Mystic Scale",
            game_text="Discard all Technical Machine cards in play (both yours and your opponent's).",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.ON_EVOLVE,
            effect=mystic_scale_discard_tms,
        ),
        Ability(
            title="Mystic Scale",
            game_text="Discard all Technical Machine cards in play (both yours and your opponent's).",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.BETWEEN_TURNS,
            effect=mystic_scale_discard_tms,
        ),
        Attack(
            title="Gentle Wrap",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=magma_ring_no_retreat(),
        ),
        Attack(
            title="Reflect Energy",
            game_text="Move 1 basic Energy card attached to Milotic ex to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
                        effect=reflect_energy_basic(),
        ),
    ],
)