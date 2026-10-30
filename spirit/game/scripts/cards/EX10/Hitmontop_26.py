"""STUB: effect not implemented — do not guess mechanics.
Hitmontop (EX10 #26): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import bonus_if_damaged, stages_on_damaged_counters

card = PokemonCardDef(
    guid="6c5c3726-3020-5a9a-87e9-1932039bb8bb",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hitmontop.Name",
    display_name="Hitmontop",
    searchable_by=["Hitmontop", "Basic", "Hitmontop"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="EX10",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=237,
    abilities=[
        Ability(
            title="Stages of Evolution",
            game_text="As long as Hitmontop is an Evolved Pok\u00e9mon, is your Active Pok\u00e9mon, and is damaged by an opponent's attack (even if Hitmontop is Knocked Out), put 2 damage counters on the Attacking Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=stages_on_damaged_counters(2),
        ),
        Attack(
            title="Upward Kick",
            game_text="If the Defending Pok\u00e9mon already has at least 2 damage counters on it, this attack does 20 damage plus 30 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if_damaged(30, base=20),
        ),
        Attack(
            title="Spiral Kick",
            cost={PokemonTypes.COLORLESS: 4},
            damage=50,
        ),
    ],
)