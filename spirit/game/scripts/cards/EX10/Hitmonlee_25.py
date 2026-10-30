"""STUB: effect not implemented — do not guess mechanics.
Hitmonlee (EX10 #25): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.ex import stages_damage_boost


card = PokemonCardDef(
    guid="ea98211c-043a-5f11-be1c-8e360d8690d4",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hitmonlee.Name",
    display_name="Hitmonlee",
    searchable_by=["Hitmonlee", "Basic", "Hitmonlee"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="EX10",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=106,
    abilities=[
        Ability(
            title="Stages of Evolution",
            game_text="As long as Hitmonlee is an Evolved Pok\u00e9mon, Hitmonlee's attacks do 20 more damage to your opponent's Pok\u00e9mon (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            passive=stages_damage_boost(20),
        ),
        Attack(
            title="Stretch Kick",
            game_text="Choose 1 of your opponent's Benched Pok\u00e9mon. This attack does 10 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1},
            # STUB: attack effect not implemented
            effect=snipe_attack(10, also_base=True),
        ),
        Attack(
            title="Mega Kick",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)