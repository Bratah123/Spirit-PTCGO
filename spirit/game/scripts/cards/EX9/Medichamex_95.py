"""STUB: effect not implemented — do not guess mechanics.
Medicham ex (EX9 #95): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import place_counters
from spirit.game.card_effects.ex import sky_kick, wise_aura_passive


card = PokemonCardDef(
    guid="df7a3004-13c0-50c9-8d56-329081ae5b8b",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Medichamex.Name",
    display_name="Medicham ex",
    searchable_by=["Medicham ex", "Stage 1", "ex", "Medichamex"],
    subtypes=["Stage 1", "ex"],
    collector_number=95,
    set_code="EX9",
    rarity=Rarities.RareHoloEX,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name",
    family_id=307,
    abilities=[
        Ability(
            title="Wise Aura",
            game_text="As long as Medicham ex is your Active Pok\u00e9mon, each Pok\u00e9mon (excluding Pok\u00e9mon-ex) (both yours and your opponent's) can't use any Pok\u00e9-Powers.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=wise_aura_passive(),
        ),
        Attack(
            title="Pure Power",
            game_text="Put 3 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=place_counters(3, 'choose_any_opponent'),
        ),
        Attack(
            title="Sky Kick",
            game_text="If the Defending Pok\u00e9mon has Fighting Resistance, this attack does 60 damage plus 40 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
                        effect=sky_kick(60, 40),
        ),
    ],
)